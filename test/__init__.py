from dataclasses import dataclass
from functools import wraps
from typing import Callable

import pytest
from aocd.models import Example
from aocd.models import Puzzle


@dataclass
class AoCTestInputInteraface:
    input_data: str
    answer_a: str
    answer_b: str
    is_example: bool

    @classmethod
    def from_puzzle(cls, puzzle: Puzzle | Example):
        try:
            answer_a = puzzle.answer_a
        except AttributeError:
            answer_a = None
        try:
            answer_b = puzzle.answer_b
        except AttributeError:
            answer_b = None
        return cls(
            input_data=puzzle.input_data,
            answer_a=answer_a,
            answer_b=answer_b,
            is_example=isinstance(puzzle, Example),
        )


def _get_aoc_test_inputs(year: int, day: int):
    puzzle = Puzzle(year=year, day=day)
    return (
        *(AoCTestInputInteraface.from_puzzle(example) for example in puzzle.examples),
        AoCTestInputInteraface.from_puzzle(puzzle),
    )


def parametrize_aoc_test(year: int, day: int):
    inputs = _get_aoc_test_inputs(year, day)

    def decorator(func: Callable):
        @wraps(func)
        @pytest.mark.parametrize("test_input", inputs)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper

    return decorator


__all__ = [
    "parametrize_aoc_test",
    "AoCTestInputInteraface",
]
