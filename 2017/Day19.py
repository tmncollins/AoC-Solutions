from _collections import *

with open("inputs/19.txt") as f:
    all_data = f.read().split("\n")
    
grid = defaultdict(str)
x,y = -1, -1
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
steps = 0

for _y in range(len(all_data)):
    for _x in range(len(all_data[_y])):
        if all_data[_y][_x] == "|":
            grid[(_x,_y)] = "|"
            if x == -1:
                x = _x
                y = _y
        elif all_data[_y][_x] == "+":
            grid[(_x,_y)] = "+"
        elif all_data[_y][_x] == "-":
            grid[(_x, _y)] = "-"
        elif all_data[_y][_x] in ALPHA:
            grid[(_x, _y)] = all_data[_y][_x]

dir = (0,1)
last = (x, -1)

text = ""
MOVE = ALPHA + "-|+"

while True:
    if grid[(x,y)] == "" or grid[(x,y)] not in MOVE: break
    elif grid[(x,y)] in ALPHA: text += grid[(x,y)]
    elif grid[(x,y)] == "+":
        dir = (0, 0)
        if   grid[(x,y+1)] != "" and grid[(x,y+1)] in MOVE and last != (x, y+1): dir = (0, 1)
        elif grid[(x,y-1)] != "" and grid[(x,y-1)] in MOVE and last != (x, y-1): dir = (0, -1)
        elif grid[(x+1,y)] != "" and grid[(x+1,y)] in MOVE and last != (x+1, y): dir = (1, 0)
        elif grid[(x-1,y)] != "" and grid[(x-1,y)] in MOVE and last != (x-1, y): dir = (-1, 0)

    last = (x,y)
    x += dir[0]
    y += dir[1]
    steps += 1

print("Part 1:", text)
print("Part 2:", steps)
