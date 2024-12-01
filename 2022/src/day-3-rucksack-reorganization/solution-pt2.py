priority_total = 0

def get_priority(item: str):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

with open('input.txt', 'r') as file:
    elf_group = []
    for i, line in enumerate(file, 1):
        if i % 3 == 1:
            elf_group = []
        line = line.rstrip('\n')
        items = set(line)
        elf_group.append(items)
        if len(elf_group) == 3:
            # print(f'Elf group:')
            # print(elf_group)
            common_item = list(elf_group[0].intersection(elf_group[1]).intersection(elf_group[2]))[0]
            # print(f'Common item: {common_item}')
            priority = get_priority(common_item)
            # print(f'Priority: {priority}')
            priority_total += priority

print(f'Total priority: {priority_total}')
