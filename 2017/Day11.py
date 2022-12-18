
with open("inputs/11.txt") as f:
    move = f.read().strip().split(",")

x = 0
y = 0
dir = {"n":(0,-1), "ne":(1,-0.5), "se":(1,0.5), "s":(0,1), "sw":(-1,0.5), "nw":(-1,-0.5)}


def dist(x, y):
    y = abs(y)
    x = abs(x)
    y -= x / 2
    return int(x + y)


max_d = 0
for m in move:
    x += dir[m][0]
    y += dir[m][1]
    max_d = max(max_d, dist(x,y))

print("Part 1:", dist(x,y))
print("Part 2:", max_d)
