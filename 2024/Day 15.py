
solid = set()
boxes = set()
robot = (0,0)

with open("inputs/Day15.txt", "r") as f:
    grid = f.read().split("\n")

height = 0
width = 0
for y in range(len(grid)):
    if len(grid[y]) < 5:
        height = y
        break
    width = max(width, len(grid[y]))
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            solid.add((x,y))
        elif grid[y][x] == "O":
            boxes.add((x,y))
        elif grid[y][x] == "@":
            robot = (x,y)

def push(pos, d):
    o_pos = pos
    global boxes, solid
    can_push = True
    n_pos = (0,0)
    while True:
        n_pos = (pos[0] + d[0], pos[1] + d[1])
        if n_pos in solid:
            can_push = False
            break
        elif n_pos in boxes:
            pos = n_pos
        else:
            break
    if can_push:
        boxes.remove(o_pos)
        boxes.add(n_pos)
        return True
    else:
        return False

def move(d):
    global solid, boxes, robot
    directions = {"<": (-1,0), ">": (1,0), "^":(0,-1), "v":(0,1)}
    new_pos = (robot[0] + directions[d][0], robot[1] + directions[d][1])
    if new_pos in solid: return # can't move here
    elif new_pos in boxes:
        if push(new_pos, directions[d]):
            robot = new_pos
        return
    else: robot = new_pos # move here

def output():
    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in solid:
                line += "#"
            elif (x,y) in boxes:
                line += "O"
            elif (x,y) == robot:
                line += "@"
            else:
                line += "."
        print(line)

def GPS():
    ans = 0
    for x,y in boxes:
        ans += y*100 + x
    return ans

moves = ""
for i in range(height+1, len(grid)):
    moves += grid[i].replace("\n", "")

for m in moves:
    move(m)

output()

print("Part 1:", GPS())