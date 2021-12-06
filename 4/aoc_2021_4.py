import pathlib
import sys


def parse(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    puzzle_input = puzzle_input.replace("  ", " ")
    puzzle_input = puzzle_input.split('\n\n')

    numbers = []
    for x in puzzle_input[0].split(','):
        numbers.append(int(x))

    boards = []
    for boardNum, board in enumerate(puzzle_input[1:]):
        boards.append([])
        for rowNum, row in enumerate(board.split('\n')):
            boards[boardNum].append([])
            for x in row.split(' '):
                if x:
                    boards[boardNum][rowNum].append(int(x))

    return numbers, boards


def part1(puzzle_data):
    '''solve part 1 and return answer'''

    nums = puzzle_data[0]
    boards = puzzle_data[1]
    rotated_boards = []
    for board in boards:
        rotated_boards.append(list(map(list, zip(*board[::-1]))))

    count = 0
    while True:
        pulled = nums[count]

        for board in boards:
            for row in board:
                if pulled in row:
                    row.remove(pulled)
                    if len(row) == 0:
                        return get_score(board, pulled)

        for board in rotated_boards:
            for row in board:
                if pulled in row:
                    row.remove(pulled)
                    if len(row) == 0:
                        return get_score(board, pulled)
        count += 1


def get_score(board, pulled):
    sum = 0
    for row in board:
        for num in row:
            sum += num
    return sum * pulled


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    nums = puzzle_data[0]
    boards = puzzle_data[1]
    rotated_boards = []
    for board in boards:
        rotated_boards.append(list(map(list, zip(*board[::-1]))))

    count = 0
    while True:
        pulled = nums[count]

        winner = []
        for boardNum, board in enumerate(boards):
            for row in board:
                if pulled in row:
                    row.remove(pulled)
                    if len(row) == 0:
                        winner.append(boardNum)

        for boardNum, board in enumerate(rotated_boards):
            for row in board:
                if pulled in row:
                    row.remove(pulled)
                    if len(row) == 0 and boardNum not in winner:
                        winner.append(boardNum)
        if winner:
            for boardNum in sorted(winner, reverse=True):
                if len(boards) == 1:
                    return get_score(boards[0], pulled)
                else:
                    boards.pop(boardNum)
                    rotated_boards.pop(boardNum)

        count += 1


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
