#!python
import re
from re import Match

mul_regex = "mul\([0-9]{1,3},[0-9]{1,3}\)"

def parse_input():
    with open('input-demo.txt', 'r') as f:
        return f.read()


def part_1(corrupted_instructions: str):
    instructions = re.findall(mul_regex, corrupted_instructions)
    total = 0
    for instruction in instructions:
        nums = tuple(int(x) for x in instruction[4:len(instruction) - 1].split(','))
        total = total + nums[0] * nums[1]
    return total


def part_2(corrupted_instructions: str):
    do = True
    instructions = re.findall(mul_regex, corrupted_instructions)
    print(re.search('mul\(5,5\)', corrupted_instructions).start())
    return 0


if __name__ == '__main__':
    corrupted_instructions = parse_input()
    # print(part_1(corrupted_instructions))
    part_2(corrupted_instructions)