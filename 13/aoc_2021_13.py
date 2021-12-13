import pathlib
import parse
import matplotlib.pyplot as plt


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    top_pattern = parse.compile('{x:d},{y:d}')
    bot_pattern = parse.compile('fold along {letter:l}={num:d}')

    top, bottom = puzzle_input.strip().split("\n\n")
    top = top.splitlines()
    bottom = bottom.splitlines()

    nums = set(map(lambda x: tuple(top_pattern.parse(x).named.values()), top))
    folds = list(map(lambda x: bot_pattern.parse(x).named, bottom))

    return nums, folds


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    dots = puzzle_data[0]
    commands = puzzle_data[1]
    command = commands[0]
    # for command in commands:
    change_queue = []
    for dot in dots:
        if command['letter'] == 'x':
            if dot[0] > command['num']:
                change_queue.append(((dot[0] - ((dot[0] - command['num']) * 2), dot[1]), dot))

        else:
            if dot[1] > command['num']:
                change_queue.append(((dot[0], dot[1] - ((dot[1] - command['num']) * 2)), dot))

    while change_queue:
        new, old = change_queue.pop()
        dots.add(new)
        dots.remove(old)

    return len(dots)


def draw(dots):
    x, y = list(zip(*dots))
    y = [-n for n in y]
    plt.scatter(x, y)
    plt.show()
    return


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    dots = puzzle_data[0]
    commands = puzzle_data[1]
    for command in commands:
        change_queue = []
        for dot in dots:
            if command['letter'] == 'x':
                if dot[0] > command['num']:
                    change_queue.append(((dot[0] - ((dot[0] - command['num']) * 2), dot[1]), dot))

            else:
                if dot[1] > command['num']:
                    change_queue.append(((dot[0], dot[1] - ((dot[1] - command['num']) * 2)), dot))

        while change_queue:
            new, old = change_queue.pop()
            dots.add(new)
            dots.remove(old)

    draw(dots)
    return len(dots)


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
