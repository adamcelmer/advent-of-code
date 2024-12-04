def parse_input():
    lines = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            letters = list(filter(lambda l: l != '\n', list(line)))
            lines.append(letters)
    return lines


def is_xmas(lines: list[list[chr]], row: int, col: int, word: list[chr], direction: tuple) -> int:
    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1
    if len(word) == 4 and ''.join(word) == 'XMAS':
        return 1
    if len(word) == 3 and ''.join(word) != 'XMA':
        return 0
    if len(word) == 2 and ''.join(word) != 'XM':
        return 0
    if len(word) == 1 and word[0] != 'X':
        return 0
    if direction:
        next_row = row + direction[0]
        next_col = col + direction[1]
        if next_row < 0 or next_row > max_row or next_col < 0 or next_col > max_col:
            return 0
        return is_xmas(lines, next_row, next_col, word + [lines[next_row][next_col]], direction)
    inner_total = 0
    for next_row in range(row - 1, row + 2):
        if next_row < 0 or next_row > max_row:
            continue
        for next_col in range(col - 1, col + 2):
            if next_col < 0 or next_col > max_col:
                continue
            inner_total = inner_total + is_xmas(lines, next_row, next_col, word + [lines[next_row][next_col]], (next_row - row, next_col - col))
    return inner_total


def part_1(lines):
    xmas_count = 0
    for row in range(0, len(lines)):
        for col in range(0, len(lines[0])):
            xmas_count = xmas_count + is_xmas(lines, row, col, [lines[row][col]], None)
    return xmas_count


if __name__ == '__main__':
    lines = parse_input()
    print(part_1(lines))
