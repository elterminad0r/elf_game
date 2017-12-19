#!/usr/bin/zsh

for i in src/datasets/*; do
    echo -n "$i | " | sed -e "s/.*\///g" -e "s/_/\\\\_/g";
    cat $i/* | pypy src/stats.py --file - --quiet | sed "s/\t/ | /g";
done;
