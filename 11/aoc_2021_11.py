import pathlib
import sys


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    data = []
    for x in puzzle_input.strip().splitlines():
        data.append([int(char) for char in x])
    return data


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    flash_count = 0
    last_col_index = len(puzzle_data[0]) - 1
    last_row_index = len(puzzle_data) - 1
    flash_queue = []
    rezero_queue = []

    for _ in range(100):

        # initial incrementing of everything
        for row_num, row in enumerate(puzzle_data):
            for col_num, value in enumerate(row):
                puzzle_data[row_num][col_num] += 1
                if puzzle_data[row_num][col_num] == 10:
                    flash_queue.append((row_num, col_num))
                    rezero_queue.append((row_num, col_num))

        # popping and chaining
        while flash_queue:
            row_num, col_num = flash_queue.pop()
            for row_offset, col_offset in (
                    (row_num + 1, col_num + 1), (row_num, col_num + 1), (row_num - 1, col_num + 1),
                    (row_num + 1, col_num), (row_num - 1, col_num),
                    (row_num + 1, col_num - 1), (row_num, col_num - 1), (row_num - 1, col_num - 1)):

                if row_offset == -1 or col_offset == -1 or row_offset > last_row_index or col_offset > last_col_index:
                    continue
                puzzle_data[row_offset][col_offset] += 1
                if puzzle_data[row_offset][col_offset] == 10:
                    flash_queue.append((row_offset, col_offset))
                    rezero_queue.append((row_offset, col_offset))

        # cleanup and counting
        while rezero_queue:
            row_num, col_num = rezero_queue.pop()
            puzzle_data[row_num][col_num] = 0
            flash_count += 1

    return flash_count


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    flash_count = 0
    last_col_index = len(puzzle_data[0]) - 1
    last_row_index = len(puzzle_data) - 1
    flash_queue = []
    rezero_queue = []
    step_num = 0

    while True:
        step_num += 1
        # initial incrementing of everything
        for row_num, row in enumerate(puzzle_data):
            for col_num, value in enumerate(row):
                puzzle_data[row_num][col_num] += 1
                if puzzle_data[row_num][col_num] == 10:
                    flash_queue.append((row_num, col_num))
                    rezero_queue.append((row_num, col_num))

        # popping and chaining
        while flash_queue:
            row_num, col_num = flash_queue.pop()
            for row_offset, col_offset in (
                    (row_num + 1, col_num + 1), (row_num, col_num + 1), (row_num - 1, col_num + 1),
                    (row_num + 1, col_num), (row_num - 1, col_num),
                    (row_num + 1, col_num - 1), (row_num, col_num - 1), (row_num - 1, col_num - 1)):

                if row_offset == -1 or col_offset == -1 or row_offset > last_row_index or col_offset > last_col_index:
                    continue
                puzzle_data[row_offset][col_offset] += 1
                if puzzle_data[row_offset][col_offset] == 10:
                    flash_queue.append((row_offset, col_offset))
                    rezero_queue.append((row_offset, col_offset))

        # cleanup and counting
        if len(rezero_queue) == 100:
            return step_num
        while rezero_queue:
            row_num, col_num = rezero_queue.pop()
            puzzle_data[row_num][col_num] = 0


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
