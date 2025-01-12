# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/13
import re
from typing import Optional

import numpy as np
from aocd.models import Puzzle


class AoC2024Day13:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._equations = self.load_input(data_path, data)

    def load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        equations: list[tuple[np.array, np.array]] = []
        A = np.zeros((2, 2), dtype=np.int64)
        b = np.zeros(2, dtype=np.int64)
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for line in data.splitlines():
            if line.startswith("Button A:"):
                groups = re.match(r"Button\sA:\sX\+(\d*),\sY\+(\d*)", line)
                x = int(groups[1])
                y = int(groups[2])
                A[0][0] = x
                A[1][0] = y
            elif line.startswith("Button B:"):
                groups = re.match(r"Button\sB:\sX\+(\d*),\sY\+(\d*)", line)
                x = int(groups[1])
                y = int(groups[2])
                A[0][1] = x
                A[1][1] = y
            elif line.startswith("Prize:"):
                groups = re.match(r"Prize:\sX=(\d*),\sY=(\d*)", line)
                x = int(groups[1])
                y = int(groups[2])
                b[0] = x
                b[1] = y
                equations.append((A.copy(), b.copy()))
        return equations

    def get_token_count(self, corrections: np.array = np.zeros(2)) -> int:
        tokens = 0
        for A, b in self._equations:
            try:
                b_corrected = b + corrections
                x = np.linalg.solve(A, b_corrected)
                if np.all(A @ x.round() == b_corrected):
                    tokens += 3 * x[0] + 1 * x[1]
            except np.linalg.LinAlgError:
                continue
        return int(tokens)


def main():
    puzzle = Puzzle(year=2024, day=13)
    solver = AoC2024Day13(data=puzzle.input_data)
    token_count = solver.get_token_count()
    token_count_corrected = solver.get_token_count(10000000000000 * np.ones(2))

    print(f"PART 1: Total token count to win prices is {token_count}")
    print(
        f"PART 2: Total token count to win prices with corrections is {token_count_corrected}"
    )


if __name__ == "__main__":
    main()
