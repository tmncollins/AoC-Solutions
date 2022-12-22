f = open("inputs/Day25.txt").read().split("\n")

sea = [list(f[i]) for i in range(len(f))]

moved = True
j = 0
while moved:
    moved = False
    right = set()
    for y in range(len(sea)):
        for x in range(len(sea[y])):
            if sea[y][x] == ">":
                tx = (x + 1) % len(sea[y])
                if sea[y][tx] == ".":
                    right.add((x,y))
    if len(right) > 0: moved = True
    for x,y in right:
        tx = (x + 1) % len(sea[y])
        sea[y][x] = "."
        sea[y][tx] = ">"

    down = set()
    for y in range(len(sea)):
        for x in range(len(sea[y])):
            if sea[y][x] == "v":
                ty = (y + 1) % len(sea)
                if sea[ty][x] == ".":
                    down.add((x, y))
    if len(down) > 0: moved = True
    for x, y in down:
        ty = (y + 1) % len(sea)
        sea[y][x] = "."
        sea[ty][x] = "v"
    j += 1
    if j % 10 == 0: print(j)

print("Part 1:", j)
