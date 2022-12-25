from _collections import *
import time

alpha = "abcdefghijklmnopqrstuvwxyz"
conv = dict()
for i in range(len(alpha)):
    conv[alpha[i]] = i

with open("inputs/Day12.txt") as f:
    all_data = f.read().split("\n")

grid = []
target, start = (0, 0), (0, 0)
start_a = set()

for y in range(len(all_data)):
    if len(all_data[y]) < 4: continue
    line = []
    for x in range(len(all_data[y])):
        c = all_data[y][x]
        if c in alpha:
            if c == "a":
                start_a.add((len(line), len(grid)))
            line.append(conv[c])
        elif c == "E":
            target = (len(line), len(grid))
            line.append(25)
        elif c == "S":
            start = (len(line), len(grid))
            line.append(0)

    grid.append(line)


def bfs(start, targets, part2 = False):

    q = deque()
    q.append((start, 0))
    seen = {start}
    move = [(0,1), (1,0), (-1,0), (0,-1)]
#    print(start, target)

    while q:
        u, d = q.popleft()
        if u in targets:
            return d

        for m in move:
            v = (u[0] + m[0], u[1] + m[1])
            if v[0] < 0 or v[1] < 0 or v[1] >= len(grid) or v[0] >= len(grid[v[1]]): continue

            if not part2:
                if v not in seen and grid[v[1]][v[0]] <= grid[u[1]][u[0]] + 1:
                    seen.add(v)
                    q.append((v, d+1))

            else:
                if v not in seen and grid[v[1]][v[0]] >= grid[u[1]][u[0]] - 1:
                    seen.add(v)
                    q.append((v, d+1))

    return float("inf")


print("Part 1:", bfs(start, {target}))
print("Part 2:", bfs(target, start_a, True))