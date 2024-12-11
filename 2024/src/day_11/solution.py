def parse_input():
    with open('input-demo.txt', 'r') as f:
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

part_1()
