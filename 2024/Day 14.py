from _collections import defaultdict

def move(pos, vel, time):
    global width, height
    new_pos = [pos[0] + vel[0] * time, pos[1] + vel[1] * time]
    new_pos[0] %= width
    new_pos[1] %= height
    return new_pos

def get_quadrant(pos):
    global width, height
    half_w = width // 2
    if pos[0] == half_w: return 0
    half_h = height // 2
    if pos[1] == half_h: return 0
    if pos[0] < half_w:
        if pos[1] < half_h: return 1
        else: return 2
    else:
        if pos[1] < half_h: return 3
        else: return 4

def entropy():
    global positions
    centre = (width // 2, height // 2)
    cx, cy = centre
    e = 0
    for x, y in positions:
        e += (cx-x)**2 + (cy-y)**2
    return e

with open("inputs/Day14.txt", "r") as f:
    all_data = f.read().split("\n")

all_dat = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split("\n")

width = 11
height = 7
width = 101
height = 103

quads = defaultdict(int)
positions = set()
bots = list()

def output():
    global positions
    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in positions:
                line += "#"
            else:
                line += "."
        print(line)

for line in all_data:
    if len(line) < 5: continue
    line = line.replace("p=", "").split(" v=")
    pos = list(map(int, line[0].split(",")))
    vel = list(map(int, line[1].split(",")))

    new_pos = move(pos, vel, 100)
    q = get_quadrant(new_pos)
    print(new_pos, q)
    quads[q] += 1
    positions.add(tuple(new_pos))
    bots.append([pos, vel])

output()

i = 0
mine = float("inf")
while True:
    i += 1
    positions = set()
    for pos, vel in bots:
        new_pos = move(pos, vel, i+1)
#        q = get_quadrant(new_pos)
#        print(new_pos, q)
#        quads[q] += 1
        positions.add(tuple(new_pos))
#        bots.append([new_pos, vel])

#    print(positions)
    e = entropy()
    if i % 1000 == 0:
        print(i, e)
    if e < mine:
        mine = min(e, mine)
        print(i, mine)
        output()
    if e < 10000:
        print(i, e)
        output()

print(quads)
print(quads[1] * quads[2] * quads[3] * quads[4])
