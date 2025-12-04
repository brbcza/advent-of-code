# (c) 2025 Filip Tefr
# https://adventofcode.com/2025/day/3
from tkinter import Grid

from aocd.models import Puzzle

_Grid = set[tuple[int, int]]


class AoC2025Day4:
    def __init__(self, data: str):
        self._grid = _Grid()
        for x, r in enumerate(data.splitlines()):
            for y, c in enumerate(r.strip()):
                if c == "@":
                    self._grid.add((x, y))

    def _get_neighbors(self, point: tuple[int, int]):
        x, y = point
        return [
            (x + dx, y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if (dx, dy) != (0, 0)
        ]

    def _can_be_accessed_by_forklift_impl(self, grid: Grid):
        accessed = _Grid()
        for point in grid:
            cnt = 0
            for n in self._get_neighbors(point):
                if n in grid:
                    cnt += 1
            if cnt < 4:
                accessed.add(point)
        return accessed

    def can_be_accessed_by_forklift(self):
        accessed = self._can_be_accessed_by_forklift_impl(self._grid)
        return len(accessed)

    def can_be_accessed_by_forklift_recursive(self):
        grid = self._grid.copy()
        cnt = 0
        while True:
            accessed = self._can_be_accessed_by_forklift_impl(grid)
            if len(accessed) == 0:
                break
            cnt += len(accessed)
            grid = grid.difference(accessed)
        return cnt


def main():
    puzzle = Puzzle(year=2025, day=4)
    solver = AoC2025Day4(data=puzzle.input_data)

    count = solver.can_be_accessed_by_forklift()
    count_resursive = solver.can_be_accessed_by_forklift_recursive()

    print(f"Rolls of paper that can be accessed by a forklift: {count}")
    print(
        f"Rolls of paper that can be accessed by a forklift recursive: {count_resursive}"
    )


if __name__ == "__main__":
    main()
