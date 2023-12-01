MAKEFLAGS += --silent

merry_christmas: poor_santa run
	printf "\n" 
	cat tree.txt

poor_santa:
	cat santa.txt
	printf "\n" 

run:
	python ./main.py

