# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_14 as aoc

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
def example_code_2():
    return aoc.inserter(example1, 2)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ({
                            ('C', 'H'): 'B',
                            ('H', 'H'): 'N',
                            ('C', 'B'): 'H',
                            ('N', 'H'): 'C',
                            ('H', 'B'): 'C',
                            ('H', 'C'): 'B',
                            ('H', 'N'): 'C',
                            ('N', 'N'): 'C',
                            ('B', 'H'): 'H',
                            ('N', 'C'): 'B',
                            ('N', 'B'): 'B',
                            ('B', 'N'): 'B',
                            ('B', 'B'): 'N',
                            ('B', 'C'): 'B',
                            ('C', 'C'): 'N',
                            ('C', 'N'): 'C'},
                        ['N', 'N', 'C', 'B'])


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.inserter(example1, 1) == [x for x in 'NCNBCHB']
    assert aoc.inserter(example1, 2) == [x for x in 'NBCCNBBBCBHCB']
    assert aoc.inserter(example1, 3) == [x for x in 'NBBBCNCCNBBNBNBBCHBHHBCHB']
    assert aoc.inserter(example1, 4) == [x for x in 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB']


def test_part1_counter(example1):
    """Test part 1 on example input"""
    assert aoc.counter(aoc.inserter(example1, 2)) == 5
    assert aoc.counter(aoc.inserter(example1, 10)) == 1588


def test_part2_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part2(example1, 2) == 5
    assert aoc.part2(example1, 10) == 1588
