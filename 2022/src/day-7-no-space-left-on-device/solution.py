import re

class Directory:
    size_threshold = 100000
    size_total_under_threshold = 0
    sizes = {}
    
    def __init__(self, name: str, parent = None, level = 0) -> None:
        self.name = name
        self.size = 0
        self.level = level
        self.parent = parent
        self.children = dict()

    def add_child(self, name: str):
        self.children[name] = Directory(name=name, parent=self, level=self.level + 1)

    def add_file(self, file_size: int):
        self.size += file_size
        Directory.sizes[self.name] = self.size
        if self.parent is not None:
            self.parent.add_file(file_size)
    
    def go_down(self, name: str):
        return self.children[name]

    def go_up(self):
        return self.parent

    def print_size(self):
        if self.parent is None:
            Directory.size_total_under_threshold = 0
        if self.size <= Directory.size_threshold:
            Directory.size_total_under_threshold += self.size

        prefix = ""
        for i in range(0, self.level):
            prefix = prefix + "-"
        line = f'{prefix} {self.name}\t{self.size}'
        print(line)
        for child in self.children.values():
            child.print_size()

    def get_root(self):
        return self.parent.get_root() if self.parent is not None else self


dir = None
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        # print(line)
        if line == "$ cd /":
            dir = Directory(name="root", parent=None, level=0)
        elif line.startswith("dir "):
            dir_name = line.split(" ")[1]
            # print(f'Directory found: {dir_name}')
            dir.add_child(dir_name)
        elif re.match(r'\d+ .+', line):
            file_size = int(line.split(" ")[0])
            # print(f'File found. size: {file_size}')
            dir.add_file(file_size)
        elif line.startswith("$ cd "):
            dir_name = line.split(" ")[2]
            # print(f'Changing directory to: {dir_name}')
            dir = dir.go_up() if dir_name == ".." else dir.go_down(dir_name)

dir = dir.get_root()
dir.print_size()
print(f'Total size of dirs with size at most {Directory.size_threshold}: {Directory.size_total_under_threshold}')

# pt 2
total_size = Directory.sizes["root"]
unused_space = 70000000 - total_size
missing_space = 30000000 - unused_space
print(f'Total size: {total_size}, unused space: {unused_space}, missing space: {missing_space}')

dir_sizes_sorted = {k: v for k, v in sorted(Directory.sizes.items(), key=lambda item: item[1])}
for k, v in dir_sizes_sorted.items():
    if v > missing_space:
        print(f'{k}:\t{v}')