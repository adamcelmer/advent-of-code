class InputProcessor():
    def __init__(self):
        self.index = 0
        self.elements = {}
    
    def add_element(self, new_element):
        self.index += 1
        # print(f'BEFORE: {self.elements}')
        if len(set(self.elements.keys())) < 4:
            self.elements[self.index % 4 if self.index % 4 > 0 else 4] = new_element
        else:
            self.elements[1] = self.elements[2]
            self.elements[2] = self.elements[3]
            self.elements[3] = self.elements[4]
            self.elements[4] = new_element
        # print(f'AFTER: {self.elements}')

    def get_marker(self) -> list:
        potential_marker = set(self.elements.values())
        if len(potential_marker) == 4:
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
