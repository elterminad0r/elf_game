#!/usr/bin/zsh

for i in datasets/*; do
    echo -n "\n$i,";
    cat $i/* | pypy stats.py --file - --quiet;
done;
