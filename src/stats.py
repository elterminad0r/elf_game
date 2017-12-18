"""
Calculate some proper statistics
"""

import os
import time
import datetime
import argparse

from math import sqrt

from sim_game import Game
from main_vd import MainVD
from unethical import Unethical
from libertarian import Libertarian
from mtn_dew import MtnDew
from woody import Woody

players = {"mvd": MainVD,
           "unethical": Unethical,
           "libertarian": Libertarian,
           "mtn_dew": lambda: MtnDew(0.2),
           "woody": Woody}

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", type=int, default=10000, help="number of datasets to generate")
    parser.add_argument("--file", type=argparse.FileType("r"), help="file to read data from")
    parser.add_argument("--player", type=str, default="mvd", choices=players.keys(), help="player to analyse")
    return parser.parse_args()

def mean(data):
    mean = sum(data) / len(data)
    var = sum((i - mean) ** 2 for i in data) / len(data)
    std_dev = sqrt(var)
    return mean, std_dev, var

def get_data(n, player):
    print("collecting data for {}".format(player))
    start = time.time()
    data = []
    print("intitialised at {:.3f}s".format(time.time() - start))
    try:
        for i in range(n):
            if i % (n // 100 or 1) == 0:
                print("\r({:.3f}s) progress: {:4.0%} {}".format(time.time() - start, i / n, "." * (i * 100 // n)), end="")
            data.append(Game(players[player]()).money)
    except KeyboardInterrupt:
        pass
    print("\ndone; completed {} games in {:.3f}s (that's {:.0f} games/s)".format(len(data), time.time() - start, len(data) / (time.time() - start)))
    print("sorting")
    data.sort()
    print("sorted")
    serialise(data, player)
    return data

def serialise(data, name):
    fname = datetime.datetime.now().strftime("datasets/{0}/{1}-%Y-%m-%d-%H-%M-%S.dat".format(name, len(data)))
    print("serialising to {!r}".format(fname))
    os.makedirs("datasets", exist_ok=True)
    os.makedirs("datasets/{}".format(name), exist_ok=True)
    with open(fname, "w") as datafile:
        for datum in data:
            datafile.write("{}\n".format(datum)) 
    print("serialised")

def fromfile(dfile):
    start = time.time()
    print("reading data from file")
    data = list(map(int, args.file))
    print("read data at {:.3f}".format(time.time() - start))
    data.sort()
    print("sorted data at {:.3f}".format(time.time() - start))
    return data

if __name__ == "__main__":
    args = get_args()
    if args.file:
        data = fromfile(args.file)
    else:
        data = get_data(args.n, args.player)

    print("average £{:.0f} ± £{:.0f} (variance £²{:.0f})".format(*mean(data)))
    print("min: {}; max: {}".format(data[0], data[-1]))
    print("LQ: {}; median: {}; UQ: {}".format(data[len(data) // 4], data[len(data) // 2], data[len(data) * 3 // 4]))
