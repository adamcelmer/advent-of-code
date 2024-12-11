with open('input.txt', 'r') as f:
    board = []
    for line in f.readlines():
        line = [int(x) for x in list(line.strip())]
        board.append(line)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_on_the_map(row, col, board):
    row_max = len(board)
    col_max = len(board[0])
    return 0 <= row < row_max and 0 <= col < col_max


def find_all_peaks(row, col, board, visited, is_distinct):
    if board[row][col] == 9:
        if not is_distinct:
            visited.add((row, col))
        return 1

    if not is_distinct:
        visited.add((row, col))

    total = 0
    for dx, dy in directions:
        next_point = (row + dx, col + dy)
        if is_on_the_map(next_point[0], next_point[1], board) \
                and next_point not in visited \
                and board[next_point[0]][next_point[1]] - board[row][col] == 1:
            total = total + find_all_peaks(row + dx, col + dy, board, visited, is_distinct)
    return total


def calculate_score(row, col, board, is_distinct=False) -> int:
    return find_all_peaks(row, col, board, set(), is_distinct)


the_total = 0
for row_idx, row in enumerate(board):
    for col_idx, val in enumerate(row):
        if val == 0:
            the_total = the_total + calculate_score(row_idx, col_idx, board)
print(f'Part 1: {the_total}')

the_total = 0
for row_idx, row in enumerate(board):
    for col_idx, val in enumerate(row):
        if val == 0:
            the_total = the_total + calculate_score(row_idx, col_idx, board, True)
print(f'Part 2: {the_total}')