from aoc.year_2025 import *

from . import AoCTestInputInteraface
from . import parametrize_aoc_test


@parametrize_aoc_test(2025, 1)
def test_day_1(test_input: AoCTestInputInteraface):
    solver = AoC2025Day1(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_door_password() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_door_password_method_0x434C49434B() == int(
            test_input.answer_b
        )


@parametrize_aoc_test(2025, 2)
def test_day_2(test_input: AoCTestInputInteraface):
    solver = AoC2025Day2(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_invalid_id_sum() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_invalid_id_sum_advanced() == int(test_input.answer_b)


@parametrize_aoc_test(2025, 3)
def test_day_3(test_input: AoCTestInputInteraface):
    solver = AoC2025Day3(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_largest_joltage_sum(number_len=2) == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_largest_joltage_sum(number_len=12) == int(test_input.answer_b)


@parametrize_aoc_test(2025, 4)
def test_day_4(test_input: AoCTestInputInteraface):
    solver = AoC2025Day4(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.can_be_accessed_by_forklift() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.can_be_accessed_by_forklift_recursive() == int(
            test_input.answer_b
        )
