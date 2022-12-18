
with open("input/8.txt") as f:
    data = list(map(int, f.readline().replace("\n", "").split()))

class node:
    def __init__(self):
        self.meta_entries = []
        self.child_nodes = []
        self.meta_sum = 0
        self.child_num = 0
        self.meta_num = 0

    def addMetaEntry(self, entry):
        self.meta_entries.append(entry)
        self.meta_sum += entry

    def addChild(self, n):
        self.child_nodes.append(n)

root = node()
ptr = 0

def makeTree(n):
    global ptr
    n.child_num = data[ptr]
    n.meta_num = data[ptr + 1]
    ptr += 2

    #children
    for i in range(n.child_num):
        n2 = node()
        n.addChild(n2)
        makeTree(n2)

    #metadata
    for i in range(n.meta_num):
        n.addMetaEntry(data[ptr])
        ptr += 1

def sumMeta(n):
    tot = n.meta_sum
    for n2 in n.child_nodes:
        tot += sumMeta(n2)
    return tot

def part1(root):
    tot = sumMeta(root)
    print("Part 1:", tot)

def value(n):
    if n.child_num > 0:
        v = 0
        for m in n.meta_entries:
            m -= 1
            if m >= 0 and m < n.child_num:

                v += value(n.child_nodes[m])
        return v
    else: return n.meta_sum

def part2(root):
    tot = value(root)
    print("Part 2:", tot)

makeTree(root)
part1(root)
part2(root)