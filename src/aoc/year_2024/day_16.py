# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/16
from queue import PriorityQueue
from typing import Optional

from aocd.models import Puzzle
from matplotlib import pyplot as plt


class AoC2024Day16:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._map: list[list[int]] = []
        self._start: tuple[int, int] = (0, 0)
        self._end: tuple[int, int] = (0, 0)
        self._load_input(data_path, data)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No input data provided")
        for i, line in enumerate(data.splitlines()):
            row: list[int] = []
            for j, c in enumerate(line.strip()):
                if c == "S":
                    self._start = (i, j)
                    row.append(0)
                elif c == "E":
                    self._end = (i, j)
                    row.append(0)
                elif c == "#":
                    row.append(1)
                else:
                    row.append(0)
            self._map.append(row)

    def _parse_paths(
        self,
        path: dict[tuple[int, int], set[tuple[int, int]]],
        point: tuple[int, int],
    ):
        paths: list[dict[tuple[int, int], list[tuple[int, int]]]] = []

        def find_subpath(
            path: dict[tuple[int, int], set[tuple[int, int]]],
            point: tuple[int, int],
            current_path: list[tuple[int, int]],
        ) -> list[list[tuple[int, int]]]:
            current_path.append(point)
            if point == self._start:
                paths.append(current_path)
                return
            for prev_point in path[point]:
                find_subpath(path, prev_point, current_path)

        find_subpath(path, point, [])

        return paths

    def _plot_path(
        self,
        path: dict[tuple[int, int], set[tuple[int, int]]],
        point: tuple[int, int],
        costs: dict[tuple[int, int], int] = {},
        pause: bool = False,
    ):
        paths = self._parse_paths(path, point)

        for path in paths:
            for x, y in path:
                self._map[x][y] = 2
        self._map[self._start[0]][self._start[1]] = 3
        self._map[self._end[0]][self._end[1]] = 3
        plt.clf()
        plt.imshow(self._map)
        # for (x, y), cost in costs.items():
        #    plt.text(y, x, str(cost), va="center", ha="center")
        plt.draw()
        plt.pause(1 / 5)
        if pause:
            plt.show()
        for path in paths:
            for x, y in path:
                self._map[x][y] = 0
        self._map[self._start[0]][self._start[1]] = 0
        self._map[self._end[0]][self._end[1]] = 0

    def find_lowest_cost_path(self) -> int:
        queue = PriorityQueue()
        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        seen_points: set[tuple[int, int]] = set()
        path: dict[tuple[int, int], set[tuple[int, int]]] = {}
        costs: dict[tuple[int, int], int] = {}
        num_paths = 0
        costs[self._start] = 0

        for dx, dy in directions:
            if self._map[self._start[0] + dx][self._start[1] + dy] == 0:
                next_point = (self._start[0] + dx, self._start[1] + dy)
                queue.put(
                    (
                        1 if (dx, dy) == (0, 1) else 1001,
                        (next_point[0], next_point[1], dx, dy, 1, 0),
                    )
                )
                seen_points.add(next_point)
                ancestors = path.get(next_point, set())
                ancestors.add(self._start)
                path[next_point] = ancestors

        while not queue.empty():
            cost, (x, y, odx, ody, steps, turnings) = queue.get()
            if cost <= costs.get((x, y), float("inf")):
                costs[(x, y)] = cost
            # self._plot_path(path, (x, y), costs)

            if (x, y) == self._end:
                num_paths += 1
                lowest_cost = costs.get((x, y), float("inf"))
                if cost > lowest_cost:
                    # self._plot_path(path, (x, y), costs, pause=True)
                    return lowest_cost, self._parse_paths(path, (x, y))

            next_point = (x + odx, y + ody)
            if (
                self._map[next_point[0]][next_point[1]] == 0
                and next_point not in seen_points
            ):
                queue.put(
                    (
                        cost + 1,
                        (next_point[0], next_point[1], odx, ody, steps + 1, turnings),
                    )
                )
                seen_points.add(next_point)

            if self._map[next_point[0]][next_point[1]] == 0 and (
                cost + 1 <= costs.get(next_point, float("inf"))
                or (
                    cost - 999 == costs.get(next_point, float("inf"))
                    and next_point != self._end
                )
            ):
                ancestors = path.get(next_point, set())
                ancestors.add((x, y))
                path[next_point] = ancestors

            for dx, dy in directions:
                if (
                    self._map[x + dx][y + dy] == 0
                    and (x + dx, y + dy) not in seen_points
                ):
                    queue.put((cost + 1000, (x, y, dx, dy, steps, turnings + 1)))
        return -1


def main():
    puzzle = Puzzle(year=2024, day=16)
    solver = AoC2024Day16(data=puzzle.input_data)
    min_path_cost, paths = solver.find_lowest_cost_path()
    unique_path_points = {point for path in paths for point in path}

    print(f"PART 1: Lowest cost path: {min_path_cost}")
    print(f"PART 2: Number of points on all paths {len(unique_path_points)}")


if __name__ == "__main__":
    main()
