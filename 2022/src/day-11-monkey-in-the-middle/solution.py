import collections

# This differs between part-1 and part-2
worry_level_managed = False
iterations = 10000
common_multiple = 2 * 7 * 11 * 19 * 3 * 5 * 17 * 13

monkeys = collections.OrderedDict()
class Monkey:
    def __init__(self,name: str, items: list, operation, test):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.inspection_count = 0
    
    def add_item(self, item):
        self.items.append(item)
    
    def inspect(self):
        for i, item in enumerate(self.items):
            item = int(self.operation(item) / 3) if worry_level_managed else self.operation(item)
            item_recipient = self.test(item)
            monkeys[item_recipient].add_item(item % common_multiple)
            self.inspection_count += 1
        self.items = []
    
    def get_inspection_count(self):
        return self.inspection_count


# Print iterations progress - not related to the task at all
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()



monkey_0 = Monkey("monkey_0", [66, 59, 64, 51], lambda x: x * 3, lambda x: 1 if x % 2 == 0 else 4)
monkey_1 = Monkey("monkey_1", [67, 61], lambda x: x * 19, lambda x: 3 if x % 7 == 0 else 5)
monkey_2 = Monkey("monkey_2", [86, 93, 80, 70, 71, 81, 56], lambda x: x + 2, lambda x: 4 if x % 11 == 0 else 0)
monkey_3 = Monkey("monkey_3", [94], lambda x: x * x, lambda x: 7 if x % 19 == 0 else 6)
monkey_4 = Monkey("monkey_4", [71, 92, 64], lambda x: x + 8, lambda x: 5 if x % 3 == 0 else 1)
monkey_5 = Monkey("monkey_5", [58, 81, 92, 75, 56], lambda x: x + 6, lambda x: 3 if x % 5 == 0 else 6)
monkey_6 = Monkey("monkey_6", [82, 98, 77, 94, 86, 81], lambda x: x + 7, lambda x: 7 if x % 17 == 0 else 2)
monkey_7 = Monkey("monkey_7", [54, 95, 70, 93, 88, 93, 63, 50], lambda x: x + 4, lambda x: 2 if x % 13 == 0 else 0)

monkeys[0] = monkey_0
monkeys[1] = monkey_1
monkeys[2] = monkey_2
monkeys[3] = monkey_3
monkeys[4] = monkey_4
monkeys[5] = monkey_5
monkeys[6] = monkey_6
monkeys[7] = monkey_7

for i in range(0, iterations):
    for _, monkey in monkeys.items():
        monkey.inspect()
    printProgressBar(i, iterations, prefix="Progress: ", suffix="Completed", length=50)

inspection_counts = {i: monkey.get_inspection_count() for i, monkey in monkeys.items()}
inspection_counts_sorted = {k: v for k, v in sorted(inspection_counts.items(), key=lambda item: item[1], reverse=True)}
for i, count in inspection_counts_sorted.items():
    print(f'monkey_{i}: {count}')

top_2 = sorted(inspection_counts.values(), reverse=True)[:2]
print(top_2)
print(top_2[0] * top_2[1])