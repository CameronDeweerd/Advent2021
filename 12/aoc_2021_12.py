import pathlib
import copy


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    connections = {}
    data = puzzle_input.strip().splitlines()
    for line in data:
        left, right = line.split('-')
        if left not in connections:
            connections[left] = {right}
        else:
            connections[left].add(right)

        if right not in connections:
            connections[right] = {left}
        else:
            connections[right].add(left)

    return connections


def part1(puzzle_data):
    '''solve part 1 and return answer'''
    return recurse_visit_1(copy.deepcopy(puzzle_data), 'start')


def recurse_visit_1(path_map, current):
    path_count = 0
    if current == 'end':
        return 1
    if path_map[current] == {}:
        return 0

    next_rooms = path_map[current]
    # prevent re-entry if a lowercase room
    if current.islower():
        for room in next_rooms:
            path_map[room].remove(current)

    for room in next_rooms:
        path_count += recurse_visit_1(copy.deepcopy(path_map), room)

    return path_count


def part2(puzzle_data):
    '''solve part 2 and return answer'''

    return recurse_visit_2(copy.deepcopy(puzzle_data), 'start', ['start'], False)


def recurse_visit_2(path_map, current, history, small_twice):
    path_count = 0
    if current == 'end':
        return 1
    if path_map[current] == {}:
        return 0

    # track all lowercase rooms visited. As soon as a one is visited a second time begin removing them from the options
    if current.islower():
        if small_twice or current == 'start':
            for room in path_map[current]:
                path_map[room].remove(current)
        elif current in history:
            # as soon as we've visited a small room a second time, all small rooms are ineligable for 2nd visits
            small_twice = True
            for past_room in history[1:]:  # skip 'start'
                for key in path_map.keys():
                    try:
                        path_map[key].remove(past_room)
                    except KeyError:
                        pass
        else:
            history.append(current)

    for room in path_map[current]:
        path_count += recurse_visit_2(copy.deepcopy(path_map), room, copy.deepcopy(history), small_twice)

    return path_count


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
