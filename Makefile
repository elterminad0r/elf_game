stats.md: src/datasets file_analysis.zsh src/stats.py
	echo -n > stats.md
	echo "name | avg / £ | sd / £ | var / £<sup>2</sup> | min / £ | LQ / £ | med / £ | UQ / £ | max / £ | mode / £ | mode freq / % | sample" >> stats.md
	echo "---|---|---|---|---|---|---|---|---|---|---|---" >> stats.md
	./file_analysis.zsh | sort -k 3,3 -r >> stats.md

descs.md: src/stats.py get_descs.py
	python get_descs.py src/*.py > descs.md
