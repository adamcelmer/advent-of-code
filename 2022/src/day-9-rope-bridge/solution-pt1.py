moves = []
head_position = (0, 0)
tail_position = (0, 0)
tail_positions = [(0, 0)]

with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        move = line.split(" ")
        moves.append((move[0], int(move[1])))

def move_head(direction):
    global head_position
    (x, y) = head_position
    if direction == "U":
        head_position = (x, y + 1)
    elif direction == "D":
        head_position = (x, y - 1)
    elif direction == "L":
        head_position = (x - 1, y)
    elif direction == "R":
        head_position = (x + 1, y)

def follow_head(direction):
    global head_position
    global tail_position
    global tail_positions
    (head_x, head_y) = head_position
    (tail_x, tail_y) = tail_position
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        if direction == "U":
            tail_position = (head_x, head_y - 1)
        elif direction == "D":
            tail_position = (head_x, head_y + 1)
        elif direction == "L":
            tail_position = (head_x + 1, head_y)
        elif direction == "R":
            tail_position = (head_x - 1, head_y)
    tail_positions.append(tail_position)
    

for (direction, steps) in moves:
    for i in range(0, steps):
        move_head(direction)
        follow_head(direction)
        # print(f'Head: {head_position}')
        # print(f'Tail: {tail_position}')

print(f'Unique tail positions: {len(set(tail_positions))}')
