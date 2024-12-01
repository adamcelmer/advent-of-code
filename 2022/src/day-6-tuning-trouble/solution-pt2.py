class InputProcessor():
    def __init__(self):
        self.index = 0
        self.elements = {}
    
    def add_element(self, new_element):
        self.index += 1
        # print(f'BEFORE: {self.elements}')
        if len(list(self.elements.keys())) < 14:
            self.elements[self.index % 14 if self.index % 14 > 0 else 14] = new_element
        else:
            for i in range(1, 14):
                self.elements[i] = self.elements[i + 1]
            self.elements[14] = new_element
        # print(f'AFTER: {self.elements}')

    def get_marker(self) -> list:
        potential_marker = set(self.elements.values())
        if len(potential_marker) == 14:
            return self.elements
        return None

    def get_index(self):
        return self.index

def parse_input() -> str:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        return lines[0]

input = parse_input()
processor = InputProcessor()

for char in input:
    processor.add_element(char)
    marker = processor.get_marker()
    if marker:
        index = processor.get_index()
        print(f'Marker found: {marker}, index: {index}')
        break
