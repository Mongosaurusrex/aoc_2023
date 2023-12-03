import os

from aocd import get_data
from dotenv import load_dotenv


class PuzzleRepository:
    def __init__(self) -> None:
        load_dotenv()

    def get_and_save_puzzle_from_day(self, to_path: str, day: int) -> str:
        if os.path.exists(to_path):
            with open(to_path, "r") as text_file:
                return text_file.read().splitlines()

        puzzle_input = get_data(
            session=os.getenv("AOC_SESSION", ""), year=2023, day=day
        )

        with open(to_path, "w") as text_file:
            text_file.write(puzzle_input)

        return puzzle_input
