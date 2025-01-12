# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/5
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day5:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self.rules, self.updates = self._load_input(data_path, data)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        rules: dict[int, set[int]] = {}
        updates: list[list[int]] = []
        parse_rules = True
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for line in data.splitlines():
            if line in ("", "\n"):
                parse_rules = False
            elif parse_rules:
                n1, n2 = (int(i) for i in line.strip().split(sep="|"))
                rules_data = rules.get(n1, set())
                rules_data.add(n2)
                rules[n1] = rules_data
            else:
                updates.append([int(x) for x in line.strip().split(sep=",")])
        return rules, updates

    def _is_valid_update(self, update: list[int]):
        for u, n in enumerate(update[::-1]):
            rules = self.rules.get(n, set())
            prev_data = set(update[: len(update) - u])
            if rules.intersection(prev_data):
                return False
        return True

    def _fix_update(self, update: list[int]):
        def select_valid_number(sub_update: list[int]):
            for i in sub_update:
                rules = self.rules.get(i, set())
                prev_data = list(filter(lambda x: x != i, sub_update.copy()))
                if rules.intersection(set(prev_data)):
                    continue
                return i
            return None

        update_len = len(update)
        fixed_update = []
        while len(fixed_update) < update_len:
            fixed_number = select_valid_number(update)
            fixed_update.insert(0, fixed_number)
            update.remove(fixed_number)
        return fixed_update

    def get_valid_updates_sum(self):
        count = 0
        for update in self.updates:
            if self._is_valid_update(update):
                count += update[len(update) // 2]
        return count

    def get_invalid_updates_fixed_sum(self):
        count = 0
        for update in self.updates:
            if not self._is_valid_update(update):
                fixed_update = self._fix_update(update)
                count += fixed_update[len(fixed_update) // 2]
        return count


def main():
    puzzle = Puzzle(year=2024, day=5)
    solver = AoC2024Day5(data=puzzle.input_data)
    valid_updates_count = solver.get_valid_updates_sum()
    invalid_updates_fixed_sum = solver.get_invalid_updates_fixed_sum()

    print(f"PART 1: Valid updates sum is {valid_updates_count}")
    print(f"PART 2: Invalid updates fixed sum is {invalid_updates_fixed_sum}")


if __name__ == "__main__":
    main()
