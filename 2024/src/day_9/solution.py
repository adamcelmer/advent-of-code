import copy
from typing import List

parsed_files = []
parsed_spaces = []
with open('input-demo.txt', 'r') as f:
    i = 0
    while True:
        char = f.read(1)
        if not char:
            break
        char = int(char)
        if i % 2 == 0:
            parsed_files.append(char)
        else:
            parsed_spaces.append(char)
        i = i + 1

def part_1(files: List[int], spaces: List[int]):
    output = [0] * files[0]
    files = files[1:]
    first_file_idx = 1
    last_file_idx = len(files)
    process_file = True
    while spaces:
        if process_file:
            if not files:
                break
            for i in range(0, spaces[0]):
                if not files:
                    break
                if files[-1] <= 0:
                    files = files[:-1]
                    last_file_idx = last_file_idx - 1
                output.append(last_file_idx)
                files[-1] = files[-1] -1
            spaces = spaces[1:]
        else:
            for i in range(0, files[0]):
                output.append(first_file_idx)
            files = files[1:]
            first_file_idx = first_file_idx + 1
        process_file = not process_file

    checksum = 0
    for f_idx, f_id in enumerate(output):
        checksum = checksum + f_idx * f_id
    print(f'Part 1: {checksum}')


def part_2(files: List[int], spaces: List[int]):
    output = [0] * files[0]
    files = files[1:]
    # for f_idx in range(len(files) - 1, 0, -1):


part_1(copy.deepcopy(parsed_files), copy.deepcopy(parsed_spaces))
part_2(parsed_files, parsed_spaces)
