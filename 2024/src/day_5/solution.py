def parse_input():
    ordering_rules = []
    updates = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line[:-1]
            if '|' in line:
                rule = line.split('|')
                ordering_rules.append((int(rule[0]), int(rule[1])))
            if ',' in line:
                updates.append([int(x) for x in line.split(',')])
    return ordering_rules, updates


def is_update_valid(ordering_rules: list[tuple[int, int]], update: list[int]) -> bool:
    visited_updates = []
    for page in update:
        for rule in ordering_rules:
            if rule[1] != page:
                continue
            if rule[0] in update and rule[1] in update and rule[0] not in visited_updates:
                return False
        visited_updates.append(page)
    return True


def part_1(ordering_rules: list[tuple[int]], updates: list[list[int]]):
    valid_updates = list(filter(lambda update: is_update_valid(ordering_rules, update), updates))
    total = 0
    for update in valid_updates:
        total = total + update[len(update) // 2]
    print(f'Part 1: {total}')


def get_expected_pages(ordering_rules: list[tuple[int]], update: list[int], page: int) -> list[int]:
    expected_pages = [r[0] for r in ordering_rules if r[1] == page]
    return [r for r in expected_pages if r in update]


def fix_order(ordering_rules: list[tuple[int]], update: list[int]) -> list[int]:
    pages_count = len(update)
    reordered = []
    while len(reordered) < pages_count:
        for page in update:
            expected_pages = get_expected_pages(ordering_rules, update + reordered, page)
            if expected_pages and len(expected_pages):
                all_expected_provided = True
                for e in expected_pages:
                    if e not in reordered:
                        all_expected_provided = False
                if all_expected_provided:
                    reordered.append(page)
                    update.remove(page)
            else:
                reordered.append(page)
                update.remove(page)
    return reordered


def part_2(ordering_rules: list[tuple[int]], updates: list[list[int]]):
    invalid_updates  = list(filter(lambda update: not is_update_valid(ordering_rules, update), updates))
    total = 0
    for update in invalid_updates:
        fixed_update = fix_order(ordering_rules, update)
        total = total + fixed_update[len(fixed_update) // 2]
    print(f'Part 2: {total}')


if __name__ == '__main__':
    ordering_rules, updates = parse_input()
    part_1(ordering_rules, updates)
    part_2(ordering_rules, updates)
