trees = []
highest_score = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        trees.append([int(x) for x in list(line)])

def get_top_visibility(i, j):
    counter = 0
    for x in range(i - 1, -1, -1):
        if trees[x][j] <= trees[i][j]:
            counter += 1
        if trees[x][j] >= trees[i][j]:
            break
    return counter

def get_bottom_visibility(i, j):
    counter = 0
    for x in range(i + 1, len(trees)):
        if trees[x][j] <= trees[i][j]:
            counter += 1
        if trees[x][j] >= trees[i][j]:
            break
    return counter

def get_left_visibility(i, j):
    counter = 0
    for x in range(j - 1, -1, -1):
        if trees[i][x] <= trees[i][j]:
            counter += 1
        if trees[i][x] >= trees[i][j]:
            break
    return counter

def get_right_visibility(i, j):
    counter = 0
    for x in range(j + 1, len(trees[0])):
        if trees[i][x] <= trees[i][j]:
            counter += 1
        if trees[i][x] >= trees[i][j]:
            break
    return counter

for i, line in enumerate(trees):
    for j, tree in enumerate(line):
        current_visibility_score = get_top_visibility(i, j) * get_bottom_visibility(i, j) * get_left_visibility(i, j) * get_right_visibility(i, j)
        if current_visibility_score > highest_score:
            print(f'New highest tree found: i={i}, j={j}, score={current_visibility_score}')
            highest_score = current_visibility_score

print(f'Best tree visibility score: {highest_score}')
