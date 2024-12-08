from collections import defaultdict

def print_board(board: list[list[str]]):
    for row in board:
        print("".join(row))


board = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        board.append(list(line))
max_row = len(board) - 1
max_col = len(board[0]) - 1

antenna_to_location = defaultdict(list)
for row in range(0, len(board)):
    for col in range(0, len(board[0])):
        point_value = board[row][col]
        if point_value != '.':
            antenna_to_location[point_value].append((row, col))

def is_point_on_board(point: tuple):
    return 0 <= point[0] <= max_row and 0 <= point[1] <= max_col

##########
# Part 1 #
##########
anti_nodes = set()
for antenna, locations in antenna_to_location.items():
    for i in range(0, len(locations) - 1):
        remaining_locations = locations[i + 1:]
        for r in remaining_locations:
            direction = (locations[i][0] - r[0], locations[i][1] - r[1])
            anti_node_1 = (locations[i][0] + direction[0], locations[i][1] + direction[1])
            anti_node_2 = (r[0] - direction[0], r[1] - direction[1])
            anti_nodes = anti_nodes | set(filter(is_point_on_board, [anti_node_1, anti_node_2]))

print(f'Part 1: {len(anti_nodes)}')

##########
# Part 2 #
##########
def get_all_points_in_line(point_1: tuple, point_2: tuple) -> set[tuple]:
    points_in_line = set()
    direction = (point_1[0] - point_2[0], point_1[1] - point_2[1])
    point = (point_1[0] + direction[0], point_1[1] + direction[1])
    while is_point_on_board(point):
        points_in_line.add(point)
        point = (point[0] + direction[0], point[1] + direction[1])
    point = (point_2[0] - direction[0], point_2[1] - direction[1])
    while is_point_on_board(point):
        points_in_line.add(point)
        point = (point[0] - direction[0], point[1] - direction[1])
    return points_in_line


anti_nodes_harmonic = set()
for antenna, locations in antenna_to_location.items():
    anti_nodes_harmonic.add(locations[-1])
    for i in range(0, len(locations) - 1):
        anti_nodes_harmonic.add(locations[i])
        remaining_locations = locations[i + 1:]
        for r in remaining_locations:
            points_in_line = get_all_points_in_line(locations[i], r)
            anti_nodes_harmonic = anti_nodes_harmonic | points_in_line

print(f'Part 2: {len(anti_nodes_harmonic)}')
