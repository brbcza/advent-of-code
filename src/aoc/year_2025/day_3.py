# (c) 2025 Filip Tefr
# https://adventofcode.com/2025/day/3
from aocd.models import Puzzle


class AoC2025Day3:
    def __init__(self, data: str):
        self._data = [x.strip() for x in data.splitlines()]

    def _get_largest_joltage(self, row: str, number_len: int = 2):
        number: list[str] = []
        for n, c in enumerate(row):
            if (
                len(number) == 0
                or (len(number) < number_len and number[-1] >= c)
                or len(row) - n + len(number) <= number_len
            ):
                number.append(c)
            elif c > number[-1]:
                while (
                    len(number) > 0
                    and c > number[-1]
                    and len(row) - n + len(number) > number_len
                ):
                    number.pop()
                number.append(c)
        assert len(number) == number_len
        return int("".join(number))

    def get_largest_joltage_sum(self, number_len: int = 2):
        joltage_sum = 0
        for row in self._data:
            joltage_sum += self._get_largest_joltage(row, number_len)
        return joltage_sum


def main():
    puzzle = Puzzle(year=2025, day=3)
    solver = AoC2025Day3(data=puzzle.input_data)

    output_joltage = solver.get_largest_joltage_sum(number_len=2)
    output_joltage_larger = solver.get_largest_joltage_sum(number_len=12)

    print(f"Total output joltage is: {output_joltage}")
    print(f"Total output larger joltage is: {output_joltage_larger}")


if __name__ == "__main__":
    main()
