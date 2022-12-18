
with open("input/25.txt") as f:
    all_data = f.read().split("\n")

def dist(a, b):
    d = 0
    for i in range(len(a)):
        d += abs(a[i] - b[i])
    return d


class union_merge:

    def __init__(self, size):
        self.arr = [i for i in range(size)]

    def get_parent(self, i):
        if self.arr[i] == i: return i
        parent = self.get_parent(self.arr[i])
        self.arr[i] = parent
        return parent

    def merge(self, a, b):
        parent_a = self.get_parent(a)
        parent_b = self.get_parent(b)
        self.arr[parent_a] = parent_b

stars = []
for line in all_data:
    if len(line) < 5: continue
    star = list(map(int, line.strip().split(",")))
    stars.append(star)

constellations = union_merge(len(stars))

for a in range(len(stars)):
    for b in range(a):
        if dist(stars[a], stars[b]) <= 3:
            constellations.merge(a, b)

cnt = set()
for i in range(len(stars)):
    cnt.add(constellations.get_parent(i))

print("Part 1:", len(cnt))