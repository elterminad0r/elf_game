"""
Visualising the distributions calculated using matplotlib
"""

import argparse
import pathlib
import itertools

import numpy as np
import matplotlib.pyplot as plt

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=pathlib.Path, nargs="*", help="input file to read data from")
    parser.add_argument("--width", type=int, default=3, help="column width")
    return parser.parse_args()

def read_data(dfile):
    print("reading data")
    if dfile.exists():
        if dfile.is_file():
            print("reading data from file {}".format(dfile))
            return np.loadtxt(dfile, np.int32)
        print("recursively reading data from directory {}".format(dfile))
        return np.loadtxt(itertools.chain.from_iterable(i.open("r") for i in dfile.glob("**/*.dat")))
    raise ValueError("could not find data")

def plot_data(ax, data, dfile):
    print("plotting")
    ax.hist(data, bins=25, normed=True)
    ax.set_title("scores in {}".format(dfile))
    ax.set_xlabel("Profit / £")
    ax.set_ylabel("Probability")

if __name__ == "__main__":
    args = get_args()
    f, axes = plt.subplots((len(args.input) - 1) // args.width + 1, args.width)
    for ax, dfile in zip(itertools.chain.from_iterable(axes), args.input):
        print("working on {}".format(dfile))
        data = read_data(dfile)
        plot_data(ax, data, dfile)

    wm = plt.get_current_fig_manager()
    wm.resize(*wm.window.maxsize())
    plt.tight_layout()
    plt.savefig("figs.pdf")
    plt.show()
