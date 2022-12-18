from _collections import *
import heapq

with open("input/18.txt") as f:
    all_data = f.read().split("\n")

grid = []
for line in all_data:
    if len(line) < 5 : continue
    grid.append(line)

starts = set()
keys = dict()
doors = dict()
alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = alpha.upper()
free = set()
all_keys = ""


def update_grid():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                if grid[y][x+2] == "@": return # already updated

                grid[y-1] = list(grid[y-1])
                grid[y] = list(grid[y])
                grid[y+1] = list(grid[y+1])

                grid[y-1][x-1] = "@"
                grid[y-1][x+1] = "@"
                grid[y+1][x+1] = "@"
                grid[y+1][x-1] = "@"

                grid[y][x] = "#"
                grid[y-1][x] = "#"
                grid[y+1][x] = "#"
                grid[y][x-1] = "#"
                grid[y][x+1] = "#"

                grid[y-1] = "".join(grid[y-1])
                grid[y] = "".join(grid[y])
                grid[y+1] = "".join(grid[y+1])
                return


update_grid()

key_pos = dict()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != "#":
            free.add((x,y))
        if grid[y][x] == "@":
            starts.add((x,y))
        elif grid[y][x] in alpha:
            key_pos[grid[y][x]] = (x,y)
            keys[grid[y][x]] = (x,y)
            all_keys += grid[y][x]
        elif grid[y][x] in ALPHA:
            doors[grid[y][x]] = (x,y)

all_keys = "".join(sorted(all_keys))
#print(all_keys)

pois = []
pois_idx = defaultdict(int)
for p in starts:
    pois.append(p)
    pois_idx[p] = len(pois)
for p in keys.values():
    pois.append(p)
    pois_idx[p] = len(pois)
for p in doors.values():
    pois.append(p)
    pois_idx[p] = len(pois)

graph = defaultdict(list)

move = [(0,1), (0,-1), (1,0), (-1,0)]

key_required = defaultdict(list)

for p in pois:
    q = deque()
    q.append((p, 0, ""))
    seen = {p}

    while q:
        u, d, req = q.popleft()

        if pois_idx[u] > 0 and d != 0:
            g = grid[u[1]][u[0]]
            if g in alpha:
                # new key
                key_required[(pois_idx[p], pois_idx[u])].append((req, d))
                graph[pois_idx[p]].append((pois_idx[u], d))
            elif g in ALPHA:
                req += g

        for m in move:
            v = (u[0] + m[0], u[1] + m[1])
            if v in free and v not in seen:
                seen.add(v)
                q.append((v, d+1, req))

for line in grid:
    print(line)

# dijkstra to find shortest path
robots = []
for p in starts:
    robots.append(pois_idx[p])
robots = tuple(robots)
q = [(0, robots, "")]
seen = defaultdict(int)

t = 200

#print(key_required)

while q:
    d, robots, keys = heapq.heappop(q)
#    print(d, robots, keys)

    if d > seen[(robots, keys)]:
        continue

    if d > t:
        print(d, len(seen.keys()), len(q))
        t += 200

    if keys == all_keys:
        print("Part 2:", d)
        break

    for i in range(len(robots)):
#        print("robot", i)
        u = robots[i]
        not_got = ""
        for k in all_keys:
            if k not in keys:
                not_got += k

#        print(not_got)

        for k in not_got:
            v = pois_idx[key_pos[k]]
            if len(key_required[(u,v)]) == 0: continue
            new_keys = "".join(sorted(keys + k))
            new_robots = list(robots)
            new_robots[i] = v
            new_robots = tuple(new_robots)
#            print(key_required[(u, v)], u, v)
            for req, dist in key_required[(u, v)]:
#                print(req,dist)
                can_get = True
                for r in req.lower():
                    if r not in keys:
                        can_get = False
                        break

                if can_get:
#                    print("yes")
#                    print(seen, new_robots)
                    if seen[(new_robots, new_keys)] == 0 or d+dist < seen[(new_robots, new_keys)]:
#                        print("push")

                        seen[(new_robots, new_keys)] = d+dist
                        heapq.heappush(q, (d+dist, new_robots, new_keys))