
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
    width = max(width, len(grid[y])*2)
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            solid.add((x*2,y))
            solid.add((x*2+1,y))
        elif grid[y][x] == "O":
            boxes.add((x*2,y))
        elif grid[y][x] == "@":
            robot = (x*2,y)

def push(pos, d):
    o_pos = pos
    global boxes, solid, new_boxes
    n_pos = (pos[0] + d[0], pos[1] + d[1])
    ans = True

    if d == (-1, 0):
        # left
        np = (pos[0] - 1, pos[1])
        np_b = (pos[0] - 2, pos[1])
        if np in solid: ans = False # hit wall
        elif np_b in boxes: ans = push(np_b, d)
        else: ans = True
    elif d == (1, 0):
        # right
        np = (pos[0] + 1, pos[1])
        np_b = (pos[0] + 2, pos[1])
        if np_b in solid: ans = False # hit wall
        elif np_b in boxes: ans = push(np_b, d)
        else: ans = True
    else:
        # up or down
        np_l = (pos[0], pos[1] + d[1])
        np_r = (pos[0]+1, pos[1]+d[1])
        np_b = (pos[0]-1, pos[1]+d[1])
        if np_l in solid or np_r in solid: ans = False # hit wall
        elif np_l in boxes: ans = push(np_l, d) # only pushing one box
        elif np_b in boxes:
            if np_r in boxes: ans = push(np_b, d) and push(np_r, d) # pushing two boxes
            else: ans = push(np_b, d) # only pushing one box
        elif np_r in boxes: ans = push(np_r, d) # only pushing one box
        else: ans = True

    if ans:
        if o_pos in new_boxes:
            new_boxes.remove(o_pos)
        new_boxes.add(n_pos)
    return ans

def needs_to_push(pos, d):
    global boxes
    if d == (1,0):
        if (pos[0]+1, pos[1]) in boxes:
            return (pos[0]+1, pos[1])
        return False
    elif d == (-1,0):
        if (pos[0]-2, pos[1]) in boxes:
            return (pos[0]-2, pos[1])
        return False
    else:
        left = (pos[0], pos[1]+d[1])
        right = (pos[0]-1, pos[1]+d[1])
        if left in boxes:
            return left
        elif right in boxes:
            return right
        return False

def move(d):
    global solid, boxes, robot, new_boxes
    directions = {"<": (-1,0), ">": (1,0), "^":(0,-1), "v":(0,1)}
    new_pos = (robot[0] + directions[d][0], robot[1] + directions[d][1])
    if new_pos in solid: return # can't move here

    p = needs_to_push(robot, directions[d])
    if p:
        new_boxes = set(boxes)
        if push(p, directions[d]):
            boxes = new_boxes
            robot = new_pos
        return
    robot = new_pos

def output():
    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in solid:
                line += "#"
            elif (x,y) in boxes:
                line += "["
            elif (x-1,y) in boxes:
                line += "]"
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
output()

for i in range(height+1, len(grid)):
    moves += grid[i].replace("\n", "")

x = 0
for m in moves:
    move(m)

#    print(x)
#    output()
#    x += 1
#    if x > 5900:
#        print(m)
#        output()


print("Part 2:", GPS())
