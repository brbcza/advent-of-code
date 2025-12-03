# (c) 2025 Filip Tefr
# https://adventofcode.com/2025/day/2
from functools import lru_cache
from typing import Callable

from aocd.models import Puzzle


@lru_cache(maxsize=None)
def _divisors(n: int):
    result = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            other = n // i
            if other != i and other != n:
                result.append(other)
    return tuple(sorted(result))


def _str_groups(s: str, n: int):
    return [s[i : i + n] for i in range(0, len(s), n)]


def _all_equal(lst):
    first = lst[0]
    for x in lst:
        if x != first:
            return False
    return True


class AoC2025Day2:
    def __init__(self, data: str):
        self._data = [
            (int(a), int(b)) for x in data.strip().split(",") for a, b in [x.split("-")]
        ]

    def _get_invalid_ids(self, start: int, stop: int):
        invalid_ids: list[int] = []
        for id in range(start, stop + 1):
            str_id = str(id)
            str_len = len(str_id)
            if len(str_id) % 2 != 0:
                continue
            if str_id[: str_len // 2] == str_id[str_len // 2 :]:
                invalid_ids.append(id)
        return invalid_ids

    def _get_invalid_ids_advanced(self, start, stop):
        invalid_ids: list[int] = []
        for id in range(start, stop + 1):
            str_id = str(id)
            if len(str_id) == 1:
                continue
            for grp_len in _divisors(len(str_id)):
                if _all_equal(_str_groups(str_id, grp_len)):
                    invalid_ids.append(id)
                    break
        return invalid_ids

    def _get_invalid_id_sum_impl(self, func: Callable[[int, int], set[int]]):
        invalid_id_sum = 0
        for start, stop in self._data:
            invalid_ids = func(start, stop)
            invalid_id_sum += sum(invalid_ids)
        return invalid_id_sum

    def get_invalid_id_sum(self):
        return self._get_invalid_id_sum_impl(self._get_invalid_ids)

    def get_invalid_id_sum_advanced(self):
        return self._get_invalid_id_sum_impl(self._get_invalid_ids_advanced)


def main():
    puzzle = Puzzle(year=2025, day=2)
    solver = AoC2025Day2(data=puzzle.input_data)

    invalid_id_sum = solver.get_invalid_id_sum()
    invalid_id_sum_advanced = solver.get_invalid_id_sum_advanced()

    print(f"Sum of invalid IDs is: {invalid_id_sum}")
    print(f"Sum of advanced invalid IDs is: {invalid_id_sum_advanced}")


if __name__ == "__main__":
    main()
