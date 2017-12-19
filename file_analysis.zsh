#!/usr/bin/zsh

echo "name | avg ± sd / £ | var / £<sup>2</sup> | min / £ | LQ / £ | med / £ | UQ / £ | max / £ | mode / £ | mode freq / % | sample";
echo "---|---|---|---|---|---|---|---|---|---|---";

for i in shrewd mvd mtn_dew libertarian early half_mountain unethical joker jefferson stingy woody twoface; do
    echo -n "$i | " | sed "s/_/\\\\_/g";
    cat src/datasets/$i/* | pypy src/stats.py --file - --quiet | sed "s/\t/ | /g";
done;
