from utils.puzzle_repository import PuzzleRepository
from calendar.one.solutions import DayOne
from calendar.two.solutions import DayTwo
from calendar.three.solutions import DayThree
from calendar.four.solutions import DayFour


def setup_solutions() -> dict:
    puzzle_repository = PuzzleRepository()

    return {
        "day_one": DayOne(puzzle_repository).solution,
        "day_two": DayTwo(puzzle_repository).solution,
        "day_three": DayThree(puzzle_repository).solution,
        "day_four": DayFour(puzzle_repository).solution,
    }


if __name__ == "__main__":
    solutions = setup_solutions()

    for key in solutions.keys():
        thunk = solutions[key]
        thunk()
