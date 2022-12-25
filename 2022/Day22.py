from _collections import defaultdict


def left(pos):
    return pos[1], -pos[0]


def right(pos):
    return -pos[1], pos[0]


with open("inputs/Day22.txt") as f:
    all_data = f.read().split("\n")

while len(all_data[0]) < 5: all_data.pop(0)

free = set()
wall = set()
row = defaultdict(list)
col = defaultdict(list)
pos = None
dir = (1, 0)
max_x = 0

moves = ""

for y in range(len(all_data)):
    all_data[y] += " "
    if len(all_data[y]) < 5:
        for x in range(max_x):
            if len(col[x]) == 1:
                col[x].append(y-1)
        moves = all_data[y + 1]
        break
    start = False
    max_x = max(max_x, len(all_data[y]))

    for x in range(len(all_data[y])):
        if all_data[y][x] == " ":
            if len(row[y]) == 1:
                row[y].append(x-1)
            if len(col[x]) == 1:
                col[x].append(y-1)
        elif all_data[y][x] in ".#":
            if len(col[x]) == 0:
                col[x].append(y)
            if len(row[y]) == 0:
                row[y].append(x)
            if all_data[y][x] == ".":
                if not pos:
                    pos = (x,y)
                free.add((x,y))
            elif all_data[y][x] == "#":
                wall.add((x,y))

    for x in range(len(all_data[y]), max_x):
        if len(col[x]) == 1:
            col[x].append(y-1)

moves = moves.replace("L", "-L-").replace("R", "-R-").split("-")


for m in moves:
    if m == "L":
        dir = left(dir)
    elif m == "R":
        dir = right(dir)

    else:
        i = int(m)
        for _ in range(i):
            v = (pos[0] + dir[0], pos[1] + dir[1])
            if v not in free and v not in wall:
                # moving left?
                if dir[0] == -1: v = (row[v[1]][1], v[1])
                # moving right?
                elif dir[0] == 1: v = (row[v[1]][0], v[1])
                # moving up
                elif dir[1] == -1: v = (v[0], col[v[0]][1])
                # moving down
                elif dir[1] == 1: v = (v[0], col[v[0]][0])

            if v in wall:
                break
            pos = v

x,y = pos
d = 0
if dir == (0, 1): d = 1
elif dir == (-1, 0): d = 2
elif dir == (0, -1): d = 3
password = 1000 * (y+1) + 4 * (x+1) + d

print("Part 1:", password)





