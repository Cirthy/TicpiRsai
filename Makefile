MAIN = main.py

MAIN_STATS = main_stats.py


all :
	python3 $(MAIN)

stats:
	python3 $(MAIN_STATS)



cleanpy :
	rm -r __pycache__

git : cleanpy
	git add *
	git commit -m $(c)
	git push origin master
