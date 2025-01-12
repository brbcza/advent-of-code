import os

import numpy as np
from aoc.year_2024 import *
from aocd.models import Puzzle


def test_day_1():
    puzzle = Puzzle(year=2024, day=1)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day1(data=example.input_data)
        if example.answer_a:
            assert solver.compute_distance() == int(example.answer_a)
        if example.answer_b:
            assert solver.compute_simmilarity() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day1(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.compute_distance() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.compute_simmilarity() == int(puzzle.answer_b)


def test_day_2():
    puzzle = Puzzle(year=2024, day=2)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day2(data=example.input_data)
        if example.answer_a:
            assert solver.count_safe_reports() == int(example.answer_a)
        if example.answer_b:
            assert solver.count_safe_reports_with_tolerance() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day2(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.count_safe_reports() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.count_safe_reports_with_tolerance() == int(puzzle.answer_b)


def test_day_3():
    puzzle = Puzzle(year=2024, day=3)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day3(data=example.input_data)
        if example.answer_a:
            assert solver.sum_multiplications() == int(example.answer_a)
        if example.answer_b:
            assert solver.sum_multiplications_with_dos() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day3(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.sum_multiplications() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.sum_multiplications_with_dos() == int(puzzle.answer_b)


def test_day_4():
    puzzle = Puzzle(year=2024, day=4)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day4(data=example.input_data)
        if example.answer_a:
            assert solver.get_xmas_count() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_cross_mas_count() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day4(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_xmas_count() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_cross_mas_count() == int(puzzle.answer_b)


def test_day_5():
    puzzle = Puzzle(year=2024, day=5)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day5(data=example.input_data)
        if example.answer_a:
            assert solver.get_valid_updates_sum() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_invalid_updates_fixed_sum() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day5(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_valid_updates_sum() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_invalid_updates_fixed_sum() == int(puzzle.answer_b)


def test_day_6():
    puzzle = Puzzle(year=2024, day=6)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day6(data=example.input_data)
        if example.answer_a:
            assert solver.get_visited_count() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_loop_count() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day6(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_visited_count() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_loop_count() == int(puzzle.answer_b)


def test_day_7():
    puzzle = Puzzle(year=2024, day=7)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day7(data=example.input_data)
        if example.answer_a:
            assert solver.get_calibration_result() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_calibration_result_with_connect_operator() == int(
                example.answer_b
            )

    # Test real data
    solver = AoC2024Day7(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_calibration_result() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_calibration_result_with_connect_operator() == int(
            puzzle.answer_b
        )


def test_day_8():
    puzzle = Puzzle(year=2024, day=8)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day8(data=example.input_data)
        if example.answer_a:
            assert solver.get_antinode_count() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_antinode_count_with_resonances() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day8(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_antinode_count() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_antinode_count_with_resonances() == int(puzzle.answer_b)


def test_day_9():
    puzzle = Puzzle(year=2024, day=9)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day9(data=example.input_data)
        if example.answer_a:
            organize_file_chunks = solver.organize_files_chunks()
            assert solver.calculate_checksum(organize_file_chunks) == int(
                example.answer_a
            )
        if example.answer_b:
            organizes_files = solver.organize_files()
            assert solver.calculate_checksum(organizes_files) == int(example.answer_b)

    # Test real data
    solver = AoC2024Day9(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        organize_file_chunks = solver.organize_files_chunks()
        assert solver.calculate_checksum(organize_file_chunks) == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        organizes_files = solver.organize_files()
        assert solver.calculate_checksum(organizes_files) == int(puzzle.answer_b)


def test_day_10():
    puzzle = Puzzle(year=2024, day=10)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day10(data=example.input_data)
        if example.answer_a:
            assert solver.get_trailhead_score_sum() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_trailhead_rating_sum() == int(example.answer_b)

    # Test real data
    solver = AoC2024Day10(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_trailhead_score_sum() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_trailhead_rating_sum() == int(puzzle.answer_b)


def test_day_11():
    puzzle = Puzzle(year=2024, day=11)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day11(data=example.input_data)
        if example.answer_a:
            assert solver.blink_n_times(25) == int(example.answer_a)
        if example.answer_b:
            assert solver.blink_n_times(75) == int(example.answer_b)

    # Test real data
    solver = AoC2024Day11(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.blink_n_times(25) == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.blink_n_times(75) == int(puzzle.answer_b)


def test_day_12():
    puzzle = Puzzle(year=2024, day=12)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day12(data=example.input_data)
        if example.answer_a:
            assert solver.calculate_price() == int(example.answer_a)

    # Test real data
    solver = AoC2024Day12(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.calculate_price() == int(puzzle.answer_a)


def test_day_13():
    puzzle = Puzzle(year=2024, day=13)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day13(data=example.input_data)
        if example.answer_a:
            assert solver.get_token_count() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_token_count(10000000000000 * np.ones(2)) == int(
                example.answer_b
            )

    # Test real data
    solver = AoC2024Day13(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_token_count() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_token_count(10000000000000 * np.ones(2)) == int(
            puzzle.answer_b
        )


def test_day_14():
    puzzle = Puzzle(year=2024, day=14)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day14(11, 7, data=example.input_data)
        if example.answer_a:
            assert solver.calculate_safety_factor(100) == int(example.answer_a)

    # Test real data
    solver = AoC2024Day14(101, 103, data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.calculate_safety_factor(100) == int(puzzle.answer_a)


def test_day_15():
    puzzle = Puzzle(year=2024, day=15)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day15(data=example.input_data)
        if example.answer_a:
            assert solver.get_gps_sum_after_moves() == int(example.answer_a)
        if example.answer_b:
            assert solver.get_gps_sum_after_moves_on_scaled_map() == int(
                example.answer_b
            )

    # Test real data
    solver = AoC2024Day15(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.get_gps_sum_after_moves() == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.get_gps_sum_after_moves_on_scaled_map() == int(puzzle.answer_b)


def test_day_16():
    puzzle = Puzzle(year=2024, day=16)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day16(data=example.input_data)
        min_path_cost, paths = solver.find_lowest_cost_path()
        if example.answer_a:
            assert min_path_cost == int(example.answer_a)
        if example.answer_b:
            unique_path_points = {point for path in paths for point in path}
            assert len(unique_path_points) == int(example.answer_b)

    # Test real data
    solver = AoC2024Day16(data=puzzle.input_data)
    min_path_cost, paths = solver.find_lowest_cost_path()
    if puzzle.answered_a and puzzle.answer_a:
        assert min_path_cost == int(puzzle.answer_a)


def test_day_17():
    puzzle = Puzzle(year=2024, day=17)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day17(data=example.input_data)
        if example.answer_a:
            program_output = solver.run_program()
            assert ",".join([str(i) for i in program_output]) == example.answer_a
        if example.answer_b:
            assert solver.find_output(solver._program) == int(example.answer_b)

    # Test real data
    solver = AoC2024Day17(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        program_output = solver.run_program()
        assert ",".join([str(i) for i in program_output]) == puzzle.answer_a
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.find_output(solver._program) == int(puzzle.answer_b)


def test_day_18():
    puzzle = Puzzle(year=2024, day=18)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day18(data=example.input_data)
        shortest_path = solver.find_shortest_path(6, 6, 12)
        if example.answer_a:
            assert len(shortest_path) == int(example.answer_a) + 3
        if example.answer_b:
            blocking_point = solver.find_blocked_path(6, 6, 12, shortest_path)
            assert f"{blocking_point[0]},{blocking_point[1]}" == example.answer_b

    # Test real data
    solver = AoC2024Day18(data=puzzle.input_data)
    shortest_path = solver.find_shortest_path(70, 70, 1024)
    if puzzle.answered_a and puzzle.answer_a:
        assert len(shortest_path) == int(puzzle.answer_a) + 1
    if puzzle.answered_a and puzzle.answer_b:
        blocking_point = solver.find_blocked_path(70, 70, 1024, shortest_path)
        assert f"{blocking_point[0]},{blocking_point[1]}" == puzzle.answer_b


def test_day_19():
    puzzle = Puzzle(year=2024, day=19)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day19(data=example.input_data)
        count, sum = solver.get_solvable_designs()
        if example.answer_a:
            assert count == int(example.answer_a)
        if example.answer_b:
            assert sum == int(example.answer_b)

    # Test real data
    solver = AoC2024Day19(data=puzzle.input_data)
    count, sum = solver.get_solvable_designs()
    if puzzle.answered_a and puzzle.answer_a:
        assert count == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert sum == int(puzzle.answer_b)


def test_day_20():
    puzzle = Puzzle(year=2024, day=20)

    # Test examples
    for example in puzzle.examples:
        solver = AoC2024Day20(data=example.input_data)
        if example.answer_a:
            assert solver.count_cheats(0, 2) == int(example.answer_a)
        if example.answer_b:
            assert solver.count_cheats(50, 20) == int(example.answer_b)

    # Test real data
    solver = AoC2024Day20(data=puzzle.input_data)
    if puzzle.answered_a and puzzle.answer_a:
        assert solver.count_cheats(100, 2) == int(puzzle.answer_a)
    if puzzle.answered_b and puzzle.answer_b:
        assert solver.count_cheats(100, 20) == int(puzzle.answer_b)
