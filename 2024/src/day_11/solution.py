from time import time

def current_milli_time():
    return round(time() * 1000)

def parse_input():
    with open('input.txt', 'r') as f:
        return f.read().split()


def process_stone(stone: str):
    new_stones = []
    if stone == '0':
        new_stones.append('1')
    elif len(stone) % 2 == 0:
        new_stones.append(str(int(stone[:len(stone)//2])))
        second_half = stone[len(stone)//2:]
        if set(second_half) == {'0'}:
            new_stones.append('0')
        else:
            new_stones.append(str(int(stone[len(stone)//2:])))
    else:
        new_stones.append(str(int(stone) * 2024))
    return new_stones


def part_1():
    stones = parse_input()
    for i in range(0, 25):
        new_stones = []
        for stone in stones:
            new_stones.extend(process_stone(stone))
        stones = new_stones
    print(f'Part 1: {len(stones)}')


def part_2():
    stones = {k: 1 for k in parse_input()}

    for _ in range(75):
        new_stones = {}
        for stone, count in stones.items():
            child_stones = process_stone(stone)
            for child_stone in child_stones:
                if child_stone in new_stones:
                    new_stones[child_stone] += count
                else:
                    new_stones[child_stone] = count
        stones = new_stones

    print(f'Part 2: {sum(stones.values())}')


start = current_milli_time()
part_1()
end = current_milli_time()
print(f'Took: {end - start}ms')

start = current_milli_time()
part_2()
end = current_milli_time()
print(f'Took: {end - start}ms')
