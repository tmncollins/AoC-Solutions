from collections import deque

with open("inputs/Day12.txt", "r") as f:
    grid = f.read().split("\n")


Y = len(grid)
X = len(grid[0])
seen = set()

def in_grid(pos):
    x,y = pos
    if x < 0 or y < 0 or x >= X or y >= Y: return False
    return True

def bfs(start):
    global seen
    area = 0
    perimeter = 0
    q = deque()
    q.append(start)
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    seen.add(start)
    region = [start]
    edges = set()
    while q:
        u = q.pop()
        area += 1
        for d in directions:
            v = (d[0] + u[0], d[1] + u[1])
            if in_grid(v) and grid[v[1]][v[0]] == grid[u[1]][u[0]]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
                        region.append(v)
            else:
                perimeter += 1
                edges.add((u, d))
#    print(grid[start[1]][start[0]], area, perimeter, area*perimeter)
    return area, perimeter, sorted(region), edges

def sides(edges):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    sides = 0
    while edges:
        for start in edges:
            q = deque()
            q.append(start)
            side = {start}
            if start[1][0] == 0: perp = (1, 0)
            else: perp = (0, 1)
            while q:
                u, d = q.popleft()
                v1 = (u[0] + perp[0], u[1] + perp[1])
                v2 = (u[0] - perp[0], u[1] - perp[1])
                if (v1, d) in edges and (v1, d) not in side:
                    side.add((v1, d))
                    q.append((v1, d))
                if (v2, d) in edges and (v2, d) not in side:
                    side.add((v2, d))
                    q.append((v2, d))

            sides += 1
            for item in side: edges.remove(item)
            break
    return sides

def score():
    global seen
    seen = set()
    ans1 = 0
    ans2 = 0
    for y in range(Y):
        for x in range(X):
            if (x,y) not in seen:
                a, p, r, e = bfs((x,y))
                ans1 += a*p
                s = sides(e)
                ans2 += a*s
    return ans1, ans2

p1, p2 = score()
print("Part 1:", p1)
print("Part 2:", p2)
