
with open("input/3.txt") as f:
    claims = f.readlines()

fab = [[0 for i in range(1000)] for _ in range(1000)]

for claim in claims:
    claim = claim.replace("\n", "").split()
    pos = claim[2][:-1].split(",")
    dimen = claim[3].split("x")

    for y in range(int(dimen[1])):
        for x in range(int(dimen[0])):
            fab[int(pos[1]) + y][int(pos[0]) + x] += 1

sqr = 0
for y in range(1000):
    for x in range(1000):
        if fab[y][x] > 1: sqr += 1
print("Part 1:", sqr)

for claim in claims:
    claim = claim.replace("\n", "").split()
    pos = claim[2][:-1].split(",")
    dimen = claim[3].split("x")

    single = True

    for y in range(int(dimen[1])):
        for x in range(int(dimen[0])):
            if fab[int(pos[1]) + y][int(pos[0]) + x] > 1:
                single = False
                break

    if single: print("Part 2:", claim[0])

