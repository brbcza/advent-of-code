# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/18
from queue import PriorityQueue
from typing import Optional

import matplotlib.pyplot as plt
from aocd.models import Puzzle


class AoC2024Day18:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._memory: list[tuple[int, int]] = []
        self._load_data(data_path, data)

    def _load_data(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for line in data.splitlines():
            self._memory.append(tuple(map(int, line.strip().split(","))))

    def _create_map(self, width: int, height: int, num_bytes: int) -> list[list[int]]:
        memory_map = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
        for x, y in self._memory[: num_bytes + 1]:
            memory_map[y][x] = 1
        return memory_map

    def _get_path(
        self,
        path: dict[tuple[int, int], tuple[int, int]],
        current: tuple[int, int],
    ) -> list[tuple[int, int]]:
        result = []
        while current != (0, 0):
            result.append(current)
            current = path[current]
        result.append((0, 0))
        return result[::-1]

    def _plot_map(
        self,
        memory_map: list[list[int]],
        path: dict[tuple[int, int], tuple[int, int]],
        current: tuple[int, int],
    ):
        path = self._get_path(path, current)
        for x, y in path:
            memory_map[x][y] = 2
        memory_map[0][0] = 3
        memory_map[-1][-1] = 3
        plt.clf()
        plt.imshow(memory_map)
        plt.draw()
        plt.pause(1 / 30)
        for x, y in path:
            memory_map[x][y] = 0
        memory_map[0][0] = 0
        memory_map[-1][-1] = 0

    def find_shortest_path(self, width: int, height: int, num_bytes: int) -> int:
        memory_map = self._create_map(width, height, num_bytes)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        path: dict[tuple[int, int], tuple[int, int]] = {}
        visited: set[tuple[int, int]] = set()
        queue = PriorityQueue()
        cost = 0 + (width + height)
        queue.put((cost, (0, 0, 0)))
        visited.add((0, 0))
        while not queue.empty():
            _, (x, y, distance) = queue.get()
            # self._plot_map(memory_map, path, (x, y))
            if (x, y) == (width, height):
                return self._get_path(path, (x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx <= width
                    and 0 <= ny <= height
                    and memory_map[nx][ny] == 0
                    and (nx, ny) not in visited
                ):
                    cost = (distance + 1) + (abs(nx - width) + abs(ny - height))
                    queue.put((cost, (nx, ny, distance + 1)))
                    path[(nx, ny)] = (x, y)
                    visited.add((nx, ny))
        return []

    def find_blocked_path(
        self,
        width: int,
        height: int,
        num_bytes: int,
        path: list[tuple[int, int]],
    ) -> int:
        path_set = set(path)
        for (
            i,
            point,
        ) in enumerate(self._memory[num_bytes + 1 :], 1):
            if not (point[1], point[0]) in path_set:
                continue
            shortest_path = self.find_shortest_path(width, height, num_bytes + i)
            if len(shortest_path) == 0:
                return point
        return -1


def main():
    uzzle = Puzzle(year=2024, day=18)
    solver = AoC2024Day18(data=puzzle.input_data)
    shortest_path = solver.find_shortest_path(70, 70, 1024)
    blocked_path = solver.find_blocked_path(70, 70, 1024, shortest_path)

    print(f"PART 1: Shortest path to the end is {len(shortest_path) - 1}")
    print(f"PART 2: Blocked path at {blocked_path}")


if __name__ == "__main__":
    main()
