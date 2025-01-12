# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/3
import re
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day3:
    data: str

    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                self.data = f.read()
        elif data:
            self.data = data
        else:
            raise ValueError("No data provided")

    def sum_multiplications(self):
        MUL_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"
        sum = 0
        for match in re.finditer(MUL_REGEX, self.data):
            sum += int(match.group(1)) * int(match.group(2))
        return sum

    def sum_multiplications_with_dos(self):
        MUL_REGEX_WITH_DOS = r"((mul)\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))"
        sum = 0
        do = True
        for match in re.finditer(MUL_REGEX_WITH_DOS, self.data):
            if match.group(0) == "do()":
                do = True
            elif match.group(0) == "don't()":
                do = False
            elif do and match.group(2) == "mul":
                sum += int(match.group(3)) * int(match.group(4))
        return sum


def main():
    uzzle = Puzzle(year=2024, day=3)
    solver = AoC2024Day3(data=puzzle.input_data)
    sum = solver.sum_multiplications()
    sum_with_dos = solver.sum_multiplications_with_dos()

    print(f"PART 1: Sum of multiplications is {sum}")
    print(f"PART 2: Sum of multiplications with 'do()' is {sum_with_dos}")


if __name__ == "__main__":
    main()
