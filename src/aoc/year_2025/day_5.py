# (c) 2025 Filip Tefr
# https://adventofcode.com/2025/day/3
from aocd.models import Puzzle


class AoC2025Day5:
    def __init__(self, data: str):
        self._ranges: list[tuple[int, int]] = []
        self._ids: list[int] = []
        reading_ids = False
        for line in data.splitlines():
            if reading_ids:
                self._ids.append(int(line.strip()))
            elif line.strip() == "":
                reading_ids = True
            else:
                start, stop = line.split("-")
                self._ranges.append((int(start), int(stop)))
        self._reduce_ranges()

    def _reduce_ranges(self):
        self._ranges.sort(key=lambda x: x[0])
        i = 0
        while True:
            if i == len(self._ranges) - 1:
                break
            r1 = self._ranges[i]
            r2 = self._ranges[i + 1]
            if r1[1] >= r2[0]:
                self._ranges.pop(i)
                self._ranges.pop(i)
                self._ranges.insert(i, (r1[0], max(r1[1], r2[1])))
            else:
                i += 1

    def get_fresh_ingredients_cnt(self):
        fresh_ids: set[int] = set()
        for start, end in self._ranges:
            for id in self._ids:
                if id in fresh_ids:
                    continue
                if id >= start and id <= end:
                    fresh_ids.add(id)
        return len(fresh_ids)

    def get_all_fresh_ingredients_cnt(self):
        cnt = 0
        for start, end in self._ranges:
            cnt += end - start + 1
        return cnt


def main():
    puzzle = Puzzle(year=2025, day=5)
    solver = AoC2025Day5(data=puzzle.input_data)

    fresh_ingredients_cnt = solver.get_fresh_ingredients_cnt()
    all_fresh_ingredients_cnt = solver.get_all_fresh_ingredients_cnt()

    print(f"Number of fresh ingredients is: {fresh_ingredients_cnt}")
    print(f"Total number of fresh ingredients is: {all_fresh_ingredients_cnt}")


if __name__ == "__main__":
    main()
