#!/usr/bin/zsh

for i in mvd mtn_dew libertarian early half_mountain unethical joker stingy woody twoface; do
    echo -n "$i | " | sed "s/_/\\\\_/g";
    cat datasets/$i/* | pypy stats.py --file - --quiet | sed "s/,/ | /g";
done;
