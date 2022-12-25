from math import gcd
from _collections import *

def lcm(a, b):
    return (a*b) // gcd(a, b)

def all_blizzards():
        global left, right, up, down
        b = set()
        for item in left: b.add(item)
        for item in right: b.add(item)
        for item in up: b.add(item)
        for item in down: b.add(item)
        return b

def output(b, pos=(-1,-1)):
    global width, height

    for y in range(height+2):
        line = ""
        for x in range(width+2):
            if (x,y) == pos:
                line += "E"
            elif (x,y) in b:
                line += "~"
            elif (x,y) in walls:
                line += "#"
            else:
                line += "."
        print(line)

def move(p, d):
    global width, height
    x,y = p
    dx,dy = d
    x += dx
    y += dy
    if x == 0:
        x = width
    elif x == width + 1:
        x = 1
    if y == 0:
        y = height
    elif y == height + 1:
        y = 1
    return x,y


with open("inputs/Day24.txt") as f:
    all_data = f.read().strip().split("\n")

left = set()
right = set()
up = set()
down = set()
walls = set()

start = (all_data[0].index("."), 0)
end = (all_data[-1].index("."), len(all_data)-1)
height = len(all_data) - 2
width = len(all_data[0]) - 2

for x in range(width+2):
    walls.add((x, 0))
    walls.add((x, height+1))

#print(walls)
walls.remove(start)
walls.remove(end)
walls.add((start[0], -1))
walls.add((end[0], height+2))

for y in range(1, len(all_data)-1):
    walls.add((0, y))
    walls.add((width+1, y))
    for x in range(1, len(all_data[y])-1):
        if all_data[y][x] == "^":
            up.add((x,y))
        elif all_data[y][x] == "<":
            left.add((x,y))
        elif all_data[y][x] == ">":
            right.add((x,y))
        elif all_data[y][x] == "v":
            down.add((x,y))

blizzards = [all_blizzards()]
#for i in range(lcm(width, height)-1):
while len(blizzards) == 1 or blizzards[0] != blizzards[-1]:
    new_left = set()
    new_right = set()
    new_up = set()
    new_down = set()
    for item in left: new_left.add(move(item, (-1, 0)))
    for item in right: new_right.add(move(item, (1, 0)))
    for item in up: new_up.add(move(item, (0, -1)))
    for item in down: new_down.add(move(item, (0, 1)))
    left = new_left
    right = new_right
    up = new_up
    down = new_down
    blizzards.append(all_blizzards())

blizzards.pop()

moves = [(0,1), (1,0), (-1,0), (0,-1), (0, 0)]

def run(start, end, start_d=0):
    q = deque()
    q.append((start_d, start))
    seen = set()

    while q:
        d, u = q.popleft()
    #    print(d,u)

    #    output(blizzards[d%len(blizzards)], u)

        if u == end:
            return d

        d += 1
        b = d % len(blizzards)

        for m in moves:
            v = (u[0] + m[0], u[1] + m[1])
            if v not in walls and v not in blizzards[b]:
               if (v, b) not in seen:
                    seen.add((v, b))
                    q.append((d, v))


print("Part 1:", run(start, end))
trip1 = run(start, end)
trip2 = run(end, start, trip1)
trip3 = run(start, end, trip2)
print("Part 2:", trip3)



