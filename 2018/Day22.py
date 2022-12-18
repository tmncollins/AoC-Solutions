from collections import deque, defaultdict
import heapq

depth = 11541
target = (14, 778)
#depth = 510
#target = (5,746)
#depth = 4002


width = target[0] * 3
height = target[1] * 3

width = 500
height = 1000

#height = width

cave = [[0 for _ in range(width)] for _ in range(height)]

# generate cave
for x in range(1, width):
    cave[0][x] = ((16807 * x) + depth) % 20183
for y in range(1, height):
    cave[y][0] = ((48271 * y) + depth) % 20183


for y in range(1, height):
    for x in range(1, width):
        if (x,y) == target: cave[y][x] = depth % 20183
        else:
            cave[y][x] = ((cave[y][x-1] * cave[y-1][x]) + depth) % 20183


for y in range(0, height):
    for x in range(0, width):
        cave[y][x] = (cave[y][x] + depth) % 3


#cave[0][0] = 0
cave[target[1]][target[0]] = 0

def output(width, height):

    terrain = ".=|"

    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) == (0,0): line += "M"
            elif (x,y) == target: line += "T"
            else: line += terrain[cave[y][x]]
        print(line)

part1 = 0
for y in range(target[1]+1):
    for x in range(target[0]+1):
        part1 += cave[y][x]

print("Part 1:", part1)

# 0 - torch, 1 - climbing gear, 2 - neither
q = [(0,0,0,0)]
move = [(0,1), (1,0), (-1,0), (0,-1)]


def can_traverse(terrain, equipment):
    if terrain == 0:
        return equipment in [0,1]
    if terrain == 1:
        return equipment in [2,1]
    if terrain == 2:
        return equipment in [0,2]


def get_both_traverse(a, b):
    a, b = min(a,b), max(a,b)
    if a == 0:
        if b == 0: return 0
        if b == 1: return 1
        if b == 2: return 0
    elif a == 1:
        if b == 0: return 1
        if b == 1: return 1
        if b == 2: return 2
    else:
        if b == 0: return 0
        if b == 1: return 2
        if b == 2: return 0


LRG = 999999999
seen = defaultdict(int)
seen[(0, 0, 0)] = LRG

#output(100, 1000)

#print(width, height)

while q:
    t, x, y, e = heapq.heappop(q)
#    print(t, x, y, e)

    if (x,y) == target:
        if e == 0:
            print("Part 2:", t)
            break
        else:
            heapq.heappush(q, (t+7, x, y, 0))
            continue

    for m in move:
        _x = x + m[0]
        _y = y + m[1]
#        print(_x, _y)
        if _x >= 0 and _y >= 0 and _x < width and _y < height:
            if can_traverse(cave[_y][_x], e):
                if LRG - (t+1) > seen[(_x, _y, e)]:
                    heapq.heappush(q, (t+1, _x, _y, e))
                    seen[(_x, _y, e)] = LRG - (t+1)
            else:
                _e = get_both_traverse(cave[y][x], cave[_y][_x])
                if LRG - (t+8) > seen[(_x, _y, _e)]:
                    heapq.heappush(q, (t+8, _x, _y, _e))
                    seen[(_x, _y, _e)] = LRG - (t+8)
