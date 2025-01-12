# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/12
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day12:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._map: list[list[str]] = []
        self._load_input(data_path, data)
        self.rows = len(self._map)
        self.cols = len(self._map[0])

    def _is_valid_coordinate(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def _load_input(
        self, data_path: Optional[str] = None, data: Optional[str] = None
    ) -> list[list[str]]:
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for line in data.splitlines():
            line = line.strip()
            row: list[str] = []
            for c in line:
                row.append(c)
            self._map.append(row)

    def _cluster_map(self) -> set[set[tuple[int, int]]]:
        seen_points: set[tuple[int, int]] = set()

        def find_cluster(
            r: int, c: int, neighbours: set[tuple[int, int]], id: str
        ) -> set[tuple[int, int]]:
            nonlocal seen_points
            seen_points.add((r, c))
            neighbours.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if (
                    self._is_valid_coordinate(nr, nc)
                    and self._map[nr][nc] == id
                    and (nr, nc) not in seen_points
                ):
                    find_cluster(nr, nc, neighbours, id)
            return neighbours

        clusters: list[set[tuple[int, int]]] = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in seen_points:
                    continue
                cluster = find_cluster(r, c, set(), self._map[r][c])
                clusters.append(cluster)

        return clusters

    def _get_perimeter_points(
        self, cluster: set[tuple[int, int]]
    ) -> set[tuple[int, int]]:
        perimeter_points: set[tuple[int, int]] = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r, c in cluster:
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if not (nr, nc) in cluster:
                    perimeter_points.add((r, c))
                    break
        return perimeter_points

    def _get_number_of_edges(self, point: tuple[int, int]) -> int:
        r, c = point
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        edges = 0
        for dx, dy in directions:
            nr, nc = r + dx, c + dy
            if (
                not self._is_valid_coordinate(nr, nc)
                or self._map[nr][nc] != self._map[r][c]
            ):
                edges += 1
        return edges

    def _calculate_perimeter(self, cluster: set[tuple[int, int]]) -> int:
        perimeter = 0
        for r, c in self._get_perimeter_points(cluster):
            perimeter += self._get_number_of_edges((r, c))
        return perimeter

    def _get_side_count(self, cluster: list[tuple[int, int]]) -> int:
        side_count = 0

    def calculate_price(self) -> int:
        clusters = self._cluster_map()
        price = 0
        for cluster in clusters:
            perimeter = self._calculate_perimeter(cluster)
            price += perimeter * len(cluster)
        return price

    def get_discounted_price(self) -> int:
        clusters = self._cluster_map()
        discounted_price = 0
        for cluster in clusters:
            corner_count = self._get_corner_count(cluster)
            discounted_price += corner_count * len(cluster)
            point = cluster.pop()
            print(self._map[point[0]][point[1]], corner_count)
        return discounted_price


def main():
    puzzle = Puzzle(year=2024, day=12)
    solver = AoC2024Day12(data=puzzle.input_data)
    price = solver.calculate_price()
    # discounted_price = solver.get_discounted_price()

    print(f"PART 1: Total price is {price}")
    # print(f"PART 2: Total discounted price is {discounted_price}")


if __name__ == "__main__":
    main()
