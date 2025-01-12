# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/14
import re
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from aocd.models import Puzzle


class AoC2024Day14:
    def __init__(
        self,
        width: int,
        height: int,
        data_path: Optional[str] = None,
        data: Optional[str] = None,
    ):
        self._width = width
        self._height = height
        self._initial_positions = self.load_input(data_path, data)

    def load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        initial_positions: list[tuple[tuple[int, int], tuple[int, int]]] = []
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for line in data.splitlines():
            groups = re.match(r"p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)", line)
            position = (int(groups[1]), int(groups[2]))
            velocity = (int(groups[3]), int(groups[4]))
            initial_positions.append((position, velocity))
        return initial_positions

    def _iterate(self, positions: list[tuple[int, int]]):
        for i, (x, y) in enumerate(positions):
            updated_position = (
                (x + self._initial_positions[i][1][0]) % self._width,
                (y + self._initial_positions[i][1][1]) % self._height,
            )
            positions[i] = updated_position

    def _simulate(self, iterations: int):
        positions = [position for position, _ in self._initial_positions]
        updated_positions = []
        for i, (x, y) in enumerate(positions):
            updated_position = (
                (x + iterations * self._initial_positions[i][1][0]) % self._width,
                (y + iterations * self._initial_positions[i][1][1]) % self._height,
            )
            updated_positions.append(updated_position)
        return updated_positions

    def calculate_safety_factor(self, iterations: int):
        positions = self._simulate(iterations)
        sectors = [0, 0, 0, 0]
        width_mid = self._width // 2
        height_mid = self._height // 2
        for x, y in positions:
            if x < width_mid and y < height_mid:
                sectors[0] += 1
            elif x > width_mid and y < height_mid:
                sectors[1] += 1
            elif x < width_mid and y > height_mid:
                sectors[2] += 1
            elif x > width_mid and y > height_mid:
                sectors[3] += 1
        return sectors[0] * sectors[1] * sectors[2] * sectors[3]

    def plot_iterations(self, start: int, iterations: int, delay: float):
        positions = self._simulate(start)
        for i in range(iterations):
            self._iterate(positions)
            M = np.zeros((self._height, self._width, 3))
            for x, y in positions:
                M[y, x] = [1, 1, 1]
            plt.clf()
            plt.text(0.5, 0.5, f"Time: {start + i}")
            plt.imshow(M)
            plt.draw()
            plt.pause(delay)
        plt.show()


def main():
    puzzle = Puzzle(year=2024, day=14)
    solver = AoC2024Day14(data=puzzle.input_data)
    safety_factor = solver.calculate_safety_factor(100)
    solver.plot_iterations(7285, 1, 0)

    print(f"PART 1: Safety factor is {safety_factor}")
    print(f"PART 2: Easter egg time is {7285 + 1}")


if __name__ == "__main__":
    main()
