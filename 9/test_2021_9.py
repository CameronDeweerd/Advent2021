# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_9 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 2, 1, 9, 9, 9, 4, 3, 2, 1, 0, 9],
        [9, 3, 9, 8, 7, 8, 9, 4, 9, 2, 1, 9],
        [9, 9, 8, 5, 6, 7, 8, 9, 8, 9, 2, 9],
        [9, 8, 7, 6, 7, 8, 9, 6, 7, 8, 9, 9],
        [9, 9, 8, 9, 9, 9, 6, 5, 6, 7, 8, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 15


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 1134
