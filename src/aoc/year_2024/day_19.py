# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/19
from functools import cache
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day19:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._towels: list[str] = []
        self._designs: list[str] = []
        self._solutions: dict[str, bool] = {}
        self._load_input(data_path, data)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        lines = data.splitlines()
        self._towels = lines[0].strip().split(", ")
        for line in lines[2:]:
            self._designs.append(line.strip())

    @cache
    def _is_design_solveable(self, design: str) -> bool:
        count = 0
        if design == "":
            return 1
        for towel in self._towels:
            if design.startswith(towel):
                count += self._is_design_solveable(design[len(towel) :])
        return count

    def get_solvable_designs(self) -> int:
        count = 0
        sum = 0
        for design in self._designs:
            num_solutions = self._is_design_solveable(design)
            if num_solutions > 0:
                count += 1
            sum += num_solutions
        return count, sum


def main():
    puzzle = Puzzle(year=2024, day=19)
    solver = AoC2024Day19(data=puzzle.input_data)
    count, sum = solver.get_solvable_designs()

    print(f"PART 1: Number of solvable designs is {count}")
    print(f"PART 2: Number of solutions is {sum}")


if __name__ == "__main__":
    main()
