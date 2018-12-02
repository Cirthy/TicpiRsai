MAIN = main.py



all :
	python3 $(MAIN)

i:
	python3 -i $(MAIN)

cleanpy :
	rm -r __pycache__

git :
	cleanpy
	git add *
	git commit -m $(c)
	git push origin master
