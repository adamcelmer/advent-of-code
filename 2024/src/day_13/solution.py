import re
from time import time

from sympy import symbols, Eq, solve


def current_milli_time():
    return round(time() * 1000)

button_pattern = r"Button ([A-Z]): X\+(\d+), Y\+(\d+)"
prize_pattern = r"X=(\d+), Y=(\d+)"

def parse_input():
    with open('input.txt', 'r') as f:
        machines = []
        current_machine = {}
        for line in f.readlines():
            line = line.strip()
            if line == "":
                machines.append(current_machine)
                current_machine = {}
                continue
            if line.startswith("Button"):
                match = re.search(button_pattern, line)
                button = match.group(1)
                x = int(match.group(2))
                y = int(match.group(3))
                current_machine[button] = {'x': x, 'y': y}
            if line.startswith("Prize"):
                match = re.search(prize_pattern, line)
                x = int(match.group(1))
                y = int(match.group(2))
                current_machine['prize'] = {'x': x, 'y': y}
        if 'prize' in current_machine:
            machines.append(current_machine)
        return machines


machines = parse_input()


def get_cost(a_x, a_y, b_x, b_y, prize_x, prize_y):
    min_cost = None
    for a_depth in range(0, 101):
        for b_depth in range(0, 101):
            val_x = a_x * a_depth + b_x * b_depth
            val_y = a_y * a_depth + b_y * b_depth
            if val_x == prize_x and val_y == prize_y:
                cost = 3 * a_depth + b_depth
                if not min_cost:
                    min_cost = cost
                else:
                    min_cost = min(min_cost, cost)
    return min_cost

total_tokens = 0
for machine in machines:
    cost = get_cost(machine['A']['x'], machine['A']['y'],
                    machine['B']['x'], machine['B']['y'],
                    machine['prize']['x'],
                    machine['prize']['y'])
    if cost:
        total_tokens += cost

print(f'Part 1: {total_tokens}')


##############
### Part 2 ###
##############
def solve_equation(a_x, a_y, b_x, b_y, prize_x, prize_y):
    a, b = symbols('a b')
    eq_1 = Eq(a * a_x + b * b_x, prize_x)
    eq_2 = Eq(a * a_y + b * b_y, prize_y)
    solution = solve((eq_1, eq_2), (a, b))
    if 0 <= int(solution[a]) and 0 <= int(solution[b]) and solution[a].default_assumptions['integer'] and solution[b].default_assumptions['integer']:
        return int(solution[a]), int((solution[b]))
    return None, None

total_tokens = 0
for machine in machines:
    a_count, b_count = solve_equation(machine['A']['x'], machine['A']['y'],
                                  machine['B']['x'], machine['B']['y'],
                                  10000000000000 + machine['prize']['x'],
                                  10000000000000 + machine['prize']['y'])
    if a_count and b_count:
        total_tokens += 3 * a_count + b_count

print(f'Part 2: {total_tokens}')
