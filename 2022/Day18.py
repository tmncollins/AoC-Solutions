from _collections import *

with open("inputs/Day18.txt") as f:
    all_data = f.read().split("\n")

rocks = set()

min_x, min_y, min_z = float("inf"), float("inf"), float("inf")
max_x, max_y, max_z = 0, 0, 0

for line in all_data:
    if len(line) < 3: continue
    r = tuple(map(int, line.split(",")))
    min_x = min(min_x, r[0])
    max_x = max(max_x, r[0])
    min_y = min(min_y, r[1])
    max_y = max(max_y, r[1])
    min_z = min(min_z, r[2])
    max_z = max(max_z, r[2])
    rocks.add(r)


moves = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]

def surface_area(rocks):
    faces = len(rocks) * 6
    for r in rocks:
        for m in moves:
            if (r[0] + m[0], r[1] + m[1], r[2] + m[2]) in rocks:
                faces -= 1
    return faces

all_area =  surface_area(rocks)
print("Part 1:", all_area)

seen = set()
seen_outer = set()
for r in rocks:
    for m1 in moves:
        q = deque()
        start = (r[0] + m1[0], r[1] + m1[1], r[2] + m1[2])
        if start in seen or start in rocks: continue
        q.append(start)
        inner = True
        s = {start}
        while q and inner:
            u = q.popleft()
            print(u)
            for m in moves:
                v = (u[0] + m[0], u[1] + m[1], u[2] + m[2])
                if v in seen_outer or v[0] < min_x or v[1] < min_y or v[2] < min_z\
                        or v[0] > max_x or v[1] > max_y or v[2] > max_z:
                    inner = False
                    break
                elif v not in s and v not in rocks:
                    s.add(v)
                    q.append(v)

        if inner:
            print(s, surface_area(s))
            all_area -= surface_area(s)
        else:
            for i in s: seen_outer.add(i)

        for i in s: seen.add(i)

print(all_area)




