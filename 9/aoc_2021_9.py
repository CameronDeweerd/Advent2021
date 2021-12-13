import pathlib
import sys


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    puzzle_data = []
    for x in puzzle_input.strip().splitlines():
        nums = list(map(int, x))
        nums.insert(0, 9)
        nums.append(9)
        puzzle_data.append(nums)
    nines = [9] * len(puzzle_data[0])
    puzzle_data.append(nines)
    puzzle_data.insert(0, nines)
    return puzzle_data


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    risk_sum = 0
    last_col_index = len(puzzle_data[0]) - 1
    last_row_index = len(puzzle_data) - 1

    for row_num, row in enumerate(puzzle_data[:-1]):
        if row_num == 0:
            continue
        for col_num, value in enumerate(row[:-1]):
            if col_num == 0:
                continue
            for row_offset, col_offset in (
                    (row_num, col_num + 1), (row_num, col_num - 1),
                    (row_num + 1, col_num), (row_num - 1, col_num)):
                # if row_offset == -1 or col_offset == -1 or row_offset > last_row_index or col_offset > last_col_index:
                #     continue
                if value >= puzzle_data[row_offset][col_offset]:
                    break
            else:
                risk_sum += value + 1

    return risk_sum


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    basin_tracker = []
    # change the data to only have 1s and 9s
    for row_num, row in enumerate(puzzle_data):
        for col_num, value in enumerate(row):
            if not value == 9:
                puzzle_data[row_num][col_num] = 1

    for row_num, row in enumerate(puzzle_data):
        for col_num, value in enumerate(row):
            if value == 1:  # untouched basin found; begin search
                check_queue = [(row_num, col_num)]
                basin = 1
                puzzle_data[row_num][col_num] = 0

                # breadth-first search
                while check_queue:
                    current_row, current_col = check_queue.pop(0)
                    for row_offset, col_offset in (
                            (current_row, current_col + 1), (current_row, current_col - 1),
                            (current_row + 1, current_col), (current_row - 1, current_col)):
                        if puzzle_data[row_offset][col_offset] == 1:
                            check_queue.append((row_offset, col_offset))
                            basin += 1
                            puzzle_data[row_offset][col_offset] = 0
                basin_tracker.append(basin)
    basin_tracker = sorted(basin_tracker, reverse=True)
    return basin_tracker[0] * basin_tracker[1] * basin_tracker[2]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return data, solution1, solution2


if __name__ == '__main__':
    PUZZLE_DIR = pathlib.Path(__file__).parent
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    data, solution1, solution2 = solve(puzzle_input)
    print(solution1)
    print(solution2)
