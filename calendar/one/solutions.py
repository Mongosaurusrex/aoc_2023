import os
import re

class DayOne:

    def __init__(self, puzzle_repository):
        self.input = puzzle_repository.get_and_save_puzzle_from_day(
            os.path.abspath("calendar/one/input.txt"), 1
        )

    def solution(self) -> None:

        print("~~ Day One ~~")
        
        dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        first_solution = 0
        second_solution = 0
        for line in self.input:
            line2 = ''
            for word in dict.keys():
                line2 = line.replace(word, dict[word])
            input2 = re.findall("\d", line2)
            input1 = re.findall("\d", line)
            first_solution += int(f"{input1[0]}{input1[-1]}")
            second_solution += int(f"{input2[0]}{input2[-1]}")
        print('1', first_solution)
        print('2', second_solution)
        
        

       

