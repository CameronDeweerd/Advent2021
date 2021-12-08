# test_aoc_template.py

import pathlib
import pytest
import aoc_2021_8 as aoc

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
        [["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"],
         ["fdgacbe", "cefdb", "cefbgd", "gcbe"]],
        [["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"],
         ["fcgedb", "cgb", "dgebacf", "gc"]],
        [["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"],
         ["cg", "cg", "fdcagb", "cbg"]],
        [["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"],
         ["efabcd", "cedba", "gadfec", "cb"]],
        [["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"],
         ["gecf", "egdcabf", "bgf", "bfgea"]],
        [["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec", "bfadeg", "bafgc", "acf"],
         ["gebdcfa", "ecba", "ca", "fadegcb"]],
        [["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"],
         ["cefg", "dcbef", "fcge", "gbcadfe"]],
        [["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf", "ced", "adcbefg", "gebcd"],
         ["ed", "bcgafe", "cdgba", "cbgef"]],
        [["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"],
         ["gbdfcae", "bgc", "cg", "cgb"]],
        [["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"],
         ["fgae", "cfgab", "fg", "bagce"]]

    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 26


@pytest.mark.skip(reason="Not implemented")
def test_part2_solution(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 61229


def test_part2_solution(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 5353


def test_part2_get_key():
    count_dict = {'a': 4, 'b': 6, 'c': 0, 'd': 0, 'e': 0, 'f': 9, 'g': 0}
    assert aoc.get_key(count_dict, 4) == 'a'
    assert aoc.get_key(count_dict, 9) == 'f'
    assert aoc.get_key(count_dict, 6) == 'b'


def test_select_num():
    chars = ["uR", "U", "M", "bR", "B"]
    assert aoc.select_num(chars) == 3


def test_part2_dict_generator(example2):
    """Test part 2 on example input"""
    assert aoc.generate_location_dict(example2[0]) == {
        'a': 'uR',
        'b': 'bR',
        'c': 'B',
        'd': 'U',
        'e': 'uL',
        'f': 'M',
        'g': 'bL'
    }
