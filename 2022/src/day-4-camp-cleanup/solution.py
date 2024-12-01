full_overlaps = 0
partial_overlaps = 0

with open('input.txt', 'r') as file:
    for line in file:
        print("########")
        line = line.rstrip('\n')
        elf_1 = line.split(",")[0]
        elf_2 = line.split(",")[1]
        elf_1_start = int(elf_1.split("-")[0])
        elf_1_end = int(elf_1.split("-")[1])
        elf_2_start = int(elf_2.split("-")[0])
        elf_2_end = int(elf_2.split("-")[1])
        print(f'elf_1={elf_1}, elf_2={elf_2}')
        # print(f'elf_1_start={elf_1_start}, elf_1_end={elf_1_end}, elf_2_start={elf_2_start}, elf_2_end={elf_2_end}')
        if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_2_start <= elf_1_start and elf_2_end >= elf_1_end):
            # print("Full overlap found")
            full_overlaps += 1
        
        elf_1_range = set(range(elf_1_start, elf_1_end + 1))
        elf_2_range = set(range(elf_2_start, elf_2_end + 1))
        common_elements = elf_1_range.intersection(elf_2_range)
        if len(common_elements) > 0:
            partial_overlaps += 1
            print("Partial overlap found")
            print(f'elf_1_range: {elf_1_range}, elf_2_range={elf_2_range}')

print(f'Full overlaps: {full_overlaps}')
print(f'Partial overlaps: {partial_overlaps}')