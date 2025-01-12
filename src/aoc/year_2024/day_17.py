# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/17
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day17:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._A = 0
        self._B = 0
        self._C = 0
        self._pc = 0
        self._program: list[str] = []
        self._output: list[int] = []
        self._load_data(data_path, data)

    def _load_data(self, data_path: Optional[str] = None, data: Optional[str] = None):
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        lines = data.splitlines()
        self._A = int(lines[0].strip().split(": ")[1])
        self._B = int(lines[1].strip().split(": ")[1])
        self._C = int(lines[2].strip().split(": ")[1])
        self._program = [int(c) for c in lines[4].strip().split(": ")[1].split(",")]

    def _get_combo_operand(self, operand: int):
        if operand <= 3:
            return operand
        elif operand == 4:
            return self._A
        elif operand == 5:
            return self._B
        elif operand == 6:
            return self._C
        else:
            raise ValueError(f"Invalid operand {operand}")

    def _adv(self, operand: int):
        numerator = self._A
        denominator = 2 ** self._get_combo_operand(operand)
        self._A = numerator // denominator
        self._pc += 2

    def _bxl(self, operand: int):
        self._B = self._B ^ operand
        self._pc += 2

    def _bst(self, operand: int):
        self._B = self._get_combo_operand(operand) % 8
        self._pc += 2

    def _jnz(self, operand: int):
        if self._A == 0:
            self._pc += 2
            return
        self._pc = operand

    def _bxc(self, operand: int):
        self._B = self._B ^ self._C
        self._pc += 2

    def _out(self, operand: int):
        self._output.append(self._get_combo_operand(operand) % 8)
        self._pc += 2

    def bdv(self, operand: int):
        numerator = self._A
        denominator = 2 ** self._get_combo_operand(operand)
        self._B = numerator // denominator
        self._pc += 2

    def _cdv(self, operand: int):
        numerator = self._A
        denominator = 2 ** self._get_combo_operand(operand)
        self._C = numerator // denominator
        self._pc += 2

    def run_program(self):
        self._pc = 0
        while self._pc < len(self._program):
            opcode = self._program[self._pc]
            operand = self._program[self._pc + 1]
            if opcode == 0:
                self._adv(operand)
            elif opcode == 1:
                self._bxl(operand)
            elif opcode == 2:
                self._bst(operand)
            elif opcode == 3:
                self._jnz(operand)
            elif opcode == 4:
                self._bxc(operand)
            elif opcode == 5:
                self._out(operand)
            elif opcode == 6:
                self.bdv(operand)
            elif opcode == 7:
                self._cdv(operand)
            else:
                raise ValueError(f"Invalid opcode {opcode}")
        return self._output

    def _compare_lists(self, list1: list[int], list2: list[int]):
        if len(list1) != len(list2):
            return False
        for x, y in zip(list1, list2):
            if x != y:
                return False
        return True

    def find_output(self, desired_output: list[int]):
        start_iter = 8 ** (len(desired_output) - 1)
        n = len(desired_output) - 2
        reg_a_value = start_iter
        while True:
            self._A = reg_a_value
            self._B = 0
            self._C = 0
            self._output = []
            self._pc = 0
            self.run_program()
            if self._compare_lists(self._output, desired_output):
                return reg_a_value
            elif self._compare_lists(self._output[n + 1 :], desired_output[n + 1 :]):
                n = max(n - 1, 0)
            reg_a_value += 8**n


def main():
    puzzle = Puzzle(year=2024, day=17)
    solver = AoC2024Day16(data=puzzle.input_data)
    program_output = solver.run_program()
    i = solver.find_output(solver._program)

    print(f'PART 1: Program output is - {",".join([str(i) for i in program_output])}')
    print(f"PART 2: Value of A is - {i}")


if __name__ == "__main__":
    main()
