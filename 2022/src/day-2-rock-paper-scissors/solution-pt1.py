score_total = 0

def map_choices(opponent, me):
    if opponent == "A":
        if me == "X":
            return 3
        if me == "Y":
            return 6
        return 0
    elif opponent == "B":
        if me == "X":
            return 0
        if me == "Y":
            return 3
        return 6
    elif opponent == "C":
        if me == "X":
            return 6
        if me == "Y":
            return 0
        return 3

def calculate_points(opponent, me):
    print(f'Calculating points for: opponent={opponent}, me={me}')
    points = 0
    if me == "X":
        points = 1
    elif me == "Y":
        points = 2
    elif me == "Z":
        points = 3
    points += map_choices(opponent, me)
    print(f'Calculated points: {points}')
    return points

with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        input_raw = line.split(" ")
        opponent = input_raw[0]
        me = input_raw[1]
        score_total += calculate_points(opponent, me)

print(f'Score total: {score_total}')