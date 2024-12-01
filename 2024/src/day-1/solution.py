#!python

def get_raw_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lists = ([], [])
        for line in lines:
            splitted = line.split()
            lists[0].append(int(splitted[0]))
            lists[1].append(int(splitted[1]))
        lists[0].sort()
        lists[1].sort()
        return lists


def part_1(lists):
    total = 0
    for i in range(0, len(lists[0])):
        total = total + abs(lists[1][i] - lists[0][i])
    print(total)


def part_2(lists):
    total = 0
    for i in range(0, len(lists[0])):
        n = lists[0][i]
        n_count = lists[1].count(n)
        total = total + n * n_count
    print(total)


if __name__ == '__main__':
    lists = get_raw_input()
    part_1(lists)
    part_2(lists)
