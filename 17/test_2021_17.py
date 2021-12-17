# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_17 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_example(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        'x1': 20,
        'x2': 30,
        'y1': -10,
        'y2': -5
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 45


def test_part2_example1(example1, example2):
    """Test part 2 on example input"""
    assert aoc.part2(example1)[1] == example2
    assert aoc.part2(example1)[0] == 112
