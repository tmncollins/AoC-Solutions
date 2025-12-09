f = open('inputs/Day8.txt', 'r').read().strip().split('\n')
from collections import defaultdict
from math import sqrt, prod
from time import time

t = time()

class UnionFind:

    def __init__(self, size):
        self.parents = [i for i in range(size+1)]

    def get_parent(self, i):
        if self.parents[i] == i: return i
        p = self.get_parent(self.parents[i])
        self.parents[i] = p
        return p

    def union(self, a, b):
        a = self.get_parent(a)
        b = self.get_parent(b)
        self.parents[b] = a

    def sizes(self):
        s = defaultdict(int)
        for i in range(len(self.parents)):
            p = self.get_parent(i)
            s[p] += 1
        return s

def distance2(a, b):
    d = 0
    for i in range(3):
        d += (a[i] - b[i]) ** 2
    return d

distances = []

for i in range(len(f)):
    f[i] = list(map(int, f[i].split(',')))

for i in range(len(f)):
    a = f[i]
    for j in range(i):
        b = f[j]
        d = distance2(a, b)
        distances.append((d, i, j))

uf = UnionFind(len(f))
distances = sorted(distances)
for i in range(1000):
    d, a, b = distances[i]
    uf.union(a, b)

s = uf.sizes()
values = sorted(list(s.values()))
print('Part 1:', values[-1] * values[-2] * values[-3])

uf = UnionFind(len(f))
idx = 0
circuits = len(f)
while True:
    d, a, b = distances[idx]
    if uf.get_parent(a) != uf.get_parent(b):
        circuits -= 1
        if circuits == 1:
            xa = f[a][0]
            xb = f[b][0]
            print('Part 2:', xa * xb)
            break
    uf.union(a, b)
    idx += 1




