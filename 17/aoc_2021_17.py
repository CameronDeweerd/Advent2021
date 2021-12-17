import pathlib
import parse
import time


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    pattern = parse.compile('target area: x={x1:d}..{x2:d}, y={y1:d}..{y2:d}')
    coordinates = pattern.parse(puzzle_input).named
    return coordinates


def parse_example(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    puzzle_input = puzzle_input.strip().split()
    return sorted(puzzle_input)


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    return (-puzzle_data['y1']) * (-puzzle_data['y1'] - 1) / 2


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    # x_options = calculate_legal_x(puzzle_data)
    # y_options = calculate_legal_y(puzzle_data)
    count = 0
    trajectory_list = []
    for x in range(puzzle_data['x2'] + 1):
        for y in range(puzzle_data['y1'], -puzzle_data['y1']):
            if follow_trajectory(x, y, puzzle_data):
                count += 1
                trajectory_list.append(''.join([str(x), ',', str(y)]))
    return count, sorted(trajectory_list)


def follow_trajectory(x_angle, y_angle, target):
    current_x = 0
    current_y = 0

    while True:
        current_x += x_angle
        current_y += y_angle
        if x_angle > 0:
            x_angle -= 1
        y_angle -= 1

        if check_is_within_target(current_x, current_y, target):
            return True
        if check_overshot(current_x, current_y, target):
            return False


def check_is_within_target(current_x, current_y, target):
    return target['x1'] <= current_x <= target['x2'] and target['y1'] <= current_y <= target['y2']


def check_overshot(current_x, current_y, target):
    return target['x2'] < current_x or current_y < target['y1']


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
