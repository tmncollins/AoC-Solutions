with open('inputs/12.txt', 'r') as f: #open the file
    contents = f.readlines()

pos = [0,0]
face = "E"

def rotate():
    global face
    next = {"E":"N", "N":"W", "W":"S", "S":"E"}
    face = next[face]

for line in contents:
#    print(pos)
    if line[0] == "N":
        pos[1] += int(line[1:])
    elif line[0] == "E":
        pos[0] += int(line[1:])
    if line[0] == "S":
        pos[1] -= int(line[1:])
    elif line[0] == "W":
        pos[0] -= int(line[1:])
    elif line[0] == "F":
        if face == "N":
            pos[1] += int(line[1:])
        elif face == "E":
            pos[0] += int(line[1:])
        if face == "S":
            pos[1] -= int(line[1:])
        elif face == "W":
            pos[0] -= int(line[1:])
    elif line[0] == "L":
        a = int(line[1:])
        while a > 0:
            a -= 90
            rotate()
    elif line[0] == "R":
        a = int(line[1:])
        while a > 0:
            a -= 90
            rotate()
            rotate()
            rotate()

print(pos, abs(pos[0]) + abs(pos[1]))

