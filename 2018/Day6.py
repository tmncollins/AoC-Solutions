from _collections import defaultdict

with open("input/6.txt") as f:
    points = f.readlines()

for i in range(len(points)):
    points[i] = list(map(int, points[i].replace("\n", "").split(",")))

GRID_W = 400
GRID_H = 400
grid = [[0 for i in range(GRID_W)] for _ in range(GRID_H)]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

inf = set()
for y in range(GRID_H):
    if y % 10 == 0: print(y)
    for x in range(GRID_W):
        MIN_D = 99999
        nearPoint = -1
        for i in range(len(points)):
            d = dist([x, y], points[i])
            if d < MIN_D:
                MIN_D = d
                nearPoint = i
            elif d == MIN_D:
                nearPoint = -1
        grid[y][x] = nearPoint
        if x == 0 or y == 0 or x == GRID_W -1 or y == GRID_H -1: inf.add(nearPoint)

counts = defaultdict(int)

for y in range(GRID_H):
    for x in range(GRID_W):
        if grid[x][y] >= 0 and not grid[x][y] in inf:
            counts[grid[x][y]] += 1

#print(counts)
print("Part 1:", max(counts.values()))

max_dist = 10000

area = 0
for y in range(GRID_H):
    if y % 10 == 0: print(y)
    for x in range(GRID_W):
        d = 0
        for point in points:
            d += dist([x,y], point)
        if d < max_dist:
            area += 1
print("Part 2:", area)