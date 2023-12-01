from utils.puzzle_repository import PuzzleRepository
from calendar.one.solutions import DayOne


def setup_solutions() -> dict:
    puzzle_repository = PuzzleRepository()

    return {"day_one": DayOne(puzzle_repository).solution}


if __name__ == "__main__":
    solutions = setup_solutions()

    for key in solutions.keys():
        thunk = solutions[key]
        thunk()

