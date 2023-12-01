import os


class DayOne:
    def __init__(self, puzzle_repository):
        self.input = puzzle_repository.get_and_save_puzzle_from_day(
            os.path.abspath("calendar/one/input.txt"), 1
        )

    def solution(self) -> None:
        print("~~ Day One ~~")
