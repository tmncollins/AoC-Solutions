from _collections import *
import heapq

with open("input/18.txt") as f:
    all_data = f.read().split("\n")

grid = []
for line in all_data:
    if len(line) < 5 : continue
    grid.append(line)

start = (0, 0)
keys = dict()
doors = dict()
alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = alpha.upper()
free = set()
all_keys = ""

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != "#":
            free.add((x,y))
        if grid[y][x] == "@":
            start = (x,y)
        elif grid[y][x] in alpha:
            keys[grid[y][x]] = (x,y)
            all_keys += grid[y][x]
        elif grid[y][x] in ALPHA:
            doors[grid[y][x]] = (x,y)

all_keys = "".join(sorted(all_keys))
#print(all_keys)

pois = [start]
pois_idx = defaultdict(int)
pois_idx[start] = 1
for p in keys.values():
    pois.append(p)
    pois_idx[p] = len(pois)
for p in doors.values():
    pois.append(p)
    pois_idx[p] = len(pois)

graph = defaultdict(list)

move = [(0,1), (0,-1), (1,0), (-1,0)]

for p in pois:
    q = deque()
    q.append((p, 0))
    seen = {p}

    while q:
        u, d = q.popleft()
        if pois_idx[u] > 0 and d != 0:
            graph[pois_idx[p]].append((pois_idx[u], d))
            continue

        for m in move:
            v = (u[0] + m[0], u[1] + m[1])
            if v in free and v not in seen:
                seen.add(v)
                q.append((v, d+1))

# dijkstra to find shortest path
s = pois_idx[start]
q = [(0, s, "")]
seen = defaultdict(int)

while q:
    d, u, keys = heapq.heappop(q)

    if keys == all_keys:
        print("Part 1:", d)
        break

    for v, dist in graph[u]:
        poi_x, poi_y = pois[v-1]
        g = grid[poi_y][poi_x]
        new_keys = keys
        if g in alpha:
            if g not in new_keys:
                new_keys = "".join(sorted(new_keys + g)) # add key
        if g in ALPHA:
            if g.lower() not in keys:
                continue # cannot move here
        new_d = d + dist
        if seen[(v, new_keys)] == 0 or new_d < seen[(v, new_keys)]:
            seen[(v, new_keys)] = new_d
            heapq.heappush(q, (new_d, v, new_keys))
