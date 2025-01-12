# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/10
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day10:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._map: list[list[int]] = []
        self._trailheads: list[tuple[int, int]] = []
        self._load_input(data_path, data)
        self._rows = len(self._map)
        self._cols = len(self._map[0])

    def _is_valid_coordinate(self, r: int, c: int) -> bool:
        return 0 <= r < self._rows and 0 <= c < self._cols

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for rid, line in enumerate(data.splitlines()):
            line = line.strip()
            row: list[int] = []
            for cid, c in enumerate(line):
                row.append(int(c))
                if c == "0":
                    self._trailheads.append((rid, cid))
            self._map.append(row)

    def _calculate_trailhead_score(self, trailhead: tuple[int, int]) -> int:
        points: set[tuple[int, int]] = set()

        def inner(point: tuple[int, int], height: int) -> int:
            nonlocal points
            if height == 9:
                points.add(point)
                return
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for direction in directions:
                r = point[0] + direction[0]
                c = point[1] + direction[1]
                if self._is_valid_coordinate(r, c) and self._map[r][c] == height + 1:
                    inner((r, c), height + 1)

        inner(trailhead, 0)
        return len(points)

    def _calculate_trailhead_rating(self, trailhead: tuple[int, int]) -> int:
        rating = 0

        def inner(point: tuple[int, int], height: int) -> int:
            nonlocal rating
            if height == 9:
                rating += 1
                return
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for direction in directions:
                r = point[0] + direction[0]
                c = point[1] + direction[1]
                if self._is_valid_coordinate(r, c) and self._map[r][c] == height + 1:
                    inner((r, c), height + 1)

        inner(trailhead, 0)
        return rating

    def get_trailhead_score_sum(self) -> int:
        score = 0
        for trailhead in self._trailheads:
            score += self._calculate_trailhead_score(trailhead)
        return score

    def get_trailhead_rating_sum(self) -> int:
        rating = 0
        for trailhead in self._trailheads:
            rating += self._calculate_trailhead_rating(trailhead)
        return rating


def main():
    puzzle = Puzzle(year=2024, day=10)
    solver = AoC2024Day10(data=puzzle.input_data)
    trailhead_score_sum = solver.get_trailhead_score_sum()
    trailhead_rating_sum = solver.get_trailhead_rating_sum()

    print(f"PART 1: Sum of trailhead scores is {trailhead_score_sum}")
    print(f"PART 2: Sum of trailhead ratings is {trailhead_rating_sum}")


if __name__ == "__main__":
    main()
