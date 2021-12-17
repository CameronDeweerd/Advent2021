import pathlib
import sys
import time


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.shortest = None


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    rows = puzzle_input.strip().splitlines()
    height = len(rows)
    width = len(rows[0])
    grid = {}
    for col in range(height):
        for row in range(width):
            grid[col, row] = Node(int(rows[col][row]))
    return grid


def parse2_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    rows = puzzle_input.strip().splitlines()
    height = len(rows)
    width = len(rows[0])
    grid = {}

    for col in range(height):
        for row in range(width):
            for right in range(5):
                for down in range(5):
                    val = (int(rows[col][row]) + right + down - 1) % 9 + 1
                    grid[col + width * right, row + height * down] = Node(val)
    return grid


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    max_height_index = int(len(puzzle_data) ** 0.5) - 1
    max_width_index = int(len(puzzle_data) ** 0.5) - 1

    gr = puzzle_data
    gr[0, 0].shortest = 0
    gr[0, 0].visited = True

    check_queue = [((0, 0), (0, 1)),
                   ((0, 0), (1, 0))]

    while check_queue:
        past_node, next_node = check_queue.pop(0)
        if gr[next_node].visited is False or gr[next_node].shortest > gr[past_node].shortest + gr[next_node].value:
            gr[next_node].visited = True
            gr[next_node].shortest = gr[past_node].shortest + gr[next_node].value

            row, col = next_node
            for row_offset, col_offset in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if row_offset < 0 or row_offset > max_height_index or col_offset < 0 or col_offset > max_width_index:
                    continue
                check_queue.append(((row, col), (row_offset, col_offset)))

    return gr[max_height_index, max_width_index].shortest


def part2(puzzle_data):
    '''solve part 2 and return answer'''


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(parse_input(puzzle_input))
    solution2 = part1(parse2_input(puzzle_input))
    return data, solution1, solution2


if __name__ == '__main__':
    start_time = time.time()
    PUZZLE_DIR = pathlib.Path(__file__).parent
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    data, solution1, solution2 = solve(puzzle_input)
    print(solution1)
    print(solution2)
    print("Execution took", (time.time() - start_time) * 1000, "ms to run")
