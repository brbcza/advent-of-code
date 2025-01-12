# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/9
from typing import Optional

from aocd.models import Puzzle


class AoC2024Day9:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._disk_map: list[Optional[int]] = []
        self._file_sizes: dict[int, int] = {}
        self._load_input(data_path, data)

    def _load_input(self, data_path: Optional[str] = None, data: Optional[str] = None):
        file_id = 0
        file = True
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for c in data:
            if file:
                self._disk_map += [file_id] * int(c)
                self._file_sizes[file_id] = int(c)
                file_id += 1
            else:
                self._disk_map += [None] * int(c)
            file = not file

    def _find_free_space(
        self,
        disk_map: list[Optional[int]],
        start: int,
        size: int,
        stop: Optional[int] = None,
    ) -> int:
        for i in range(start, len(self._disk_map)):
            if stop is not None and i >= stop:
                return -1
            if i + size > len(self._disk_map):
                return -1
            if all([disk_map[i + j] is None for j in range(size)]):
                return i
        return -1

    def organize_files_chunks(self):
        orginized_disk_map = self._disk_map.copy()
        last_swap_index = 0
        for i, id in reversed(list(enumerate(self._disk_map))):
            if id is None:
                continue
            last_swap_index = self._find_free_space(
                orginized_disk_map, last_swap_index, 1
            )
            if last_swap_index == -1 or last_swap_index >= i:
                break
            orginized_disk_map[last_swap_index], orginized_disk_map[i] = (
                orginized_disk_map[i],
                orginized_disk_map[last_swap_index],
            )
        return orginized_disk_map

    def organize_files(self):
        orginized_disk_map = self._disk_map.copy()
        actual_file_id = -1
        for i, id in reversed(list(enumerate(self._disk_map))):
            if id == 0:
                break
            if id is None or id == actual_file_id:
                continue
            free_space = self._find_free_space(
                orginized_disk_map, 0, self._file_sizes[id], i
            )
            if free_space == -1 or free_space >= i:
                continue
            for j in range(self._file_sizes[id]):
                orginized_disk_map[free_space + j], orginized_disk_map[i - j] = (
                    orginized_disk_map[i - j],
                    orginized_disk_map[free_space + j],
                )
            actual_file_id = id
        return orginized_disk_map

    def calculate_checksum(self, disk_map: list[Optional[int]]) -> int:
        checksum = 0
        for i, id in enumerate(disk_map):
            if id is None:
                continue
            checksum += i * id
        return checksum


def main():
    puzzle = Puzzle(year=2024, day=9)
    solver = AoC2024Day9(data=puzzle.input_data)
    orginized_chunks = solver.organize_files_chunks()
    orginized_chunks_checksum = solver.calculate_checksum(orginized_chunks)
    orginized_files = solver.organize_files()
    orginized_files_checksum = solver.calculate_checksum(orginized_files)

    print(f"PART 1: Checksum of the organized chunks is {orginized_chunks_checksum}")
    print(f"PART 2: Checksum of the organized files is {orginized_files_checksum}")


if __name__ == "__main__":
    main()
