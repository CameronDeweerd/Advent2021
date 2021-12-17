# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_15 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2_parse2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse2_input(puzzle_input)


def test_parse_example2(example2_parse2):
    """Test that input is parsed properly"""
    assert len(example2_parse2) == 100
    assert example2_parse2[0, 0].value == 1
    assert example2_parse2[0, 1].value == 7
    assert example2_parse2[1, 0].value == 1
    assert example2_parse2[1, 1].value == 3
    assert example2_parse2[8, 8].value == 9
    assert example2_parse2[8, 9].value == 6
    assert example2_parse2[9, 8].value == 9
    assert example2_parse2[9, 9].value == 2


def test_parse2_example2(example2):
    """Test that input is parsed properly"""
    assert len(example2) == 4
    assert example2[0, 0].value == 1
    assert example2[0, 1].value == 7
    assert example2[1, 0].value == 1
    assert example2[1, 1].value == 3


def test_part1(example1, example2):
    """Test part 1 on example input"""
    assert aoc.part1(example2) == 4
    assert aoc.part1(example1) == 40


def test_part2_example2(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 315
