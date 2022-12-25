from _collections import defaultdict


def left(pos):
    return pos[1], -pos[0]


def right(pos):
    return -pos[1], pos[0]


with open("inputs/Day22.txt") as f:
    all_data = f.read().split("\n")

grid = []
moves = ""
max_x = 0
for y in range(len(all_data)):
    line = all_data[y]
    if len(line) < 5:
        if len(grid) == 0: continue
        else:
            moves = all_data[y+1]
            break

    grid.append(line)
    max_x = max(len(all_data[y]), max_x)
max_x += 1

faces = []
face_offset = []
face_length = 50
pos = (0, 0, 0)

# extract all the faces and positions
for start_y in range(0, len(grid), face_length):
    for start_x in range(0, len(grid[start_y]), face_length):
        face = []
        for y in range(start_y, start_y + face_length):
            line = grid[y][start_x:start_x+face_length]
            if "." not in line: break
            face.append(line)
        if len(face) == face_length:
            faces.append(face)
            face_offset.append((start_x, start_y))

free = set()
wall = set()
row = [defaultdict(list) for _ in range(6)]
col = [defaultdict(list) for _ in range(6)]
pos = (0, 0, 0)
dir = (1, 0)

# extract info from the faces
for f in range(6):
    face = faces[f]
    for y in range(face_length):
        for x in range(face_length):
            if face[y][x] == "#":
                wall.add((f,x,y))
            elif face[y][x] == ".":
                free.add((f,x,y))

moves = moves.replace("L", "-L-").replace("R", "-R-").split("-")

# change face what happens when we go off (f, d)?
# f = face num
# d = direction: 0-right, 1-down, 2-left, 3-up
# this gives us ((f, x, y), dir)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
U = 3
R = 0
L = 2
D = 1

# hard code cube net info
change_face = dict()
change_face[(0, R)] = (1, "left", "same", R)
change_face[(0, D)] = (2, "same", "top", D)
change_face[(0, L)] = (3, "left", "inverse", R)
change_face[(0, U)] = (5, "left", "x", R)

change_face[(1, R)] = (4, "right", "inverse", L)
change_face[(1, D)] = (2, "right", "x", L)
change_face[(1, L)] = (0, "right", "same", L)
change_face[(1, U)] = (5, "same", "bottom", U)

change_face[(2, R)] = (1, "y", "bottom", U)
change_face[(2, D)] = (4, "same", "top", D)
change_face[(2, L)] = (3, "y", "top", D)
change_face[(2, U)] = (0, "same", "bottom", U)

change_face[(3, R)] = (4, "left", "same", R)
change_face[(3, D)] = (5, "same", "top", D)
change_face[(3, L)] = (0, "left", "inverse", R)
change_face[(3, U)] = (2, "left", "x", R)

change_face[(4, R)] = (1, "right", "inverse", L)
change_face[(4, D)] = (5, "right", "x", L)
change_face[(4, L)] = (3, "right", "same", L)
change_face[(4, U)] = (2, "same", "bottom", U)

change_face[(5, R)] = (4, "y", "bottom", U)
change_face[(5, D)] = (1, "same", "top", D)
change_face[(5, L)] = (0, "y", "top", D)
change_face[(5, U)] = (3, "same", "bottom", U)

for m in moves:
    if m == "L":
        dir = left(dir)
    elif m == "R":
        dir = right(dir)
    else:

        i = int(m)
        for _ in range(i):
            v = [pos[0], pos[1] + dir[0], pos[2] + dir[1]]
            f, x, y, d = -1, -1, -1, -1
            if v[1] < 0:
                # gone off left
                f, x, y, d = change_face[(pos[0], 2)]
            elif v[2] < 0:
                # gone off up
                f, x, y, d = change_face[(pos[0], 3)]
            elif v[1] >= face_length:
                # gone off right
                f, x, y, d = change_face[(pos[0], 0)]
            elif v[2] >= face_length:
                # gone off down
                f, x, y, d = change_face[(pos[0], 1)]

            if f != -1:
                v[0] = f
                X, Y = v[1], v[2]
                if x == "right":
                    v[1] = face_length - 1
                elif x == "left":
                    v[1] = 0
                elif x == "inverse":
                    v[1] = face_length - X - 1
                elif x == "yinverse":
                    v[1] = face_length - Y - 1
                elif x == "y":
                    v[1] = Y
                elif x == "same":
                    pass
                else: print("error")

                if y == "top":
                    v[2] = 0
                elif y == "bottom":
                    v[2] = face_length - 1
                elif y == "inverse":
                    v[2] = face_length - Y - 1
                elif y == "xinverse":
                    v[2] = face_length - X - 1
                elif y == "x":
                    v[2] = X
                elif y == "same":
                    pass
                else: print("error")

            v = tuple(v)
            if v in wall:
                break

            pos = v
            if d != -1:
                dir = directions[d]

f,x,y = pos
x += face_offset[f][0]
y += face_offset[f][1]
d = 0
if dir == (0, 1): d = 1
elif dir == (-1, 0): d = 2
elif dir == (0, -1): d = 3
password = 1000 * (y+1) + 4 * (x+1) + d

print("Part 2:", password)





