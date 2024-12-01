moves = []
# 0 == head
positions = {x: (0, 0) for x in range(0, 10)}
tail_positions = [(0, 0)]

with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        move = line.split(" ")
        moves.append((move[0], int(move[1])))

def move_head(direction):
    global positions
    (x, y) = positions[0]
    if direction == "U":
        positions[0] = (x, y + 1)
    elif direction == "D":
        positions[0] = (x, y - 1)
    elif direction == "L":
        positions[0] = (x - 1, y)
    elif direction == "R":
        positions[0] = (x + 1, y)

def calculate_direction(head_x, head_y, tail_x, tail_y):
    if abs(head_x - tail_x) > 1:
        if head_x < tail_x:
            return "L"
        return "R"
    else:
        if head_y < tail_y:
            return "D"
        return "U"

def follow_head(head_index):
    global positions
    global tail_positions
    (head_x, head_y) = positions[head_index]
    (tail_x, tail_y) = positions[head_index + 1]
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return
    if abs(x_diff) > 1 and abs(y_diff) > 1:
        positions[head_index + 1] = (head_x + 1 if head_x < tail_x else head_x - 1, head_y + 1 if head_y < tail_y else head_y - 1)
        return
    direction = calculate_direction(head_x, head_y, tail_x, tail_y)
    if direction == "U":
        positions[head_index + 1] = (head_x, head_y - 1)
    elif direction == "D":
        positions[head_index + 1] = (head_x, head_y + 1)
    elif direction == "L":
        positions[head_index + 1] = (head_x + 1, head_y)
    elif direction == "R":
        positions[head_index + 1] = (head_x - 1, head_y)

debug_counter = 0
for (direction, steps) in moves:
    for i in range(0, steps):
        move_head(direction)
        for j in range(0, 9):
            follow_head(j)
        tail_positions.append(positions[9])
        debug_counter += 1
        print(f'{debug_counter}-{direction}: {positions}')

print(f'Unique tail positions: {len(set(tail_positions))}')
