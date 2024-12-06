def parse_input() -> list[list[str]]:
    board = []
    with open('input-demo.txt', 'r') as f:
        for line in f.readlines():
            board.append(list(line))
    return board


GUARD_UP = '^'
GUARD_DOWN = 'v'
GUARD_LEFT = '<'
GUARD_RIGHT = '>'


def is_guard(o) -> bool:
    return o in [GUARD_UP, GUARD_DOWN, GUARD_LEFT, GUARD_RIGHT]


def find_starting_point(board: list[list[str]]) -> tuple:
    for i, row in enumerate(board):
        for j, o in enumerate(row):
            if o in [GUARD_UP, GUARD_DOWN, GUARD_LEFT, GUARD_RIGHT]:
                return (i, j), o


def find_point_next_to_obstruction(board: list[list[str]], position: tuple, direction: tuple) -> tuple:
    steps = 0
    while True:
        nex_position = (position[0] + direction[0], position[1] + direction[1])
        if nex_position[0] < 0 or nex_position[0] > len(board) or nex_position[1] < 0 or nex_position[1] > len(board[0]):
            return position
        if nex_position == '#':
            return nex_position



def part_1(board: list[list[str]]):
    visited_positions = set()
    starting_point, guard = find_starting_point(board)
    visited_positions.add(starting_point)


if __name__ == '__main__':
    board = parse_input()
    part_1(board)
    # part_2(ordering_rules, updates)