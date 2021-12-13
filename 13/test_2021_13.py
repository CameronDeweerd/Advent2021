# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_13 as aoc

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
    assert example1 == ({
                            (0, 3),
                            (0, 13),
                            (0, 14),
                            (1, 10),
                            (2, 14),
                            (3, 0),
                            (3, 4),
                            (4, 1),
                            (4, 11),
                            (6, 0),
                            (6, 10),
                            (6, 12),
                            (8, 4),
                            (8, 10),
                            (9, 0),
                            (9, 10),
                            (10, 4),
                            (10, 12)
                        }, [
                            {'letter': 'y', 'num': 7},
                            {'letter': 'x', 'num': 5}
                        ])


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 17


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 16
