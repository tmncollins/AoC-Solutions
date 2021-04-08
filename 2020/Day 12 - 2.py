wayPoint = [10, 1]
pos = [0,0]

with open('inputs/12.txt', 'r') as f: #open the file
    contents = f.readlines()


def rotate():
    global pos, wayPoint
    x = wayPoint[0]
    y = wayPoint[1]
    wayPoint = [- y, x]

for line in contents:
    print(pos, wayPoint)
    if line[0] == "N":
        wayPoint[1] += int(line[1:])
    elif line[0] == "E":
        wayPoint[0] += int(line[1:])
    if line[0] == "S":
        wayPoint[1] -= int(line[1:])
    elif line[0] == "W":
        wayPoint[0] -= int(line[1:])
    elif line[0] == "F":
        x = wayPoint[0]
        y = wayPoint[1]

        for i in range(int(line[1:])):
            pos[0] += x
            pos[1] += y

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
