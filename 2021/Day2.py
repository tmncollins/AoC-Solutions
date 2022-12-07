f = open("Day2.txt")
data = f.read().split("\n")

d, h = 0, 0
aim = 0
for line in data:
    cmd, v = line.split()
    v = int(v)

    if cmd[0] == "f":
        h += v
    elif cmd[0] == "u":
        d -= v
    elif cmd[0] == "d":
        d += v

print("Part 1:", d*h)

d, h = 0, 0
aim = 0
for line in data:
    cmd, v = line.split()
    v = int(v)

    if cmd[0] == "f":
        h += v
        d += aim * v
    elif cmd[0] == "u":
        aim -= v
    elif cmd[0] == "d":
        aim += v

print("Part 2:", d*h)