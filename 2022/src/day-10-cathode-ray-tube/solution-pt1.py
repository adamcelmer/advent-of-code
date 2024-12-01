import collections

cycles = collections.OrderedDict()

with open('input.txt', 'r') as file:
    cycle_no = 1
    for line in file:
        line = line.rstrip('\n')
        if line == "noop":
            cycles[cycle_no] = 0
            cycle_no += 1
        else:
            cycle = line.split(" ")
            cycles[cycle_no] = 0
            cycles[cycle_no + 1] = int(cycle[1])
            cycle_no += 2

register_x = 1
signal_strength_sum = 0
for cycle_no, increment in cycles.items():
    if cycle_no in [20, 60, 100, 140, 180, 220]:
        signal_strength_sum += cycle_no * register_x
    register_x += increment

print(f'signal_strength_sum = {signal_strength_sum}')
