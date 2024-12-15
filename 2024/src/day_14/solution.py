import re
import time

robot_pattern = r"[-]?\d+"
x_max = 101
y_max = 103
quadrants = {
    1: {'x': (0, x_max // 2 - 1), 'y': (0, y_max // 2 - 1)},
    2: {'x': (x_max // 2 + 1, x_max - 1), 'y': (0, y_max // 2 - 1)},
    3: {'x': (0, x_max // 2 - 1), 'y': (y_max // 2 + 1, y_max - 1)},
    4: {'x': (x_max // 2 + 1, x_max - 1), 'y': (y_max // 2 + 1, y_max - 1)}
}

robots = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        numbers = re.findall(robot_pattern, line)
        robots.append({
            'p': (int(numbers[0]), int(numbers[1])),
            'v': (int(numbers[2]), int(numbers[3]))}
        )

def print_robots():
    print("#############")
    for y in range(y_max):
        line = ""
        for x in range(x_max):
            count = len(list(filter(lambda r: r['p'] == (x, y), robots)))
            if count > 0:
                line += str(count)
            else:
                line += "."
        print(line)


def move_robot(robot):
    robot['p'] = (robot['p'][0] + robot['v'][0], robot['p'][1] + robot['v'][1])
    if robot['p'][0] < 0:
        robot['p'] = (x_max + robot['p'][0], robot['p'][1])
    if robot['p'][0] >= x_max:
        diff = robot['p'][0] - x_max
        robot['p'] = (diff, robot['p'][1])
    if robot['p'][1] < 0:
        robot['p'] = (robot['p'][0], y_max + robot['p'][1])
    if robot['p'][1] >= y_max:
        diff = robot['p'][1] - y_max
        robot['p'] = (robot['p'][0], diff)


def which_quadrant(x, y):
    for q_id, quadrant in quadrants.items():
        if quadrant['x'][0] <= x <= quadrant['x'][1] and quadrant['y'][0] <= y <= quadrant['y'][1]:
            return q_id
    return None


for _ in range(100):
    for robot in robots:
        move_robot(robot)
    print_robots()
    time.sleep(1)


counts = {1: 0, 2: 0, 3: 0, 4: 0}
for robot in robots:
    q_id = which_quadrant(robot['p'][0], robot['p'][1])
    if q_id:
        counts[q_id] += 1

total = 1
for v in counts.values():
    total = total * v
print(f'Part 1: {total}')
