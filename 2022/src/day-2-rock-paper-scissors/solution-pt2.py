score_total = 0

def get_my_choice(opponent, expected_result):
    if opponent == "ROCK":
        if expected_result == "LOSE":
            return "SCISSORS"
        if expected_result == "DRAW":
            return "ROCK"
        return "PAPER"
    elif opponent == "PAPER":
        if expected_result == "LOSE":
            return "ROCK"
        elif expected_result == "DRAW":
            return "PAPER"
        return "SCISSORS"
    elif opponent == "SCISSORS":
        if expected_result == "LOSE":
            return "PAPER"
        elif expected_result == "DRAW":
            return "SCISSORS"
        return "ROCK"

def calculate_points(opponent, expected_result):
    print(f'Calculating points: opponent={opponent}, expected_result={expected_result}')
    points = 0
    me = get_my_choice(opponent, expected_result)
    print(f'I have to choose: {me}')
    if me == "ROCK":
        points = 1
    elif me == "PAPER":
        points = 2
    else:
        points = 3
    if expected_result == "DRAW":
        points += 3
    elif expected_result == "WIN":
        points += 6
    print(f'my points: {points}')
    return points

def map_to_choice(choice_raw):
    if choice_raw == "A":
        return "ROCK"
    elif choice_raw == "B":
        return "PAPER"
    return "SCISSORS"

def map_to_result(expected_result_raw):
    if expected_result_raw == "X":
        return "LOSE"
    elif expected_result_raw == "Y":
        return "DRAW"
    elif expected_result_raw == "Z":
        return "WIN"

with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        input_raw = line.split(" ")
        opponent = map_to_choice(input_raw[0])
        expected_result = map_to_result(input_raw[1])
        score_total += calculate_points(opponent, expected_result)

print(f'Score total: {score_total}')