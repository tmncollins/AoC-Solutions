with open("inputs/Day7.txt") as f:
    all_data = f.read().split("\n")


class Files:

    def __init__(self):
        self.name = ""
        self.parent = None
        self.children = []

    def get_child(self, c):
        for child in self.children:
            if type(child) == Files:
                if child.name == c:
                    return child
        return self

    def size(self):
        size = 0
        for child in self.children:
            if type(child) == Files:
                size += child.size()
            else:
                size += child[1]
        return size

root = Files()
node = root

for line in all_data:
    if line == "": continue

    if line[0] == "$":
        line = line.split()
        if line[1] == "cd":
            if line[2] == "/":
                node = root
            elif line[2] == "..":
                node = node.parent
            else:
                node = node.get_child(line[2])
    else:
        line = line.split()
        if line[0] == "dir":
            f = Files()
            f.parent = node
            f.name = line[1]
            node.children.append(f)
        else:
            s = int(line[0])
            node.children.append((line[1], s))

# Part 1


def get_size(node):
    global part1, dirs

    size = 0
    for child in node.children:
        if type(child) == Files:
            size += get_size(child)
        else:
            size += child[1]

    if size <= 100000:
        part1 += size
    dirs.append(size)

#    print(node.name, size)

    return size


part1 = 0
dirs = []
tot_size = get_size(root)
print("Part 1:", part1)

req = tot_size - 40000000
#print(tot_size)
#print(req)
dirs = sorted(dirs)
#print(dirs)
for i in dirs:
    if i >= req:
        print("Part 2:", i)
        break

