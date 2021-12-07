import pathlib
import sys


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    return sorted(map(int, puzzle_input.split(',')))


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    current_target = puzzle_data[len(puzzle_data) // 2]

    fuel_cost = calculate_fuel_1(puzzle_data, current_target)
    next_fuel_cost = calculate_fuel_1(puzzle_data, current_target + 1)

    # decide if we need to check higher or lower numbers
    if next_fuel_cost < fuel_cost:
        direction = 1
    else:
        direction = -1

    while True:
        next_fuel_cost = calculate_fuel_1(puzzle_data, current_target + direction)
        if next_fuel_cost > fuel_cost:
            return current_target, fuel_cost
        else:
            current_target = current_target + direction
            fuel_cost = next_fuel_cost


def calculate_fuel_1(crabs, target):
    total = 0
    for crab in crabs:
        total += abs(target - crab)
    return total


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    current_target = puzzle_data[len(puzzle_data) // 2]

    fuel_cost = calculate_fuel_2(puzzle_data, current_target)
    next_fuel_cost = calculate_fuel_2(puzzle_data, current_target + 1)

    # decide if we need to check higher or lower numbers
    if next_fuel_cost < fuel_cost:
        direction = 1
    else:
        direction = -1

    while True:
        next_fuel_cost = calculate_fuel_2(puzzle_data, current_target + direction)
        if next_fuel_cost > fuel_cost:
            return current_target, fuel_cost
        else:
            current_target = current_target + direction
            fuel_cost = next_fuel_cost


def calculate_fuel_2(crabs, target):
    total = 0
    for crab in crabs:
        n = abs(target - crab)
        total += n * (n + 1) // 2
    return total


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
