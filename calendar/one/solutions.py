import re


class DayOne:
    def __init__(self, puzzle_repository):
        import os

        self.input = puzzle_repository.get_and_save_puzzle_from_day(
            os.path.abspath("calendar/one/input.txt"), 1
        )

    def solution(self) -> None:
        print("~~ Day One ~~")

        dict = {
            "one": "one1one",
            "two": "two2two",
            "three": "three3three",
            "four": "four4four",
            "five": "five5five",
            "six": "six6six",
            "seven": "seven7seven",
            "eight": "eight8eight",
            "nine": "nine9nine",
        }
        first_solution = 0
        second_solution = 0
        for line in self.input:
            line2 = ""
            for word in dict.keys():
                if line2 == "":
                    line2 = line.replace(word, dict[word])
                else:
                    line2 = line2.replace(word, dict[word])
            input2 = re.findall("\d", line2)
            input1 = re.findall("\d", line)
            first_solution += int(f"{input1[0]}{input1[-1]}")
            second_solution += int(f"{input2[0]}{input2[-1]}")
        print("A", first_solution)
        print("B", second_solution)
