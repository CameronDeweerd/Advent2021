import pathlib
import sys


def parse(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    data = []
    for line in puzzle_input.split('\n'):
        x = line.split()
        data.append((x[0], int(x[1])))
    return data


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    location = [0, 0]
    for x in puzzle_data:
        if x[0] == 'forward':
            location[0] += x[1]
        elif x[0] == 'down':
            location[1] += x[1]
        else:
            location[1] -= x[1]
    print(location)
    return location[0] * location[1]


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    aim = 0
    location = [0, 0]
    for x in puzzle_data:
        if x[0] == 'forward':
            location[0] += x[1]
            location[1] += aim * x[1]
        elif x[0] == 'down':
            aim += x[1]
        else:
            aim -= x[1]
    print(location)
    return location[0] * location[1]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return data, solution1, solution2


if __name__ == '__main__':
    PUZZLE_DIR = pathlib.Path(__file__).parent
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    data, solution1, solution2 = solve(puzzle_input)
    print(solution1)
    print(solution2)
