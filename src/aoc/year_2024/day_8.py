# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/8
from itertools import combinations
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day8:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._antennas: dict[str, list[tuple[int, int]]] = dict()
        self._rows = 0
        self._cols = 0
        self._load_input(data_path, data)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        rows = data.splitlines()
        self._rows = len(rows)
        self._cols = len(rows[0].strip())
        for r, line in enumerate(rows):
            for c, char in enumerate(line.strip()):
                if char == "." or char == "#":
                    continue
                coordinates = self._antennas.get(char, [])
                coordinates.append((r, c))
                self._antennas[char] = coordinates

    def _is_valid_coordinate(self, r: int, c: int) -> bool:
        return 0 <= r < self._rows and 0 <= c < self._cols

    def get_antinode_count(self) -> int:
        antinodes: set[tuple[int, int]] = set()
        for _, coordinates in self._antennas.items():
            for c1, c2 in combinations(coordinates, 2):
                dx = c2[0] - c1[0]
                dy = c2[1] - c1[1]
                a1 = (c1[0] - dx, c1[1] - dy)
                a2 = (c2[0] + dx, c2[1] + dy)
                if self._is_valid_coordinate(*a1):
                    antinodes.add(a1)
                if self._is_valid_coordinate(*a2):
                    antinodes.add(a2)
        return len(antinodes)

    def get_antinode_count_with_resonances(self) -> int:
        antinodes: set[tuple[int, int]] = set()
        for _, coordinates in self._antennas.items():
            for c1, c2 in combinations(coordinates, 2):
                if self._is_valid_coordinate(*c1):
                    antinodes.add(c1)
                if self._is_valid_coordinate(*c2):
                    antinodes.add(c2)
                dx = c2[0] - c1[0]
                dy = c2[1] - c1[1]
                a1 = (c1[0] - dx, c1[1] - dy)
                a2 = (c2[0] + dx, c2[1] + dy)
                while self._is_valid_coordinate(*a1):
                    antinodes.add(a1)
                    a1 = (a1[0] - dx, a1[1] - dy)
                while self._is_valid_coordinate(*a2):
                    antinodes.add(a2)
                    a2 = (a2[0] + dx, a2[1] + dy)
        return len(antinodes)


def main():
    puzzle = Puzzle(year=2024, day=8)
    solver = AoC2024Day8(data=puzzle.input_data)
    antinode_count = solver.get_antinode_count()
    antinode_count_with_resonances = solver.get_antinode_count_with_resonances()

    print(f"PART 1: Antinode count is {antinode_count}")
    print(f"PART 2: Antinode count with resonances is {antinode_count_with_resonances}")


if __name__ == "__main__":
    main()
