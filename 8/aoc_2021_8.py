import pathlib
import sys


def parse_input(puzzle_input):
    """take the puzzle input data and convert it into usable data"""
    puzzle_data = []
    for line in puzzle_input.strip().split("\n"):
        line_data = line.split(" | ")
        line_data[0] = line_data[0].split(" ")
        line_data[1] = line_data[1].split(" ")
        puzzle_data.append(line_data)
    return puzzle_data


def part1(puzzle_data):
    """solve part 1 and return answer"""
    count = 0
    for line in puzzle_data:
        for sequence in line[1]:
            if len(sequence) in (2, 3, 4, 7):
                count += 1
    return count


def part2(puzzle_data):
    """solve part 2 and return answer"""
    sum = 0
    for line in puzzle_data:
        location_dict = generate_location_dict(line[0])
        for count, sequence in enumerate(line[1]):
            chars = []
            for letter in sequence:
                chars.append(location_dict[letter])
            sum += pow(10, (3 - count)) * select_num(chars)

    return sum


def select_num(chars):
    '''
    :param chars: list[str]
    :return: int
    '''
    # return all the countable numbers
    len_dict = {2: 1, 3: 7, 4: 4, 7: 8}
    if len(chars) in len_dict:
        return len_dict[len(chars)]

    # return 0
    if "M" not in chars:
        return 0

    # return 6 and 9
    if len(chars) == 6:
        if 'bL' in chars:
            return 6
        else:
            return 9

    # return 5
    if 'uL' in chars:
        return 5

    # return 2 and 3
    if 'bR' in chars:
        return 3
    else:
        return 2


def generate_location_dict(line):
    """
    :param line: list[str]; len = 10
    :return location_dict: dict[str] = str; len - 7

    assume the following 7 positions and map each letter to one them:
          |---U---|
         uL      uR
         |---M---|
        bL      bR
        |---B---|

    example Output:
        location_dict = {
            'a': 'uR',
            'b': 'bR',
            'c': 'B',
            'd': 'U',
            'e': 'uL',
            'f': 'M',
            'g': 'bL'
            }
    """
    location_dict = {}
    # based on how many times certain letters appear we can narrow down where they control
    count_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for sequence in line:
        for letter in sequence:
            count_dict[letter] += 1
    location_dict[get_key(count_dict, 4)] = "bL"
    location_dict[get_key(count_dict, 6)] = "uL"
    location_dict[get_key(count_dict, 9)] = "bR"

    # find symbols that make up number 1 and get uR
    for sequence in line:
        if len(sequence) == 2:
            sequence = sequence.replace(get_key(location_dict, "bR"), "")
            location_dict[sequence] = "uR"

    # find symbols that make up number 4 and get M
    for sequence in line:
        if len(sequence) == 4:
            for spot in ("uL", "uR", 'bR'):
                sequence = sequence.replace(get_key(location_dict, spot), "")
            location_dict[sequence] = "M"

    # find symbols that make up number 7 and get U
    for sequence in line:
        if len(sequence) == 3:
            for spot in ("uR", 'bR'):
                sequence = sequence.replace(get_key(location_dict, spot), "")
            location_dict[sequence] = "U"

    # find symbols that make up number 8 and get U
    for sequence in line:
        if len(sequence) == 7:
            for spot in ('U', "uL", "uR", "uM", "bL", 'bR'):
                sequence = sequence.replace(get_key(location_dict, spot), "")
            location_dict[sequence] = "B"

    return location_dict


def get_key(mydict, value):
    return list(mydict.keys())[list(mydict.values()).index(value)]


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
