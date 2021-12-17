# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_16 as aoc

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
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_parse_example1():
    """Test that input is parsed properly"""
    assert aoc.parse_input('D2FE28') == '110100101111111000101000'
    assert aoc.parse_input('38006F45291200') == '00111000000000000110111101000101001010010001001000000000'
    assert aoc.parse_input('EE00D40C823060') == '11101110000000001101010000001100100000100011000001100000'


def test_translation(example1, example2, example3, example4):
    """Test part 1 on example input"""
    assert aoc.translate_packet(aoc.parse_input('D2FE28'))[0].contents == 2021
    assert aoc.translate_packet(aoc.parse_input('38006F45291200'))[0].contents[0].contents == 10
    assert aoc.translate_packet(aoc.parse_input('38006F45291200'))[0].contents[1].contents == 20
    assert aoc.translate_packet(aoc.parse_input('EE00D40C823060'))[0].contents[0].contents == 1
    assert aoc.translate_packet(aoc.parse_input('EE00D40C823060'))[0].contents[1].contents == 2
    assert aoc.translate_packet(aoc.parse_input('EE00D40C823060'))[0].contents[2].contents == 3


def test_ensure_full_consumption(example1, example2, example3, example4):
    """Test part 1 on example input"""
    assert int(aoc.translate_packet(example1)[1]) == 0
    assert int(aoc.translate_packet(example2)[1]) == 0
    assert int(aoc.translate_packet(example3)[1]) == 0
    assert int(aoc.translate_packet(example4)[1]) == 0


def test_part1_example1(example1, example2, example3, example4):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 16
    assert aoc.part1(example2) == 12
    assert aoc.part1(example3) == 23
    assert aoc.part1(example4) == 31


def test_part2_example2():
    """Test part 2 on example input"""
    assert aoc.part2(aoc.parse_input('C200B40A82')) == 3
    assert aoc.part2(aoc.parse_input('04005AC33890')) == 54
    assert aoc.part2(aoc.parse_input('880086C3E88112')) == 7
    assert aoc.part2(aoc.parse_input('CE00C43D881120')) == 9
    assert aoc.part2(aoc.parse_input('D8005AC2A8F0')) == 1
    assert aoc.part2(aoc.parse_input('F600BC2D8F')) == 0
    assert aoc.part2(aoc.parse_input('9C005AC2F8F0')) == 0
    assert aoc.part2(aoc.parse_input('9C0141080250320F1802104A08')) == 1
