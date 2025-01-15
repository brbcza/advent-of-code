# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/20
from collections import defaultdict
from queue import PriorityQueue
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day20:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._map: list[list[int]] = []
        self._start = (0, 0)
        self._end = (0, 0)
        self._load_input(data_path, data)
        self._width = len(self._map[0])
        self._height = len(self._map)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for i, line in enumerate(data.splitlines()):
            row: list[int] = []
            for j, char in enumerate(line):
                if char == "#":
                    row.append(1)
                elif char == ".":
                    row.append(0)
                elif char == "S":
                    self._start = (i, j)
                    row.append(0)
                elif char == "E":
                    self._end = (i, j)
                    row.append(0)
            self._map.append(row)

    def _recover_path(self, path_dict: dict[tuple[int, int], tuple[int, int]]):
        path: list[tuple[int, int]] = []
        current = self._end
        while current != self._start:
            path.append(current)
            current = path_dict[current]
        path.append(self._start)
        return path[::-1]

    def _is_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self._height and 0 <= y < self._width

    def _find_path(self) -> Optional[list[tuple[int, int]]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue: PriorityQueue[tuple[int, tuple[int, int]]] = PriorityQueue()
        path: dict[tuple[int, int], tuple[int, int]] = {}
        visited: set[tuple[int, int]] = set()
        queue.put((0, self._start))
        while not queue.empty():
            dist, (x, y) = queue.get()
            if (x, y) == self._end:
                return self._recover_path(path)
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    self._is_valid(new_x, new_y)
                    and (new_x, new_y) not in visited
                    and self._map[new_x][new_y] == 0
                ):
                    queue.put((dist + 1, (new_x, new_y)))
                    visited.add((new_x, new_y))
                    path[(new_x, new_y)] = (x, y)
        return None

    def _generate_manhattan_points(
        self, point: tuple[int, int], distance: int
    ) -> dict[int, int]:
        points = []
        for offset in range(distance):
            inv_offset = distance - offset
            points.append((point[0] + offset, point[1] + inv_offset))
            points.append((point[0] + inv_offset, point[1] - offset))
            points.append((point[0] - offset, point[1] - inv_offset))
            points.append((point[0] - inv_offset, point[1] + offset))
        return points

    def _generate_manhattan_points_until(
        self, point: tuple[int, int], max_distance: int
    ) -> dict[int, int]:
        points = []
        for distance in range(2, max_distance + 1):
            generated_points = self._generate_manhattan_points(point, distance)
            points.extend(zip(generated_points, len(generated_points) * [distance]))
        return points

    def get_cheats(self, min_safe: int, cheat_distance: int):
        path = self._find_path()
        if path is None:
            return 0
        shortcuts: dict[int, int] = defaultdict(int)
        indexes: dict[tuple[int, int], int] = {}
        for index, point in enumerate(path):
            indexes[point] = index
        for dist, point in enumerate(path):
            for (
                manhattan_point,
                manhattan_point_distance,
            ) in self._generate_manhattan_points_until(point, cheat_distance):
                if not self._is_valid(*manhattan_point):
                    continue
                if not manhattan_point in indexes:
                    continue
                if self._map[manhattan_point[0]][manhattan_point[1]] == 1:
                    continue
                manhattan_point_index = indexes[manhattan_point]
                shortcut_distance = manhattan_point_index - (
                    dist + manhattan_point_distance
                )
                if shortcut_distance > 0 and shortcut_distance >= min_safe:
                    shortcuts[shortcut_distance] += 1
        return shortcuts

    def count_cheats(self, min_safe: int, cheat_distance: int):
        cheats = self.get_cheats(min_safe, cheat_distance)
        cheat_count = 0
        if len(cheats) == 0:
            return 0
        for key in sorted(cheats.keys(), reverse=True):
            # print(f"Distance: {key}, count: {cheats[key]}")
            cheat_count += cheats[key]
        return cheat_count


def main():
    puzzle = Puzzle(year=2024, day=20)
    solver = AoC2024Day20(data=puzzle.input_data)
    cheat_count = solver.count_cheats(100, 2)
    long_cheat_count = solver.count_cheats(100, 20)

    print(f"PART 1: Number of 2-long cheats is {cheat_count}")
    print(f"PART 2: Number of 20-long cheats is {long_cheat_count}")


if __name__ == "__main__":
    main()
