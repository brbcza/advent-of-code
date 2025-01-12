# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/6
from typing import Optional

import numpy as np
from aocd.models import Puzzle


class AoC2024Day6:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._pos = np.array([0, 0])
        self._direction = np.array([-1, 0], dtype=int)
        self._visited: set[tuple[int, int]] = set()
        self._map = np.array([])
        self._load_input(data_path, data)
        self._initial_pos = self._pos.copy()

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for r, line in enumerate(data.splitlines()):
            line = line.strip()
            row = np.zeros(len(line), dtype=int)
            for c, char in enumerate(line):
                if char == "#":
                    row[c] = 1
                elif char == "^":
                    self._pos = np.array([r, c], dtype=int)
            self._map = np.vstack([self._map, row]) if self._map.size else row

    def _reset(self):
        self._pos = self._initial_pos.copy()
        self._direction = np.array([-1, 0])

    def _move(self):
        next_pos = self._pos + self._direction
        while self._map[next_pos[0], next_pos[1]] == 1:
            self._direction = np.array([[0, 1], [-1, 0]]).dot(self._direction)
            next_pos = self._pos + self._direction
        self._pos = next_pos

    def get_visited_count(self):
        self._reset()
        while (
            self._pos[0] >= 0
            and self._pos[0] < self._map.shape[1] - 1
            and self._pos[1] >= 0
            and self._pos[1] < self._map.shape[0] - 1
        ):
            self._move()
            self._visited.add((self._pos[0], self._pos[1]))
        return len(self._visited)

    def get_loop_count(self):
        self._reset()
        loop_count = 0
        visited: set[tuple[int, int, int, int]] = set()
        for r, c in self._visited:
            if self._map[r, c] == 1:
                continue
            elif np.array_equal(self._pos, np.array([r, c])):
                continue
            self._map[r, c] = 1
            while (
                self._pos[0] >= 0
                and self._pos[0] < self._map.shape[1] - 1
                and self._pos[1] >= 0
                and self._pos[1] < self._map.shape[0] - 1
            ):
                self._move()
                if (
                    self._pos[0],
                    self._pos[1],
                    self._direction[0],
                    self._direction[1],
                ) in visited:
                    loop_count += 1
                    break
                visited.add(
                    (self._pos[0], self._pos[1], self._direction[0], self._direction[1])
                )
            self._map[r, c] = 0
            self._reset()
            visited.clear()
        return loop_count


def main():
    puzzle = Puzzle(year=2024, day=6)
    solver = AoC2024Day6(data=puzzle.input_data)
    visited_count = solver.get_visited_count()
    loop_count = solver.get_loop_count()

    print(f"PART 1: Number of visited position is {visited_count}")
    print(f"PART 2: Number of loops is {loop_count}")


if __name__ == "__main__":
    main()
