MAKEFLAGS += --silent

poor_santa:
	cat santa.txt
	printf "\n" 
day_1:
	echo "~~ Day One ~~"
	python3 ./1/solutions.py
merry_christmas: poor_santa day_1
	printf "\n" 
	cat tree.txt
