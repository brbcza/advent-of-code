# (c) 2025 Filip Tefr
# https://adventofcode.com/2025/day/3
import operator
from functools import reduce

from aocd.models import Puzzle


class AoC2025Day6:
    def __init__(self, data: str):
        lines = data.splitlines()
        self._operation_index = len(lines) - 1
        self._numbers: list[tuple[int, int, int]] = []
        self._operations = lines[-1].split()

        last_start_pos = 0
        for i in range(len(lines[0])):
            if all(row[i] == " " for row in lines[:-1]):
                self._numbers.append(
                    tuple(x[last_start_pos:i] for x in lines[: self._operation_index])
                )
                last_start_pos = i + 1
        self._numbers.append(tuple(x[last_start_pos:] for x in lines[:-1]))

    def get_problem_sum(self):
        cnt = 0
        for i, op in enumerate(self._operations):
            if op == "+":
                cnt += reduce(operator.add, (int(x) for x in self._numbers[i]))
            elif op == "*":
                cnt += reduce(operator.mul, (int(x) for x in self._numbers[i]))
            else:
                assert False
        return cnt

    def get_advanced_problem_sum(self):
        cnt = 0
        for i, op in enumerate(self._operations):
            operands = [
                "".join([self._numbers[i][k][j] for k in range(self._operation_index)])
                for j in range(len(self._numbers[i][0]))
            ]
            if op == "+":
                cnt += reduce(operator.add, (int(x) for x in operands))
            elif op == "*":
                cnt += reduce(operator.mul, (int(x) for x in operands))
            else:
                assert False
        return cnt


def main():
    puzzle = Puzzle(year=2025, day=6)
    solver = AoC2025Day6(data=puzzle.input_data)

    sum_of_solutions = solver.get_problem_sum()
    sum_of_advanced_solutions = solver.get_advanced_problem_sum()

    print(f"Sum of problem's solutions is: {sum_of_solutions}")
    print(f"Sum of advanced problem's solutions is: {sum_of_advanced_solutions}")


if __name__ == "__main__":
    main()
