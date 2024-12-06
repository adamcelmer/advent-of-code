def parse_input() -> list[list[str]]:
    board = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = list(line)[:-1]
            board.append(list(line))
    return board


GUARD_DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}
GUARD_NEXT_DIRECTION = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}


def is_guard(o) -> bool:
    return o in GUARD_DIRECTIONS.keys()


def find_starting_point(board: list[list[str]]) -> tuple:
    for i, row in enumerate(board):
        for j, o in enumerate(row):
            if o in GUARD_DIRECTIONS.keys():
                return (i, j), o


def find_next_point_before_obstacle(board: list[list[str]], position: tuple, direction: tuple) -> [tuple, bool]:
    while True:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if next_position[0] < 0 or next_position[0] >= len(board) or next_position[1] < 0 or next_position[1] >= len(board[0]):
            if board[position[0]][position[1]] == '#':
                return (position[0] - direction[0], position[1] - direction[1]), True
            return position, False
        if board[next_position[0]][next_position[1]] == '#':
            return position, True
        position = next_position


def get_all_points_between(p1: tuple, p2: tuple):
    all_points = []
    if p1[0] == p2[0]:
        if p2[1] - p1[1] > 0:
            x = p2[1]
            while x >= p1[1]:
                all_points.append((p1[0], x))
                x = x - 1
        else:
            x = p2[1]
            while x <= p1[1]:
                all_points.append((p1[0], x))
                x = x + 1
    else:
        if p2[0] - p1[0] > 0:
            x = p2[0]
            while x >= p1[0]:
                all_points.append((x, p1[1]))
                x = x - 1
        else:
            x = p2[0]
            while x <= p1[0]:
                all_points.append((x, p1[1]))
                x = x + 1
    return all_points


def part_1(board: list[list[str]]):
    point, guard = find_starting_point(board)
    visited_positions = []
    direction = GUARD_DIRECTIONS[guard]
    obstacle_found = True
    while obstacle_found:
        next_point, obstacle_found = find_next_point_before_obstacle(board, point, direction)
        visited_positions = visited_positions + get_all_points_between(point, next_point)
        direction = GUARD_NEXT_DIRECTION[direction]
        point = next_point
    print(len(set(visited_positions)))


if __name__ == '__main__':
    board = parse_input()
    part_1(board)
    # part_2(ordering_rules, updates)