trees = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        trees.append([int(x) for x in list(line)])

def is_visible_from_top(i, j, tree):
    for x in range(0, i):
        if trees[x][j] >= tree:
            return False
    return True

def is_visible_from_bottom(i, j, max_i, tree):
    for x in range(i + 1, max_i):
        if trees[x][j] >= tree:
            return False
    return True

def is_visible_from_left(i, j, tree):
    for x in range(0, j):
        if trees[i][x] >= tree:
            return False
    return True

def is_visible_from_right(i, j, max_j, tree):
    for x in range(j + 1, max_j):
        if trees[i][x] >= tree:
            return False
    return True

visible_trees = 0
for i, line in enumerate(trees):
    for j, tree in enumerate(line):
        if i == 0 or j == 0 or i == len(trees) - 1 or j == len(line) - 1:
            visible_trees += 1
            continue
        if is_visible_from_top(i, j, tree) or is_visible_from_bottom(i, j, len(trees), tree) or is_visible_from_left(i, j, tree) or is_visible_from_right(i, j, len(line), tree):
            visible_trees += 1

print(f'Visible trees: {visible_trees}')