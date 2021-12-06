import pathlib
import sys


def parse(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    return puzzle_input.split('\n')


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    digits = len(puzzle_data[0])
    count = [0] * digits
    for row in puzzle_data:
        splitNum = list(row)
        for place in range(digits):
            if splitNum[place] == '1':
                count[place] += 1
            else:
                count[place] -= 1
    final = ""
    for num in count:
        if num > 0:
            final += '1'
        else:
            final += '0'
    gamma = int(final, 2)
    epsilon = pow(2, digits) - gamma - 1
    print(gamma, epsilon)
    return gamma * epsilon


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    for count, row in enumerate(puzzle_data):
        puzzle_data[count] = list(row)

    digits = len(puzzle_data[0])

    oxy = puzzle_data.copy()
    co2 = puzzle_data.copy()

    final = ["", ""]
    for x in range(digits):
        oxy = countPos(oxy, x, True)
        final[0] += oxy[0][x]
        if len(co2) > 1:
            co2 = countPos(co2, x, False)
        final[1] += co2[0][x]

    oxy = int(final[0], 2)
    co2 = int(final[1], 2)

    return (oxy, co2, oxy * co2)


def countPos(numList, position, wantMost):
    ones = []
    zeros = []

    for row in numList:
        if row[position] == "1":
            ones.append(row)
        else:
            zeros.append(row)
    if len(ones) >= len(zeros):
        if wantMost:
            return ones
        else:
            return zeros
    else:
        if wantMost:
            return zeros
        else:
            return ones


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
