from _collections import deque

with open("inputs/Day10.txt", "r") as f:
    grid = f.read().split("\n")

Y = len(grid)
X = len(grid[0])

def in_grid(pos):
    x,y = pos
    if x < 0 or y < 0 or x >= X or y >= Y: return False
    return True

def count_trails(start, part2=False):
    ends = set()
    p2 = 0
    q = deque()
    q.append(start)
    directions = [(-1,0), (0,-1), (1,0), (0,1)]
    while q:
        u = q.popleft()
        if grid[u[1]][u[0]] == "9":
            ends.add(u)
            p2 += 1
            continue
        for d in directions:
            v = (u[0] + d[0], u[1] + d[1])
            if in_grid(v):
                if int(grid[u[1]][u[0]]) + 1 == int(grid[v[1]][v[0]]):
                    q.append(v)
    if part2:
        return p2
    return len(ends)

part1 = 0
part2 = 0
for y in range(Y):
    for x in range(X):
        if grid[y][x] == "0":
            part1 += count_trails((x,y))
            part2 += count_trails((x,y), True)
print("Part 1:", part1)
print("Part 2:", part2)

