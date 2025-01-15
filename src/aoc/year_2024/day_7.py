# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/7
from typing import Optional

from aocd.models import Puzzle


def connect_operator(a: int, b: int) -> int:
    return a * (10 ** len(str(b))) + b


class AoC2024Day7:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._equations = self._load_input(data_path, data)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        equations: list[tuple[int, list[int]]] = []
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for line in data.splitlines():
            solution, members = line.split(":")
            members = members.strip().split(" ")
            solution = int(solution)
            members = [int(m) for m in members]
            equations.append((solution, members))
        return equations

    def _solve_equation(self, equation: tuple[int, list[int]]):
        def solve(solution: int, members: list[int]):
            if len(members) == 1:
                if members[0] == solution:
                    return True
                else:
                    return False
            elif len(members) > 1:
                return solve(
                    solution, [members[0] + members[1]] + members[2:]
                ) or solve(solution, [members[0] * members[1]] + members[2:])
            return False

        solution, members = equation
        return solve(solution, members)

    def _solve_equation_with_connect_operator(self, equation: tuple[int, list[int]]):
        def solve(solution: int, members: list[int]):
            if len(members) == 1:
                if members[0] == solution:
                    return True
                else:
                    return False
            elif len(members) > 1:
                return (
                    solve(solution, [members[0] + members[1]] + members[2:])
                    or solve(solution, [members[0] * members[1]] + members[2:])
                    or solve(
                        solution,
                        [connect_operator(members[0], members[1])] + members[2:],
                    )
                )
            return False

        solution, members = equation
        return solve(solution, members)

    def get_calibration_result(self):
        sum = 0
        for equation in self._equations:
            if self._solve_equation(equation):
                sum += equation[0]
        return sum

    def get_calibration_result_with_connect_operator(self):
        sum = 0
        for equation in self._equations:
            solution = self._solve_equation_with_connect_operator(equation)
            if solution:
                sum += equation[0]
        return sum


def main():
    puzzle = Puzzle(year=2024, day=7)
    solver = AoC2024Day7(data=puzzle.input_data)
    calibration_result = solver.get_calibration_result()
    calibration_result_with_connect_operator = (
        solver.get_calibration_result_with_connect_operator()
    )

    print(f"PART 1: Calibration result is {calibration_result}")
    print(
        f"PART 2: Calibration result with connect operator is {calibration_result_with_connect_operator}"
    )


if __name__ == "__main__":
    main()
