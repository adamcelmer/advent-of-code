import operator

elves = {}

with open('input.txt') as f:
    elf_no = 1
    sum = 0
    for line in f:
        calories = line.rstrip('\n')
        if line == "" or line == "\n":
            elves[elf_no] = sum
            sum = 0
            elf_no = elf_no + 1
            continue
        sum += int(calories)
    elves[elf_no] = sum

elves = dict(sorted(elves.items(), key=operator.itemgetter(1), reverse=True))

elves_list=list(elves.items())
fattest_elves = [elves_list[0], elves_list[1], elves_list[2]]
print(f'3 fattest elves: {fattest_elves}')

cal_sum = elves_list[0][1] + elves_list[1][1] + elves_list[2][1]
print(f'Their calories summary: {cal_sum}')
# print(elves[0])
# print(elves[1])
# print(elves[2])