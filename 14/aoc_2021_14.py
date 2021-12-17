import pathlib
import copy
import time


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    code, commands = puzzle_input.split('\n\n')
    code = [x for x in code]
    command_dict = {}
    for line in commands.strip().splitlines():
        command_dict[line[0], line[1]] = line[6]

    return command_dict, code


def part1(puzzle_data, loops=10):
    '''solve part 1 and return answer'''

    code = inserter(puzzle_data)

    return counter(code)


def counter(code):
    code_dict = {}

    for x in code:
        if x in code_dict:
            code_dict[x] += 1
        else:
            code_dict[x] = 1

    values = sorted(code_dict.values())

    return values[-1] - values[0]


def inserter(puzzle_data, loops=10):
    command_dict, code = copy.deepcopy(puzzle_data)
    insert_queue = []

    for loop in range(loops):
        for index, char in enumerate(code[:-1]):
            insert_queue.append(command_dict[code[index], code[index + 1]])
        new_code = []
        while True:
            try:
                new_code.append(code.pop(0))
                new_code.append(insert_queue.pop(0))
            except IndexError:
                break
        code = new_code
        # print(f"Loop # {loop} complete")
    return code


def part2(puzzle_data, loops=40):
    '''solve part 2 and return answer'''
    command_dict, code = copy.deepcopy(puzzle_data)
    modified_command_dict, command_counter = command_modifier(command_dict)
    last = code[-1]

    for index, char in enumerate(code[:-1]):
        command_counter[code[index], code[index + 1]] += 1

    for _ in range(loops):
        temp_command_counter = copy.deepcopy(command_counter)
        for command in modified_command_dict:
            first_new, second_new = modified_command_dict[command]
            num_pairs = command_counter[command]
            temp_command_counter[command] -= num_pairs
            temp_command_counter[first_new] += num_pairs
            temp_command_counter[second_new] += num_pairs
        command_counter = temp_command_counter
    return counter2(command_counter, last)


def command_modifier(command_dict):
    modified_command_dict = {}
    command_counter = {}

    for command in command_dict:
        modified_command_dict[command] = [(command[0], command_dict[command]), (command_dict[command], command[1])]
        command_counter[command] = 0
    return modified_command_dict, command_counter


def counter2(command_counter, last):
    code_dict = {}

    for x in command_counter:
        if x[0] in code_dict:
            code_dict[x[0]] += command_counter[x]
        else:
            code_dict[x[0]] = command_counter[x]
    code_dict[last] += 1
    values = sorted(code_dict.values())

    return values[-1] - values[0]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part2(parse_input(puzzle_input), loops=10)
    solution2 = part2(parse_input(puzzle_input), loops=40)
    return data, solution1, solution2


if __name__ == '__main__':
    start_time = time.time()
    PUZZLE_DIR = pathlib.Path(__file__).parent
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    data, solution1, solution2 = solve(puzzle_input)
    print(solution1)
    print(solution2)
    print("Execution took", (time.time() - start_time) * 1000, "ms to run")
