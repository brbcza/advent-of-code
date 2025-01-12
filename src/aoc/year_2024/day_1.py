# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/1
from typing import Optional

import numpy as np
from aocd.models import Puzzle


class AoC2024Day1:
    _data: np.ndarray[int, int]

    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._load_data(data_path, data)

    def _load_data(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            self._data = np.loadtxt(data_path, dtype=int)
        elif data:
            self._data = np.loadtxt(data.splitlines(), dtype=int)
        else:
            raise ValueError("No data provided")

    def compute_distance(self):
        c1 = self._data[:, 0]
        c2 = self._data[:, 1]
        c1.sort()
        c2.sort()
        distance = np.sum(np.abs(c1 - c2))
        return distance

    def compute_simmilarity(self):
        c1 = self._data[:, 0]
        c2 = self._data[:, 1]
        simmilarity = 0
        for item in c1:
            simmilarity += item * np.count_nonzero(c2 == item)
        return simmilarity


def main():
    puzzle = Puzzle(year=2024, day=1)
    solver = AoC2024Day1(data=puzzle.input_data)
    distance = solver.compute_distance()
    simnilarity = solver.compute_simmilarity()

    print(f"PART 1: Distance between colums is {distance}")
    print(f"PART 2: Simmilarity between colums is {simnilarity}")


if __name__ == "__main__":
    main()
