# (c) 2025 Filip Tefr
# https://adventofcode.com/2025/day/1
from aocd.models import Puzzle


class AoC2025Day1:
    START_POS = 50
    MAX_POS = 99 + 1

    def __init__(self, data: str):
        self._moves = [
            (-1 if m.strip()[0] == "L" else 1, int(m.strip()[1:]))
            for m in data.splitlines()
        ]

    def get_door_password(self):
        password = 0
        position = self.START_POS
        for dir, steps in self._moves:
            position = (position + dir * steps) % self.MAX_POS
            password += position == 0
        return password

    def get_door_password_method_0x434C49434B(self):
        zero_crosses = 0
        position = self.START_POS
        for dir, steps in self._moves:
            div, rem = divmod(position + dir * steps, self.MAX_POS)
            zero_crosses += (
                abs(div)
                # Prev result is zero -> -1
                - (position == 0 and dir < 0)
                # New result is zero -> +1
                + (rem == 0 and dir < 0)
            )
            position = rem
        return zero_crosses


def main():
    puzzle = Puzzle(year=2025, day=1)
    solver = AoC2025Day1(data=puzzle.examples[0].input_data)

    password = solver.get_door_password()
    password_2 = solver.get_door_password_method_0x434C49434B()

    print(f"Door password is: {password}")
    print(f"Door password with method 0x434C49434B is : {password_2}")


if __name__ == "__main__":
    main()
