import pathlib
import sys


def parse(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''


def part1(puzzle_data):
    '''solve part 1 and return answer'''


def part2(puzzle_data):
    '''solve part 2 and return answer'''


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return data, solution1, solution2


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data, solution1, solution2 = solve(puzzle_input)
        print(solution1)
        print(solution2)
