from heapq import *
from _collections import *
import time

# still need to get score of 20
scores = [3,0,0,12,0,30,7,16,18,60,
          121,0,13,98,0,48,102,0,228,40,
          21,0,0,72,50,182,0,112,0,420
         ]

start = time.time()

def can_build(robot, ore, clay, obsidian):
    arr = [ore, clay, obsidian]
    for i in range(len(robot)):
        if robot[i] > arr[i]:
            return False
    return True


def get_factor(ng, g, t):
    # f is number of geodes + expected number of geodes
    # assume we can make a geode every other go
    x = t//2
    tri = (x) * (x+1)
    f = ng + t*g + tri

    return f


def max_geodes(r_ore, r_clay, r_obsidian, r_geode):
    # factor, num_geode, geode, num_obsidian, obsidian, num_clay, clay, num_ore, ore, min
    q = [(0, 0, 0, 0, 0, 0, 0, 0, 1, 24)]
    geodes = 0
    seen = OrderedDict()
    MAX_SIZE = 1e7
    cnt = 0
    max_ore = 0
    max_clay = 0
    max_obsidian = 0
    robots = [r_ore, r_clay, r_obsidian, r_geode]
    for i in range(4):
        max_ore = max(max_ore, robots[i][0])
        max_clay = max(max_clay, robots[i][1])
        max_obsidian = max(max_obsidian, robots[i][2])

    while q:
        f, ng, g, no, o, nc, c, nore, ore, t = heappop(q)
#        print(f, ng, g, no, o, nc, c, nore, ore, 24-t)

        cnt += 1
        if cnt % 1000000 == 0:
            print(len(seen), len(q))

        # no need to build a new robot on the final turn, that would be silly
        if t == 1:
            return ng + g

#        print(t)

        ng += g
        no += o
        nc += c
        nore += ore
        t -= 1

        # make each robot type
        # make an ore robot:
        # no need if we are already producing max clay each turn
        if o < max_ore and can_build(r_ore, nore, nc, no):
            v = (-get_factor(ng, g, t), ng, g, no-r_ore[2], o, nc-r_ore[1], c, nore-r_ore[0]-1, ore+1, t)
            v2 = (ng, g, no-r_ore[2], o, nc-r_ore[1], c, nore-r_ore[0]-1, ore+1)
            if v2 not in seen:
                seen[v2] = 0
                heappush(q, v)

        # make a clay robot
        # no need if we are already producing max clay each turn
        if c < max_clay and can_build(r_clay, nore, nc, no):
            v = (-get_factor(ng, g, t), ng, g, no-r_clay[2], o, nc-r_clay[1]-1, c+1, nore-r_clay[0], ore, t)
            v2 = (ng, g, no-r_clay[2], o, nc-r_clay[1]-1, c+1, nore-r_clay[0], ore)
            if v2 not in seen:
                seen[v2] = 0
                heappush(q, v)

        # make an obsidian robot
        # no need if we are already producing max clay each turn
        if o < max_obsidian and can_build(r_obsidian, nore, nc, no):
            v = (-get_factor(ng, g, t), ng, g, no-r_obsidian[2]-1, o+1, nc-r_obsidian[1], c, nore-r_obsidian[0], ore, t)
            v2 = (ng, g, no-r_obsidian[2]-1, o+1, nc-r_obsidian[1], c, nore-r_obsidian[0], ore)
            if v2 not in seen:
                seen[v2] = 0
                heappush(q, v)

        # make a geode robot
        if can_build(r_geode, nore, nc, no):
            v = (-get_factor(ng-1, g+1, t), ng-1, g+1, no-r_geode[2], o, nc-r_geode[1], c, nore-r_geode[0], ore, t)
            v2 = (ng-1, g+1, no-r_geode[2], o, nc-r_geode[1], c, nore-r_geode[0], ore)
            if v2 not in seen:
                seen[v2] = 0
                heappush(q, v)

        # build nothing
        v = (-get_factor(ng, g, t), ng, g, no, o, nc, c, nore, ore, t)
        v2 = (ng, g, no, o, nc, c, nore, ore)
        if v2 not in seen:
            seen[v2] = 0
            heappush(q, v)

        to_del = []
        for element in seen:
            if len(seen) - len(to_del) > MAX_SIZE:
                to_del.append(element)
            else:
                break
        for element in to_del:
            seen.pop(element)


with open("inputs/Day19.txt") as f:
    all_data = f.read().strip().split("\n")

part1 = 0
for line in all_data:
    if len(line) < 5: continue

    line = line.split()
    id = int(line[1].replace(":", ""))

    r_ore = [int(line[6]), 0, 0]
    r_clay = [int(line[12]), 0, 0]
    r_obsidian = [int(line[18]), int(line[21]), 0]
    r_geode = [int(line[27]), 0, int(line[30])]

    print(id, r_ore, r_clay, r_obsidian, r_geode)
    geodes = max_geodes(r_ore, r_clay, r_obsidian, r_geode)
    print("geodes:", geodes, "score:", geodes * id)
    part1 += geodes * id

print("Part 1:", part1)
print(time.time() - start)
