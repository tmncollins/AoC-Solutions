from _collections import *

data = open("Day9.txt").read().split("\n")

grid = [list(map(int, list(data[i]))) for i in range(len(data))]
dic = dict()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        dic[(x,y)] = grid[y][x]

def minimum(x, y):
    v = dic[(x,y)]
    if (x-1,y) in dic and dic[(x-1,y)] <= v: return 0
    if (x+1,y) in dic and dic[(x+1,y)] <= v: return 0
    if (x,y-1) in dic and dic[(x,y-1)] <= v: return 0
    if (x,y+1) in dic and dic[(x,y+1)] <= v: return 0

    return v + 1

tot = 0
pts = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        s = minimum(x,y)
        if s != 0:
            tot += s
            pts.append((x,y))

print("Part 1:", tot)

seen = set()
direct = [(-1, 0), (1, 0), (0, 1), (0, -1)]
basins = []
c = 0
for i in pts:
    q = deque()
    q.append(i)
    seen = set()
    seen.add(i)
    while q:
        x,y = q.popleft()
        for dx, dy in direct:
            p = (x + dx, y + dy)
            if p in dic and p not in seen and dic[p] < 9:
                seen.add(p)
                q.append(p)
    basins.append(len(seen))
    c += 1

basins = sorted(basins)
print("Part 2:", basins[-1] * basins[-2] * basins[-3])