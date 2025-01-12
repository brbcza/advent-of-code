# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/15
from typing import Optional

from aocd.models import Puzzle


EMPTY = 0
WALL = 1
BOX = 2
BOX_LEFT = 3
BOX_RIGHT = 4


class AoC2024Day15:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._initial_map: list[list[int]] = []
        self._initial_position: tuple[int, int] = (0, 0)
        self._movements = ""
        self._load_input(data_path, data)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        parse_grid = True
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No input data provided")
        for i, line in enumerate(data.splitlines()):
            if line in ("", "\n"):
                parse_grid = False
                continue
            if parse_grid:
                row: list[int] = []
                for j, c in enumerate(line.strip()):
                    if c == "#":
                        row.append(WALL)
                    elif c == ".":
                        row.append(EMPTY)
                    elif c == "O":
                        row.append(BOX)
                    elif c == "@":
                        row.append(EMPTY)
                        self._initial_position = (i, j)
                self._initial_map.append(row)
            else:
                self._movements += line.strip()

    def _scale_map(self) -> list[list[int]]:
        scaled_map: list[list[int]] = []
        for row in self._initial_map:
            scaled_row: list[int] = []
            for cell in row:
                if cell == WALL:
                    scaled_row += [WALL, WALL]
                elif cell == EMPTY:
                    scaled_row += [EMPTY, EMPTY]
                elif cell == BOX:
                    scaled_row += [BOX_LEFT, BOX_RIGHT]
            scaled_map.append(scaled_row)
        return scaled_map

    def _scale_position(self) -> tuple[int, int]:
        x, y = self._initial_position
        return x, 2 * y

    def _move(
        self,
        map: list[list[int]],
        direction: str,
        position: tuple[int, int],
    ) -> tuple[int, int]:
        def move_box(position: tuple[int, int], direction: tuple[int, int]) -> bool:
            x, y = position
            dx, dy = direction
            new_x, new_y = x + dx, y + dy
            if map[new_x][new_y] == EMPTY:
                map[new_x][new_y] = BOX
                map[x][y] = EMPTY
                return True
            elif map[new_x][new_y] == WALL:
                return False
            else:
                moved = move_box((new_x, new_y), direction)
                if moved:
                    map[new_x][new_y] = BOX
                    map[x][y] = EMPTY
                return moved

        def move_large_box(
            position: tuple[int, int],
            direction: tuple[int, int],
            only_check: bool = False,
        ) -> bool:
            x, y = position
            dx, dy = direction
            new_x, new_y = x + dx, y + dy
            if direction in ((0, -1), (0, 1)):
                if map[new_x][new_y + dy] == EMPTY:
                    if only_check:
                        return True
                    map[new_x][new_y + dy], map[new_x][new_y] = (
                        map[new_x][new_y],
                        map[new_x][new_y + dy],
                    )
                    map[new_x][new_y] = map[x][y]
                    map[x][y] = EMPTY
                    return True
                elif map[new_x][new_y + dy] == WALL:
                    return False
                else:
                    moved = move_large_box((new_x, new_y + dy), direction)
                    if moved and not only_check:
                        map[new_x][new_y + dy], map[new_x][new_y] = (
                            map[new_x][new_y],
                            map[new_x][new_y + dy],
                        )
                        map[new_x][new_y] = map[x][y]
                        map[x][y] = EMPTY
                    return moved
            elif direction in ((-1, 0), (1, 0)):
                if map[x][y] == BOX_LEFT:
                    if map[new_x][new_y] == EMPTY and map[new_x][new_y + 1] == EMPTY:
                        if only_check:
                            return True
                        map[new_x][new_y] = BOX_LEFT
                        map[new_x][new_y + 1] = BOX_RIGHT
                        map[x][y] = EMPTY
                        map[x][y + 1] = EMPTY
                        return True
                    elif map[new_x][new_y] == WALL or map[new_x][new_y + 1] == WALL:
                        return False
                    else:
                        moved = True
                        if map[new_x][new_y] in (BOX_RIGHT, BOX_LEFT):
                            moved = moved and move_large_box(
                                (new_x, new_y), direction, only_check=True
                            )
                        if map[new_x][new_y + 1] == BOX_LEFT:
                            moved = moved and move_large_box(
                                (new_x, new_y + 1), direction, only_check=True
                            )
                        if moved and not only_check:
                            if map[new_x][new_y] in (BOX_RIGHT, BOX_LEFT):
                                move_large_box((new_x, new_y), direction)
                            if map[new_x][new_y + 1] == BOX_LEFT:
                                move_large_box((new_x, new_y + 1), direction)
                            map[new_x][new_y] = BOX_LEFT
                            map[new_x][new_y + 1] = BOX_RIGHT
                            map[x][y] = EMPTY
                            map[x][y + 1] = EMPTY
                        return moved
                if map[x][y] == BOX_RIGHT:
                    if map[new_x][new_y] == EMPTY and map[new_x][new_y - 1] == EMPTY:
                        if only_check:
                            return True
                        map[new_x][new_y] = BOX_RIGHT
                        map[new_x][new_y - 1] = BOX_LEFT
                        map[x][y] = EMPTY
                        map[x][y - 1] = EMPTY
                        return True
                    elif map[new_x][new_y] == WALL or map[new_x][new_y - 1] == WALL:
                        return False
                    else:
                        moved = True
                        if map[new_x][new_y] in (BOX_RIGHT, BOX_LEFT):
                            moved = moved and move_large_box(
                                (new_x, new_y), direction, only_check=True
                            )
                        if map[new_x][new_y - 1] == BOX_RIGHT:
                            moved = moved and move_large_box(
                                (new_x, new_y - 1), direction, only_check=True
                            )
                        if moved and not only_check:
                            if map[new_x][new_y] in (BOX_RIGHT, BOX_LEFT):
                                move_large_box((new_x, new_y), direction)
                            if map[new_x][new_y - 1] == BOX_RIGHT:
                                move_large_box((new_x, new_y - 1), direction)
                            map[new_x][new_y] = BOX_RIGHT
                            map[new_x][new_y - 1] = BOX_LEFT
                            map[x][y] = EMPTY
                            map[x][y - 1] = EMPTY
                        return moved

        directions = {
            "<": (0, -1),
            ">": (0, 1),
            "^": (-1, 0),
            "v": (1, 0),
        }
        dx, dy = directions[direction]
        x, y = position
        new_x, new_y = x + dx, y + dy

        if map[new_x][new_y] == WALL:
            return position
        elif map[new_x][new_y] == EMPTY:
            return (new_x, new_y)
        elif map[new_x][new_y] in (BOX_LEFT, BOX_RIGHT):
            moved = move_large_box((new_x, new_y), directions[direction])
            return (new_x, new_y) if moved else position
        else:
            moved = move_box((new_x, new_y), directions[direction])
            return (new_x, new_y) if moved else position

    def _get_gps_sum(self, map: list[list[int]]) -> int:
        gps_sum = 0
        for i, row in enumerate(map):
            for j, cell in enumerate(row):
                if cell in (BOX, BOX_LEFT):
                    gps_sum += 100 * i + j
        return gps_sum

    def get_gps_sum_after_moves(self) -> int:
        map = [r[:] for r in self._initial_map]
        position = self._initial_position
        for move in self._movements:
            position = self._move(map, move, position)
        return self._get_gps_sum(map)

    def get_gps_sum_after_moves_on_scaled_map(self) -> int:
        map = self._scale_map()
        position = self._scale_position()
        for move in self._movements:
            position = self._move(map, move, position)
        return self._get_gps_sum(map)


def main():
    puzzle = Puzzle(year=2024, day=15)
    solver = AoC2024Day15(data=puzzle.input_data)
    gps_sum_after_moves = solver.get_gps_sum_after_moves()
    gps_sum_after_moves_on_scaled_map = solver.get_gps_sum_after_moves_on_scaled_map()

    print(f"PART 1: GPS sum after moves is {gps_sum_after_moves}")
    print(
        f"PART 2: GPS sum after moves on scaled map is {gps_sum_after_moves_on_scaled_map}"
    )


if __name__ == "__main__":
    main()
