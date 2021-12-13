import pathlib
import sys


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    data = []
    x = puzzle_input.strip().splitlines()
    for line in x:
        data.append(list(line))
    return data


def part1(puzzle_data):
    '''solve part 1 and return answer'''

    error_dict = {"}": 0, "]": 0, ">": 0, ")": 0}

    for line in puzzle_data:
        left_stack = []
        for bracket in line:
            if bracket in ("{", "[", "<", "("):
                left_stack.append(bracket)
                continue
            else:
                left = left_stack.pop()
                if left == "{" and bracket == "}":
                    continue
                if left == "[" and bracket == "]":
                    continue
                if left == "<" and bracket == ">":
                    continue
                if left == "(" and bracket == ")":
                    continue
                error_dict[bracket] += 1
                break

    score = (error_dict[")"] * 3) + (error_dict["]"] * 57) + (error_dict["}"] * 1197) + (error_dict[">"] * 25137)
    return score


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    scores = []
    autocomplete_dict = {"(": 1, "[": 2, "{": 3, "<": 4}

    for line in puzzle_data:
        left_stack = []
        for bracket in line:
            if bracket in ("{", "[", "<", "("):
                left_stack.append(bracket)
                continue
            else:
                left = left_stack.pop()
                if left == "{" and bracket == "}":
                    continue
                if left == "[" and bracket == "]":
                    continue
                if left == "<" and bracket == ">":
                    continue
                if left == "(" and bracket == ")":
                    continue
                break
        else:
            score = 0
            for bracket in reversed(left_stack):
                score *= 5
                score += autocomplete_dict[bracket]
            scores.append(score)
    scores = sorted(scores)
    return scores[len(scores) // 2]


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
