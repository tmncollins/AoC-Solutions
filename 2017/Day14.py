from _collections import *
from itertools import *

with open("inputs/14.txt") as f:
    all_data = f.read().strip()

def run(lengths):
    global string, skip, ret
    string = deque(string)

    for l in lengths:

        s1, s2 = deque(islice(string, 0, l)), deque(islice(string, l, len(string)))
        s1.reverse()
        string = s1 + s2
        x = skip + l
        string.rotate(-x)
        ret = (ret + x) % len(string)
        skip += 1

def hash(lengths):
    global string, skip, ret
    string = [i for i in range(256)]
    skip = 0
    ret = 0
    lengths += [17, 31, 73, 47, 23]

    for i in range(64):
        run(lengths)

    string.rotate(ret)

    sparse = []
    for i in range(len(string) // 16):
        x = 0
        for j in range(16):
            x = x ^ string[i*16 + j]
        sparse.append(x)

    h = ""
    hex = "0123456789abcdef"

    for i in sparse:
        a = i // 16
        b = i % 16
        h += hex[a] + hex[b]

    return h


used = 0
grid = set()

for row in range(128):
    s = all_data + "-" + str(row)
    lengths = [ord(i) for i in s]
    h = hash(lengths)
    h = int(h, 16)
    h = bin(h)[2:]
    used += h.count("1")
    h = h[::-1]
    for x in range(len(h)):
        if h[x] == "1":
            grid.add((x, row))

print("Part 1:", used)

seen = set()
move = [(1,0), (0,1), (-1,0), (0,-1)]
groups = 0

for item in grid:
    if item in seen: continue

    seen.add(item)
    q = deque()
    q.append(item)
    groups += 1

    while q:
        u = q.popleft()

        for m in move:
            v = (u[0] + m[0], u[1] + m[1])
            if v in grid and v not in seen:
                seen.add(v)
                q.append(v)

print("Part 2:", groups)