import pathlib
import parse


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    fish_dictionary = {}
    for x in range(-1, 9):
        fish_dictionary[x] = 0
    fish_list = list(map(int, puzzle_input.split(',')))

    for fish in fish_list:
        if fish in fish_dictionary:
            fish_dictionary[fish] += 1

    return fish_dictionary


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    duration = 80
    for _ in range(duration):
        for x in range(0, 9):
            puzzle_data[x - 1] = puzzle_data[x]
        puzzle_data[8] = puzzle_data[-1]
        puzzle_data[6] += puzzle_data[-1]
        puzzle_data[-1] = 0
    return sum(puzzle_data.values())


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    duration = 256
    for _ in range(duration):
        for x in range(0, 9):
            puzzle_data[x - 1] = puzzle_data[x]
        puzzle_data[8] = puzzle_data[-1]
        puzzle_data[6] += puzzle_data[-1]
        puzzle_data[-1] = 0
    return sum(puzzle_data.values())


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(parse_input(puzzle_input))
    solution2 = part2(parse_input(puzzle_input))
    return data, solution1, solution2


if __name__ == '__main__':
    PUZZLE_DIR = pathlib.Path(__file__).parent
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    data, solution1, solution2 = solve(puzzle_input)
    print(solution1)
    print(solution2)
