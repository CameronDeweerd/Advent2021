import pathlib
import sys
import time


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''


def part1(puzzle_data):
    '''solve part 1 and return answer'''


def part2(puzzle_data):
    '''solve part 2 and return answer'''


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return data, solution1, solution2


if __name__ == '__main__':
    start_time = time.time()
    PUZZLE_DIR = pathlib.Path(__file__).parent
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    data, solution1, solution2 = solve(puzzle_input)
    print(solution1)
    print(solution2)
    print("Execution took", (time.time() - start_time) * 1000, "ms to run")
