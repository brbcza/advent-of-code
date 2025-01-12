# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/4
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day4:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self.data = self._load_input(data_path, data)
        self.n_rows = len(self.data)
        self.n_cols = len(self.data[0])

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path) as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        return [line.strip() for line in data.splitlines()]

    def _is_index_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.n_rows and 0 <= y < self.n_cols

    def _search_word(self, x: int, y: int, dx: int, dy: int, word: str) -> bool:
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not self._is_index_valid(nx, ny) or self.data[nx][ny] != word[i]:
                return False
        return True

    def get_xmas_count(self) -> int:
        XMAS = "XMAS"
        directions = [
            (0, 1),
            (1, 0),
            (1, 1),
            (1, -1),
            (0, -1),
            (-1, 0),
            (-1, -1),
            (-1, 1),
        ]
        count = 0
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                for dx, dy in directions:
                    if self._search_word(i, j, dx, dy, XMAS):
                        count += 1
        return count

    def get_cross_mas_count(self) -> int:
        MAS = "MAS"
        count = 0
        for i in range(1, self.n_rows - 1):
            for j in range(1, self.n_cols - 1):
                if (
                    self._search_word(i - 1, j - 1, 1, 1, MAS)
                    or self._search_word(i + 1, j + 1, -1, -1, MAS)
                ) and (
                    self._search_word(i + 1, j - 1, -1, 1, MAS)
                    or self._search_word(i - 1, j + 1, 1, -1, MAS)
                ):
                    count += 1
        return count


def main():
    uzzle = Puzzle(year=2024, day=4)
    solver = AoC2024Day4(data=puzzle.input_data)
    xmas_count = solver.get_xmas_count()
    cross_mas_count = solver.get_cross_mas_count()

    print(f"PART 1: XMAS found {xmas_count} times")
    print(f"PART 2: CROSSMAS found {cross_mas_count} times")


if __name__ == "__main__":
    main()
