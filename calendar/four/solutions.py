import os
import re
from collections import defaultdict


class DayFour:
    def __init__(self, puzzle_repository):
        self.input = puzzle_repository.get_and_save_puzzle_from_day(
            os.path.abspath("calendar/four/input.txt"), 4
        )

    def solution(self):
        print("~~ Day four ~~")

        N = defaultdict(int)
        soltion_a = 0
        for index, line in enumerate(self.input):
            N[index] += 1
            result_ticket, your_ticket = tuple(line.split(":")[1].split("|"))
            your_ticket = set(re.findall("\d+", your_ticket))
            result_ticket = set(re.findall("\d+", result_ticket))

            value_of_ticket = len((your_ticket & result_ticket))

            if value_of_ticket > 0:
                soltion_a += 2 ** (value_of_ticket - 1)

            for j in range(value_of_ticket):
                N[index + 1 + j] += N[index]

        print("A", soltion_a)
        print("B", sum(N.values()))
