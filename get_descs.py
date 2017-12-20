"""
Scrape Python files for descriptions of algorithms
"""

import re
import argparse

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="*", type=argparse.FileType("r"), help="input files")
    return parser.parse_args()

def get_doc(docfile):
    return re.match(r'"""(.*?)"""', docfile.read(), re.MULTILINE | re.DOTALL).group(1).strip().replace("\n\n", "<br>").replace("\n", " ")

if __name__ == "__main__":
    args = get_args()
    print("Strategy filename | Strategy description")
    print("---|---")
    for f in args.input:
        doc = get_doc(f)
        if "strategy" in doc.lower():
            print("{} | {}".format(f.name.replace("_", "\\_"), doc))
