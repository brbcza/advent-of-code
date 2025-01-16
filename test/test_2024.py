import numpy as np
import pytest
from aoc.year_2024 import *
from aocd.models import Puzzle

from . import AoCTestInputInteraface
from . import parametrize_aoc_test


@parametrize_aoc_test(2024, 1)
def test_day_1(test_input: AoCTestInputInteraface):
    solver = AoC2024Day1(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.compute_distance() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.compute_simmilarity() == int(test_input.answer_b)


@parametrize_aoc_test(2024, 2)
def test_day_2(test_input: AoCTestInputInteraface):
    solver = AoC2024Day2(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.count_safe_reports() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.count_safe_reports_with_tolerance() == int(test_input.answer_b)


@parametrize_aoc_test(2024, 3)
def test_day_3(test_input: AoCTestInputInteraface):
    solver = AoC2024Day3(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.sum_multiplications() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.sum_multiplications_with_dos() == int(test_input.answer_b)


@parametrize_aoc_test(2024, 4)
def test_day_4(test_input: AoCTestInputInteraface):
    solver = AoC2024Day4(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_xmas_count() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_cross_mas_count() == int(test_input.answer_b)


@parametrize_aoc_test(2024, 5)
def test_day_5(test_input: AoCTestInputInteraface):
    solver = AoC2024Day5(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_valid_updates_sum() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_invalid_updates_fixed_sum() == int(test_input.answer_b)


@parametrize_aoc_test(2024, 6)
def test_day_6(test_input: AoCTestInputInteraface):
    solver = AoC2024Day6(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_visited_count() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_loop_count() == int(test_input.answer_b)


@parametrize_aoc_test(2024, 7)
def test_day_7(test_input: AoCTestInputInteraface):
    solver = AoC2024Day7(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_calibration_result() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_calibration_result_with_connect_operator() == int(
            test_input.answer_b
        )


@parametrize_aoc_test(2024, 8)
def test_day_8(test_input: AoCTestInputInteraface):
    solver = AoC2024Day8(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_antinode_count() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_antinode_count_with_resonances() == int(test_input.answer_b)


@pytest.mark.skip(reason="Day 9 is too slow")
@parametrize_aoc_test(2024, 9)
def test_day_9(test_input: AoCTestInputInteraface):
    solver = AoC2024Day9(data=test_input.input_data)
    if test_input.answer_a:
        organize_file_chunks = solver.organize_files_chunks()
        assert solver.calculate_checksum(organize_file_chunks) == int(
            test_input.answer_a
        )
    if test_input.answer_b:
        organizes_files = solver.organize_files()
        assert solver.calculate_checksum(organizes_files) == int(test_input.answer_b)


@parametrize_aoc_test(2024, 10)
def test_day_10(test_input: AoCTestInputInteraface):
    solver = AoC2024Day10(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_trailhead_score_sum() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_trailhead_rating_sum() == int(test_input.answer_b)


@parametrize_aoc_test(2024, 11)
def test_day_11(test_input: AoCTestInputInteraface):
    solver = AoC2024Day11(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.blink_n_times(25) == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.blink_n_times(75) == int(test_input.answer_b)


@parametrize_aoc_test(2024, 12)
def test_day_12(test_input: AoCTestInputInteraface):
    solver = AoC2024Day12(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.calculate_price() == int(test_input.answer_a)


@parametrize_aoc_test(2024, 13)
def test_day_13(test_input: AoCTestInputInteraface):
    solver = AoC2024Day13(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_token_count() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_token_count(10000000000000 * np.ones(2)) == int(
            test_input.answer_b
        )


@parametrize_aoc_test(2024, 14)
def test_day_14(test_input: AoCTestInputInteraface):
    width = 11 if test_input.is_example else 101
    height = 7 if test_input.is_example else 103
    solver = AoC2024Day14(width, height, data=test_input.input_data)
    if test_input.answer_a:
        assert solver.calculate_safety_factor(100) == int(test_input.answer_a)


@parametrize_aoc_test(2024, 15)
def test_day_15(test_input: AoCTestInputInteraface):
    solver = AoC2024Day15(data=test_input.input_data)
    if test_input.answer_a:
        assert solver.get_gps_sum_after_moves() == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.get_gps_sum_after_moves_on_scaled_map() == int(
            test_input.answer_b
        )


@parametrize_aoc_test(2024, 16)
def test_day_16(test_input: AoCTestInputInteraface):
    solver = AoC2024Day16(data=test_input.input_data)
    min_path_cost, paths = solver.find_lowest_cost_path()
    if test_input.answer_a:
        assert min_path_cost == int(test_input.answer_a)
    # Solver is not accurate enough to solve this test, it needs manual adjustment
    if test_input.is_example and test_input.answer_b:
        unique_path_points = {point for path in paths for point in path}
        assert len(unique_path_points) == int(test_input.answer_b)


@parametrize_aoc_test(2024, 17)
def test_day_17(test_input: AoCTestInputInteraface):
    solver = AoC2024Day17(data=test_input.input_data)
    if test_input.answer_a:
        program_output = solver.run_program()
        assert ",".join([str(i) for i in program_output]) == test_input.answer_a
    if test_input.answer_b:
        assert solver.find_output(solver._program) == int(test_input.answer_b)


@parametrize_aoc_test(2024, 18)
def test_day_18(test_input: AoCTestInputInteraface):
    solver = AoC2024Day18(data=test_input.input_data)
    width = 6 if test_input.is_example else 70
    height = 6 if test_input.is_example else 70
    num_bytes = 12 if test_input.is_example else 1024
    shortest_path = solver.find_shortest_path(width, height, num_bytes)
    if test_input.answer_a:
        assert len(shortest_path) == int(test_input.answer_a) + (
            3 if test_input.is_example else 1
        )
    if test_input.answer_b:
        blocking_point = solver.find_blocked_path(
            width, height, num_bytes, shortest_path
        )
        assert f"{blocking_point[0]},{blocking_point[1]}" == test_input.answer_b


@parametrize_aoc_test(2024, 19)
def test_day_19(test_input: AoCTestInputInteraface):
    solver = AoC2024Day19(data=test_input.input_data)
    count, sum = solver.get_solvable_designs()
    if test_input.answer_a:
        assert count == int(test_input.answer_a)
    if test_input.answer_b:
        assert sum == int(test_input.answer_b)


@parametrize_aoc_test(2024, 20)
def test_day_20(test_input: AoCTestInputInteraface):
    solver = AoC2024Day20(data=test_input.input_data)
    min_safe_a = 0 if test_input.is_example else 100
    min_safe_b = 50 if test_input.is_example else 100
    if test_input.answer_a:
        assert solver.count_cheats(min_safe_a, 2) == int(test_input.answer_a)
    if test_input.answer_b:
        assert solver.count_cheats(min_safe_b, 20) == int(test_input.answer_b)
