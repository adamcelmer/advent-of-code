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
sprite = [0, 1 ,2]
lines = []
line = ""
for crt, increment in cycles.items():
    line_no = int(crt / 40) + 1
    pixel_no = (crt % 40)
    register_x += increment
    sprite = [register_x - 1, register_x, register_x + 1]
    if pixel_no in sprite:
        line = line + "#"
    else:
        line = line + "."
    if pixel_no == 39:
        lines.append(line)
        line = ""

for line in lines:
    print(line)

