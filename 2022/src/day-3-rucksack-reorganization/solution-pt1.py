priority_total = 0

def get_priority(item: str):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        items = list(line)
        # print(f'Items: {items}')
        rucksack_1 = items[:len(items)//2]
        rucksack_2 = items[len(items)//2:]
        # print(f'Rucksack 1: {rucksack_1}')
        # print(f'Rucksack 2: {rucksack_2}')
        common_item = list(set(rucksack_1).intersection(rucksack_2))[0]
        # print(f'Common item: {common_item}')
        priority = get_priority(common_item)
        # print(f'Priority: {priority}')
        priority_total += priority

print(f'Total priority: {priority_total}')