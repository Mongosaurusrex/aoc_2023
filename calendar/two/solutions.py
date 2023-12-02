from functools import reduce
import sys
import os


class DayTwo:
    def __init__(self, puzzle_repository):
        self.input = puzzle_repository.get_and_save_puzzle_from_day(
            os.path.abspath("calendar/two/input.txt"), 2
        )

    def solution(self) -> None:
        print("~~ Day Two ~~")

        game_state = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        answer1 = 0
        answer2 = 0

        limits = {"red": 12, "green": 13, "blue": 14}

        for line_num, line in enumerate(self.input):
            valid = True
            mins = {"red": 0, "green": 0, "blue": 0}

            for handful in line.strip().split(": ")[1].split("; "):
                for group in handful.split(", "):
                    count, color = group.split(" ")
                    if int(count) > limits[color]:
                        valid = False

                    if int(count) > mins[color]:
                        mins[color] = int(count)

            answer1 += line_num + 1 if valid else 0
            answer2 += reduce(lambda a, b: a * b, mins.values())

        print("A", answer1)
        print("B", answer2)
