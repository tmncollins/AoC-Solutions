import heapq
from collections import defaultdict, deque

with open("inputs/Day16.txt", "r") as f:
    grid = f.read().split("\n")

start = (0,0)
target = (0,0)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            start = (x,y)
        if grid[y][x] == "E":
            target = (x,y)

def rotate_clockwise(d):
    return (-d[1], d[0])

def rotate_anticlockwise(d):
    return (d[1], -d[0])

q = [(0, start, (1,0))]
seen = {(start, (1,0)):0}
parents = defaultdict(set)

while q:
    dist, u, dir = heapq.heappop(q)
#    print(u, dir, dist)
    if u == target:
        print("Part 1:", dist)
        break
    v = (u[0] + dir[0], u[1] + dir[1])
    if grid[v[1]][v[0]] != "#":
        if (v, dir) not in seen or dist+1 <= seen[(v,dir)]:
            if (v, dir) not in seen or dist+1 < seen[(v,dir)]:
                seen[(v,dir)] = dist+1
                heapq.heappush(q, (dist+1,v,dir))
                parents[(v, dir)] = {(u, dir)}
            else:
                parents[(v, dir)].add((u, dir))
    d2 = rotate_clockwise(dir)
    if (u, d2) not in seen or dist+1000 <= seen[(u,d2)]:
        if (u, d2) not in seen or dist+1000 < seen[(u,d2)]:
            seen[(u,d2)] = dist+1000
            heapq.heappush(q, (dist+1000,u,d2))
            parents[(u,d2)] = {(u, dir)}
        else:
            parents[(u,d2)].add((u, dir))
    d2 = rotate_anticlockwise(dir)
    if (u, d2) not in seen or dist+1000 <= seen[(u,d2)]:
        if (u, d2) not in seen or dist + 1000 < seen[(u, d2)]:
            seen[(u,d2)] = dist+1000
            heapq.heappush(q, (dist+1000,u,d2))
            parents[(u,d2)] = {(u, dir)}
        else:
            parents[(u,d2)].add((u, dir))

def output():
    global grid, path
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid[y])):
            if grid[y][x] == "#": line += "#"
            elif (x,y) in path: line += "O"
            else: line += "."
        print(line)

path = set()
seen = set()
q = deque()
#print(parents)
q.append((target, (1,0)))
q.append((target, (-1,0)))
q.append((target, (0,1)))
q.append((target, (0,-1)))
while q:
#    print(len(q))
    u, d = q.popleft()
    path.add(u)
    if u == start: continue
    for item in parents[(u,d)]:
        if item not in seen:
            seen.add(item)
            q.append(item)

print("Part 2:", len(path))
#output()
