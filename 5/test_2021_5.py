# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_5 as aoc

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
        {'x1': 0, 'y1': 9, 'x2': 5, 'y2': 9},
        {'x1': 8, 'y1': 0, 'x2': 0, 'y2': 8},
        {'x1': 9, 'y1': 4, 'x2': 3, 'y2': 4},
        {'x1': 2, 'y1': 2, 'x2': 2, 'y2': 1},
        {'x1': 7, 'y1': 0, 'x2': 7, 'y2': 4},
        {'x1': 6, 'y1': 4, 'x2': 2, 'y2': 0},
        {'x1': 0, 'y1': 9, 'x2': 2, 'y2': 9},
        {'x1': 3, 'y1': 4, 'x2': 1, 'y2': 4},
        {'x1': 0, 'y1': 0, 'x2': 8, 'y2': 8},
        {'x1': 5, 'y1': 5, 'x2': 8, 'y2': 2}
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 5


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 12
