import importlib
from argparse import ArgumentParser
from argparse import BooleanOptionalAction
from typing import Optional


def run_day(year: int, day: int):
    print(f"Running day {day} of year {year}")
    try:
        solver = importlib.import_module(f"aoc.year_{year}.day_{day}")
    except ImportError:
        print(f"[ERROR] Day {day} of year {year} has not been implemented")
        return
    return solver.main()


def submit_answer(
    year: int, day: int, answer: Optional[tuple[Optional[str], Optional[str]]]
):
    print(f"Submitting answer for day {day} of year {year}")
    print(f"Done")


def main():
    parser = ArgumentParser(
        prog="aoc_runner",
        description="Run puzzle solutions from Advent of Code",
    )
    parser.add_argument(
        "year", type=int, help="The year of the Advent of Code challenge"
    )
    parser.add_argument("day", type=int, help="The day of the Advent of Code challenge")
    parser.add_argument(
        "--submit",
        action=BooleanOptionalAction,
        default=False,
        help="Submit the solution to the Advent of Code website",
    )
    args = parser.parse_args()

    answer = run_day(args.year, args.day)
    if args.submit:
        submit_answer(args.year, args.day, answer)


if __name__ == "__main__":
    main()
