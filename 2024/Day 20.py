from functools import lru_cache
from time import time

def in_grid(pos):
    x,y = pos
    if x < 0 or y < 0 or x >= width or y >= height: return False
    return True

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

@lru_cache(maxsize=None)
def cheat(pos, t, part2=False):
    global directions, grid
    if t == 0:
        if grid[pos[1]][pos[0]] != "#":
            return {pos}
        return False
    ans = set()
    if part2 and grid[pos[1]][pos[0]] != "#": ans = {pos}
    for d in directions:
        v = (pos[0] + d[0], pos[1] + d[1])
        if in_grid(v):
            x = cheat(v, t-1, part2)
            if x:
                for item in x: ans.add(item)
    return ans


with open("inputs/Day20.txt", "r") as f:
    grid = f.read().split("\n")

width = len(grid[0])
height = len(grid)

end = (0,0)
start = (0,0)
for y in range(height):
    for x in range(width):
        if grid[y][x] == "E":
            end = (x,y)
        if grid[y][x] == "S":
            start = (x,y)

dist = dict()
dist[end] = 0
directions = [(0,1), (1,0), (-1,0), (0,-1)]
pos = end
while pos != start:
    for d in directions:
        v = (pos[0] + d[0], pos[1] + d[1])
        if grid[v[1]][v[0]] != "#" and v not in dist:
            dist[v] = dist[pos] + 1
            pos = v

part1 = 0
for pos in dist:
    cheats = cheat(pos, 2)
    for c in cheats:
        time_saved = dist[pos] - dist[c] - 2
        if time_saved >= 100:
            part1 += 1
#            print(pos, c, time_saved)
print("Part 1:", part1)

part2 = 0
start = time()
i = 0
for pos in dist:
    if i % 1000 == 0: print(i)
    cheats = cheat(pos, 20, True)
    for c in cheats:
        time_saved = dist[pos] - dist[c] - distance(pos, c)
        if time_saved >= 100:
            part2 += 1
    i += 1
print("Part 2:", part2)
print(time() - start)

part2 = set()
positions = list(dist.keys())
start = time()
for a in range(len(positions)):
    if a % 1000 == 0: print("At", a, "out of", len(positions))
    for b in range(a):
        posa = positions[a]
        posb = positions[b]
        if distance(posa, posb) <= 20:
            time_saved = dist[posa] - dist[posb]-distance(posa, posb)
            if time_saved >= 100:
                part2.add((min(posa,posb), max(posa,posb)))
#                print(posa, posb, time_saved)

print("Part 2:", len(part2))
print(time() - start)
