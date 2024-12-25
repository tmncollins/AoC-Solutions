from copy import deepcopy
from _collections import deque

with open("inputs/Day21.txt") as file:
    data = file.read().strip().split("\n")

free = set()
rocks = set()
width = len(data[0])
height = len(data[1])

start = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            free.add((x,y))
            start = (x,y)
        elif data[y][x] == ".":
            free.add((x,y))
        elif data[y][x] == "#":
            rocks.add((x,y))

def count_reach_brute(start, n):
    pos = {start}
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i in range(n):
        np = set()
        for p in pos:
            for m in moves:
                p2 = (p[0] + m[0], p[1] + m[1])
                if p2 in free:
                    np.add(p2)
        pos = np
#        print(len(pos))
    return len(pos)

def triangle(n):
    if n <= 0: return 0
    return ((n)*(n+1))//2

def output(pos):
    d = 15
    for y in range(start[1]-d,start[1]+d+1):
        line = ""
        if y % height == 0: print("-"*(d*2 + (d*2)//width)  )
        for x in range(start[0]-d,start[1]+d+1):
            if x % width == 0: line += "|"
            if (x%width,y%height) in rocks:
                line += "#"
            elif (x,y) in pos:
                line += "O"
            else:
                line += "."
        print(line)
    print()

def count_reach(start, n):
    if n == 0: return 1
    if n < 0: return 0
    seen = {start}
    q = deque()
    q.append((start, n))
    count = 0
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while q:
        pos, d = q.popleft()
        if d % 2 == 0:
            count += 1
        if d == 0: continue
        for m in moves:
            pos2 = (pos[0] + m[0], pos[1] + m[1])
            if pos2 not in seen and pos2 in free:
                seen.add(pos2)
                q.append((pos2, d-1))
    return count


def count_reach_inf(start, n):
    if n == 0: return 1
    if n < 0: return 0
    seen = {start}
    all_pos = set()
    q = deque()
    q.append((start, n))
    count = 0
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while q:
        pos, d = q.popleft()
        if d % 2 == 0:
            count += 1
            all_pos.add(pos)
        if d == 0: continue
        for m in moves:
            pos2 = (pos[0] + m[0], pos[1] + m[1])
            pos2_mod = (pos2[0] % width, pos2[1] % height)
            if pos2 not in seen and pos2_mod not in rocks:
                seen.add(pos2)
                q.append((pos2, d-1))
    output(all_pos)
    return count


print("Part 1:", count_reach(start, 64))

edges = [(0, height // 2), (width-1, height//2), (width//2, 0), (width//2, height-1)]
corners = [(0, 0), (0, height-1), (width-1, 0), (width-1, height-1)]

n = 26501365
ans = 0

star = (n-width+1)//width

same = count_reach(start, n)
opp = count_reach(start, n-1)

n_same = (((star)//2)*2+1)**2
n_opp = (((star+1)//2)*2)**2

# rings
ans = n_same * same + n_opp * opp

# edges
n_edge = (n - width//2 - 1) - width*(star)
for edge in edges:
    ans += count_reach(edge, n_edge)

# corners
n_corner = (n - width - 1) - width*(star-1)
num_corners = star
for corner in corners:
    a = count_reach(corner, n_corner) * num_corners
    b = count_reach(corner, n_corner-width) * (num_corners+1)
    ans += a + b

print("Part 2:", ans)