# (c) 2024 Filip Tefr
# https://adventofcode.com/2024/day/2
from typing import Optional

import numpy as np
from aocd.models import Puzzle


class AoC2024Day2:
    def __init__(self, data_path: Optional[str] = None, data: Optional[str] = None):
        self._reports = self._load_input(data_path, data)

    def _load_input(
        self, data_path: Optional[str] = None, data: Optional[str] = None
    ) -> list[np.array]:
        reports = []
        if data_path:
            with open(data_path, "r") as f:
                data = f.read()
        elif not data:
            raise ValueError("No data provided")
        for line in data.splitlines():
            reports.append(np.fromstring(line.strip(), dtype=int, sep=" "))
        return reports

    def _is_report_safe(self, report: np.array) -> bool:
        sorted_report = np.sort(report)
        if np.any(report != sorted_report) and np.any(report != sorted_report[::-1]):
            return False
        for i in range(len(report) - 1):
            difference = abs(report[i] - report[i + 1])
            if difference < 1 or difference > 3:
                return False
        return True

    def count_safe_reports(self) -> int:
        safe_count = 0
        for report in self._reports:
            if self._is_report_safe(report):
                safe_count += 1
        return safe_count

    def count_safe_reports_with_tolerance(self) -> int:
        safe_count = 0
        for report in self._reports:
            if self._is_report_safe(report):
                safe_count += 1
            else:
                for i in range(len(report)):
                    if self._is_report_safe(np.delete(report, i)):
                        safe_count += 1
                        break
        return safe_count


def main():
    puzzle = Puzzle(year=2024, day=2)
    solver = AoC2024Day2(data=puzzle.input_data)
    safe_reports_count = solver.count_safe_reports()
    safe_reports_count_with_tolerance_count = solver.count_safe_reports_with_tolerance()

    print(f"PART 1: Number of safe reports is {safe_reports_count}")
    print(
        f"PART 2: Number of safe reports with tolerance is {safe_reports_count_with_tolerance_count}"
    )


if __name__ == "__main__":
    main()
