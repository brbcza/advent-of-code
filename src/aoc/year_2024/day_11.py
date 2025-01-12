# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/11
from functools import cache
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day11:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._stones: dict[int, int] = {}
        self._load_data(data_path, data)

    def _load_data(
        self, data_path: Optional[str] = None, data: Optional[str] = None
    ) -> list[int]:
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for stone in data.strip().split(" "):
            stone_n = int(stone)
            count = self._stones.get(stone_n, 0)
            self._stones[stone_n] = count + 1

    @cache
    def _iterate(self, stone: int) -> list[int]:
        num_digits = len(str(stone))
        if stone == 0:
            return [1]
        elif num_digits % 2 == 0:
            return [
                int(str(stone)[: num_digits // 2]),
                int(str(stone)[num_digits // 2 :]),
            ]
        else:
            return [stone * 2024]

    def _blink_once(self, stones: dict[int, int]):
        updated_stones: dict[int, int] = {}
        for stone, count in stones.items():
            for update in self._iterate(stone):
                updated_stones[update] = updated_stones.get(update, 0) + count
        return updated_stones

    def blink_n_times(self, n: int) -> list[int]:
        stones = self._stones
        for i in range(n):
            stones = self._blink_once(stones)
        return sum(stones.values())


def main():
    puzzle = Puzzle(year=2024, day=11)
    solver = AoC2024Day11(data=puzzle.input_data)
    n_stones_after_25_blinks = solver.blink_n_times(25)
    n_stones_after_75_blinks = solver.blink_n_times(75)

    print(f"PART 1: Number of stones after 25 blinks is {n_stones_after_25_blinks}")
    print(f"PART 2: Number of stones after 75 blinks is {n_stones_after_75_blinks}")


if __name__ == "__main__":
    main()
