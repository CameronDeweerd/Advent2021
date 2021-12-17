import pathlib
import time
from math import prod


def parse_input(puzzle_input):
    '''take the puzzle input data and convert it into usable data'''
    bin_list = list(map(lambda x: bin(int(x, 16))[2:].zfill(4), puzzle_input.strip()))
    return ''.join(bin_list)


class Packet:
    def __init__(self, version=None, typeID=None):
        self.version = version
        self.typeID = typeID
        self.contents = None


def part1(puzzle_data):
    '''solve part 1 and return answer'''

    outer_packet, remainder = translate_packet(puzzle_data)
    return count_versions(outer_packet)


def translate_packet(packet_binary_data):
    new_packet = Packet(int(packet_binary_data[0:3], 2), int(packet_binary_data[3:6], 2))
    packet_binary_data = packet_binary_data[6:]

    # if is a "literal value" packet
    if new_packet.typeID == 4:
        new_packet.contents, packet_binary_data = create_literal_packet(packet_binary_data)
        return new_packet, packet_binary_data
    else:
        new_packet.contents, packet_binary_data = create_operation_packet(packet_binary_data)
        return new_packet, packet_binary_data


def create_literal_packet(packet_binary_data):
    bin_num = ""
    while True:
        prefix, current_val, packet_binary_data = packet_binary_data[0:1], packet_binary_data[1:5], packet_binary_data[
                                                                                                    5:]
        bin_num += current_val
        if prefix == '0':
            break
    return int(bin_num, 2), packet_binary_data


def create_operation_packet(packet_binary_data):
    if packet_binary_data[0] == '0':
        num_subpacket_bits = int(packet_binary_data[1:16], 2)
        packet_binary_data = packet_binary_data[16:]
        contents = []
        subsection, packet_binary_data = packet_binary_data[0:num_subpacket_bits], packet_binary_data[
                                                                                   num_subpacket_bits:]
        while '1' in subsection:  # open packets until the subsection is consumed
            subpacket, subsection = translate_packet(subsection)
            contents.append(subpacket)
        return contents, packet_binary_data

    elif packet_binary_data[0] == '1':
        num_subpackets = int(packet_binary_data[1:12], 2)
        packet_binary_data = packet_binary_data[12:]
        contents = []
        while num_subpackets > 0:  # open packets until the we open N subpackets
            subpacket, packet_binary_data = translate_packet(packet_binary_data)
            contents.append(subpacket)
            num_subpackets -= 1
        return contents, packet_binary_data


def count_versions(packet):
    total = packet.version
    if not packet.typeID == 4:
        for subpacket in packet.contents:
            total += count_versions(subpacket)
    return total


def part2(puzzle_data):
    '''solve part 2 and return answer'''
    outer_packet, remainder = translate_packet(puzzle_data)
    return process_packet(outer_packet)


def process_packet(packet):
    packetID = packet.typeID
    if packetID == 0:
        nums = open_nested_packets(packet)
        value = sum(nums)

    elif packetID == 1:
        nums = open_nested_packets(packet)
        value = prod(nums)

    elif packetID == 2:
        nums = open_nested_packets(packet)
        value = min(nums)

    elif packetID == 3:
        nums = open_nested_packets(packet)
        value = max(nums)

    elif packetID == 4:
        value = packet.contents
    elif packetID == 5:
        nums = open_nested_packets(packet)
        value = 1 if nums[0] > nums[1] else 0

    elif packetID == 6:
        nums = open_nested_packets(packet)
        value = 1 if nums[0] < nums[1] else 0

    elif packetID == 7:
        nums = open_nested_packets(packet)
        value = 1 if nums[0] == nums[1] else 0

    return value


def open_nested_packets(packet):
    return list(map(lambda y: process_packet(y), packet.contents))


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(parse_input(puzzle_input))
    solution2 = part2(parse_input(puzzle_input))
    return data, solution1, solution2


if __name__ == '__main__':
    start_time = time.time()
    PUZZLE_DIR = pathlib.Path(__file__).parent
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    data, solution1, solution2 = solve(puzzle_input)
    print(solution1)
    print(solution2)
    print("Execution took", (time.time() - start_time) * 1000, "ms to run")
