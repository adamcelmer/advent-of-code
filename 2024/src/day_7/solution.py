from dataclasses import dataclass

@dataclass
class Equation:
    expected_result: int
    elements: list[int]

    def __can_get_result(self, total, elements, with_concatenation=False):
        if total == self.expected_result:
            return True
        if not elements:
            return False
        concatenated_result = self.__can_get_result(int(f'{total}{elements[0]}'), elements[1:], with_concatenation=with_concatenation) if with_concatenation else False
        return (self.__can_get_result(total + elements[0], elements[1:], with_concatenation=with_concatenation)
                or self.__can_get_result(total * elements[0], elements[1:], with_concatenation=with_concatenation)
                or concatenated_result)


    def is_valid(self, with_concatenation=False) -> bool:
        concatenated_result = self.__can_get_result(int(f'{self.elements[0]}{self.elements[1]}'), self.elements[2:], with_concatenation=with_concatenation) if with_concatenation else False
        return self.__can_get_result(self.elements[0], self.elements[1:], with_concatenation=with_concatenation) or concatenated_result

    def print(self):
        print(f'expected_result: {self.expected_result}, elements: {self.elements}')


def parse_input() -> list[Equation]:
    equations = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            expected_result = int(line.split(':')[0])
            elements = [int(x) for x in line.split(':')[1].strip().split(' ')]
            equations.append(Equation(expected_result, elements))
    return equations


def part_1(equations: list[Equation]):
    total = 0
    for e in equations:
        if e.is_valid():
            total = total + e.expected_result
    print(f'Part 1: {total}')


def part_2(equations: list[Equation]):
    total = 0
    for e in equations:
        if e.is_valid(with_concatenation=True):
            total = total + e.expected_result
    print(f'Part 2: {total}')


if __name__ == '__main__':
    equations = parse_input()
    part_1(equations)
    part_2(equations)
