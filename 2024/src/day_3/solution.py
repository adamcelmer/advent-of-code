#!python
import re

mul_regex = "mul\([0-9]{1,3},[0-9]{1,3}\)"
do_regex = "do\(\)"
dont_regex = "don't\(\)"

def parse_input():
    with open('input.txt', 'r') as f:
        return f.read()


def parse_instruction(raw_instruction: str):
    return tuple(int(x) for x in raw_instruction[4:len(raw_instruction) - 1].split(','))


def part_1(corrupted_instructions: str):
    instructions = re.findall(mul_regex, corrupted_instructions)
    total = 0
    for instruction in instructions:
        nums = parse_instruction(instruction)
        total = total + nums[0] * nums[1]
    return total


def find_closest_smaller_than(number: int, numbers: list[int]):
    if not numbers:
        return None
    filtered = list(filter(lambda x: x < number, numbers))
    if not filtered:
        return None
    return max(filtered)


def part_2(corrupted_instructions: str):
    instructions = [(i.start(), parse_instruction(i.group())) for i in re.finditer(mul_regex, corrupted_instructions)]
    dos = [d.start() for d in re.finditer(do_regex, corrupted_instructions)]
    donts = [d.start() for d in re.finditer(dont_regex, corrupted_instructions)]
    total = 0
    for position, value in instructions:
        closest_do = find_closest_smaller_than(position, dos)
        closest_dont = find_closest_smaller_than(position, donts)
        if not closest_dont:
            total = total + value[0] * value[1]
            continue
        if not closest_do:
            continue
        if closest_do > closest_dont:
            total = total + value[0] * value[1]
    return total



if __name__ == '__main__':
    corrupted_instructions = parse_input()
    print(part_1(corrupted_instructions))
    print(part_2(corrupted_instructions))
