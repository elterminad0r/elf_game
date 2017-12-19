stats.md: src/datasets file_analysis.zsh
	./file_analysis.zsh > stats.md

descs.md: src get_descs.py
	python get_descs.py src/*.py > descs.md
