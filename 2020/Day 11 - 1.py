with open('inputs/11.txt', 'r') as f: #open the file
    contents = f.readlines()

from _collections import defaultdict

width = len(contents[0])
height = len(contents)

# -1 empty, 0 floor, 1 occupied
seats = defaultdict(int)
for y in range(height):
    for x in range(width):
        try:
            if contents[y][x] == "L":
                seats[(x,y)] = 1
        except:
            pass


def update(old):
    global width, height
    new = defaultdict(int)
    dir = [(-1,0),(1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for y in range(height):
        for x in range(width):
            if old[(x,y)] != 0:
                o = 0
                for d in dir:
                    if old[(x+d[0],y+d[1])] == 1:
                        o += 1
                if old[(x,y)] == -1 and o == 0:
                    new[(x,y)] = 1
                elif old[(x,y)] == 1 and o >= 4:
                    new[(x,y)] = -1
                else:
                    new[(x,y)] = old[(x,y)]
            else:
                new[(x,y)] = 0

    return new

before = -1
s = 0
while True:
    seats = update(seats)
    x = list(seats.values()).count(1)
    if x == before:
        if s == 5:
            break
        s += 1
    else:
        before = x
        s = 0
print(before)