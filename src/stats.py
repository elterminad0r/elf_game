"""
Statistical analysis of result distributions.
"""

import os
import time
import datetime
import argparse

from math import sqrt
from collections import Counter

from sim_game import Game

# import all the strategies
from main_vd import MainVD
from unethical import Unethical
from libertarian import Libertarian
from mtn_dew import MtnDew
from woody import Woody
from stingy import Stingy
from early_inv import Early
from joker import Joker
from twoface import TwoFace
from shrewd import Shrewd

# mapping from names to callables returning a strategy. implemented like this
# in case a more complicated object wants instantiation, as this could be
# wrapped in a lambda
players = {"mvd": MainVD,
           "unethical": Unethical,
           "libertarian": Libertarian,
           "mtn_dew": lambda: MtnDew(0.2),
           "half_mountain": lambda: MtnDew(0.5),
           "woody": Woody,
           "stingy": Stingy,
           "early": Early,
           "joker": Joker,
           "twoface": TwoFace,
           "shrewd": Shrewd}

# argv handling
def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", type=int, default=10000, help="number of datasets to generate")
    parser.add_argument("--file", type=argparse.FileType("r"), default=[], nargs="*", help="file to read data from")
    parser.add_argument("--player", type=str, default=[], nargs="*", choices=players.keys(), help="player to analyse")
    parser.add_argument("--quiet", action="store_true", help="suppress non-csv output")
    return parser.parse_args()

# calculating statistics about data

def mean(data):
    mean = sum(data) / len(data)
    var = sum((i - mean) ** 2 for i in data) / len(data)
    std_dev = sqrt(var)
    return mean, std_dev, var

def mode(data):
    return Counter(data).most_common(1)[0]

# "manually" generating data, with some optional logging
def get_data(n, player, quiet):
    quiet or print("collecting data for {}".format(player))
    start = time.time()
    data = []
    quiet or print("intitialised at {:.3f}s".format(time.time() - start))
    try:
        for i in range(n):
            if i % (n // 100 or 1) == 0 and not quiet:
                print("\r({:.3f}s) progress: {:4.0%} {}".format(time.time() - start, i / n, "." * (i * 100 // n)), end="")
            data.append(Game(players[player]()).money)
    except KeyboardInterrupt:
        pass
    quiet or print("\ndone; completed {} games in {:.3f}s (that's {:.0f} games/s)".format(len(data), time.time() - start, len(data) / (time.time() - start)))
    quiet or print("sorting")
    data.sort()
    quiet or print("sorted")
    serialise(data, player, quiet)
    return data

# serialise a data set to a file, creating directories if necessary. this is
# always performed when data is generated as data can be quite expensive to
# generate.
def serialise(data, name, quiet):
    fname = datetime.datetime.now().strftime("datasets/{0}/{1}-%Y-%m-%d-%H-%M-%S.dat".format(name, len(data)))
    quiet or print("serialising to {!r}".format(fname))
    os.makedirs("datasets", exist_ok=True)
    os.makedirs("datasets/{}".format(name), exist_ok=True)
    with open(fname, "w") as datafile:
        for datum in data:
            datafile.write("{}\n".format(datum)) 
    quiet or print("serialised")

# read previously serialised data from a file
def fromfile(dfile, quiet):
    start = time.time()
    quiet or print("reading data from file")
    data = list(map(int, dfile))
    quiet or print("read data at {:.3f}".format(time.time() - start))
    data.sort()
    quiet or print("sorted data at {:.3f}".format(time.time() - start))
    return data

# boilerplate for getting and displaying statistics
def stats(data, quiet):
    av, sdev, var = map(int, mean(data))
    min_, max_ = data[0], data[-1]
    size = len(data)
    lq, med, uq = data[size // 4], data[size // 2], data[size * 3 // 4]
    modeval, occ = mode(data)
    occ /= size
    if not quiet:
        print("average £{:,} ± £{:,} (variance £²{:,})".format(av, sdev, var))
        print("min: £{:,}; max: £{:,}".format(min_, max_))
        print("LQ: £{:,}; median: £{:,}; UQ: £{:,}".format(lq, med, uq))
        print("mode £{:,} occurred {:.3%}".format(modeval, occ))
        print("sample size {:,}".format(len(data)))
    print("{:,} ± {:,}\t{:,}\t{:,}\t{:,}\t{:,}\t{:,}\t{:,}\t{:,}\t{:.4f}\t{:,}".format(av, sdev, var, min_, lq, med, uq, max_, modeval, occ * 100, size))

if __name__ == "__main__":
    args = get_args()
    for f in args.file:
        stats(fromfile(f, args.quiet), args.quiet)
    for p in args.player:
        stats(get_data(args.n, p, args.quiet), args.quiet)
