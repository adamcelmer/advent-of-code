import queue
import re

def parse_buckets():
    input = {}
    with open('input.txt', 'r') as file:
        lines = []
        for line in file:
            if not "[" in line:
                break
            lines.append(line)
        lines.reverse()
        for line in lines:
            chars = list(line)
            for i, char in enumerate(chars):
                if char.isalpha():
                    char = char.upper()
                    bucket = int(i / 4) + 1
                    if bucket not in input:
                        input[bucket] = queue.LifoQueue()
                    input[bucket].put(char)
    return input

def parse_commands():
    commands = []
    with open('input.txt', 'r') as file:
        for line in file:
            if not "move" in line:
                continue
            command_raw = re.findall(r'\d+', line)
            command = tuple(map(int, command_raw))
            commands.append(command)
    return commands

def print_buckets(buckets):
    print("### Buckets ###")
    line = "init"
    while not line.strip() == "":
        line = ""
        for i in range(1, len(buckets) + 1):
            if buckets[i].empty():
                line = line + "   "
            else:
                line = line + f'[{buckets[i].get()}]'
        print(line)

buckets = parse_buckets()
commands = parse_commands()

# print_buckets(buckets)
for (move, fromm, to) in commands:
    crates_moved = []
    for i in range(0, move):
        crates_moved.append(buckets[fromm].get())
    crates_moved.reverse()
    for crate in crates_moved:
        buckets[to].put(crate)
print_buckets(buckets)
