from _collections import defaultdict

black = defaultdict(bool)

with open("inputs/24.txt") as f:
    contents = f.readlines()

for line in contents:
    line = line.replace("\n", "")
    index = 0
    pos = [0,0]
    while index < len(line):
        if line[index] == "e":
            pos[0] += 1
        elif line[index] == "w":
            pos[0] -= 1
        elif line[index] == "s":
            index += 1
            pos[1] += 1
            if line[index] == "e":
                pos[0] += 0.5
            elif line[index] == "w":
                pos[0] -= 0.5
        elif line[index] == "n":
            pos[1] -= 1
            index += 1
            if line[index] == "e":
                pos[0] += 0.5
            elif line[index] == "w":
                pos[0] -= 0.5
        index += 1
    black[tuple(pos)] = not black[tuple(pos)]

tot = 0

for item in black.values():
    if item: tot += 1

print(tot)