import pathlib
import parse


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    pattern = parse.compile('{x1:d},{y1:d} -> {x2:d},{y2:d}')
    coordinates = []
    for row in puzzle_input.split('\n'):
        coordinates.append(pattern.parse(row).named)

    return coordinates


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    diagram = {}
    for row in puzzle_data:
        # horizontal
        if row['x1'] == row['x2']:
            x = row['x1']
            for y in range(row['y1'], row['y2'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1
            for y in range(row['y2'], row['y1'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1
        # vertical
        elif row['y1'] == row['y2']:
            y = row['y1']
            for x in range(row['x1'], row['x2'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1
            for x in range(row['x2'], row['x1'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1

    final = diagram.values()
    count = 0
    for num in final:
        if num > 1:
            count += 1
    return count


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    diagram = {}
    for row in puzzle_data:
        # horizontal
        if row['x1'] == row['x2']:
            x = row['x1']
            for y in range(row['y1'], row['y2'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1
            for y in range(row['y2'], row['y1'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1
        # vertical
        elif row['y1'] == row['y2']:
            y = row['y1']
            for x in range(row['x1'], row['x2'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1
            for x in range(row['x2'], row['x1'] + 1):
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1
        # diagonal
        else:
            direction = [0, 0]
            if row['x1'] - row['x2'] > 1:
                direction[0] = -1
            else:
                direction[0] = 1
            if row['y1'] - row['y2'] > 1:
                direction[1] = -1
            else:
                direction[1] = 1

            for size in range(abs(row['x1'] - row['x2']) + 1):
                x = row['x1'] + size * direction[0]
                y = row['y1'] + size * direction[1]
                if (x, y) in diagram:
                    diagram[(x, y)] += 1
                else:
                    diagram[(x, y)] = 1

    final = diagram.values()
    count = 0
    for num in final:
        if num > 1:
            count += 1
    return count


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
