from collections import deque
from math import ceil

def in_grid(u):
    x,y = u
    if x < 0 or y < 0 or x > width or y > height: return False
    return True

def output():
    for y in range(height+1):
        line = ""
        for x in range(width+1):
            if grid[y][x] == 1:
                line += "#"
            else:
                line += "."
        print(line)

def bfs(start, end):
    q = deque()
    q.append((0,start))
    seen = {start}
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    while q:
        dist,u = q.popleft()
        for d in directions:
            v = (u[0] + d[0], u[1] + d[1])
            if in_grid(v) and v not in seen and grid[v[1]][v[0]] == 0:
                seen.add(v)
                if v == end: return dist+1
                q.append((dist+1, v))
    return -1

def reset(t):
    global grid
    grid = [[0 for _ in range(width+1)] for _ in range(height+1)]

    for i in range(t):
        x,y = list(map(int, bytes[i].split(",")))
        grid[y][x] = 1

with open("inputs/Day18.txt", "r") as f:
    bytes = f.read().split("\n")

width = 70
height = 70
target = (width, height)

reset(1024)
print("Part 1:", bfs((0,0), target))
#output()

lower = 1024
upper = len(bytes)

while lower < upper:
    middle = ceil((lower + upper) / 2)
    reset(middle)
    if bfs((0,0), target) == -1:
        upper = middle - 1
    else:
        lower = middle
#    print(lower, upper)
print("Part 2:", bytes[lower])

#reset(len(bytes))
#output()