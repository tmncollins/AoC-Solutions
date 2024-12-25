def move(pos, d):
    if d == "<":
        pos = (pos[0] - 1, pos[1])
    elif d == ">":
        pos = (pos[0] + 1, pos[1])
    elif d == "v":
        pos = (pos[0], pos[1] + 1)
    elif d == "^":
        pos = (pos[0], pos[1] - 1)
    return pos


with open("inputs/Day3.txt") as f:
    directions = f.read().strip()

pos = (0, 0)
seen = {pos}
seen2 = {pos}
pos2 = (0, 0)
pos3 = (0, 0)
i = 0

for d in directions:
    pos = move(pos, d)
    seen.add(pos)

    if i % 2 == 0:
        pos2 = move(pos2, d)
        seen2.add(pos2)
    else:
        pos3 = move(pos3, d)
        seen2.add(pos3)

    i += 1

print("Part 1:", len(seen))
print("Part 2:", len(seen2))
