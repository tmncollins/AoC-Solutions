data = open("Day15.txt").read().split("\n")

cave = []
for line in data:
    cave.append(list(map(int, list(line))))

INF = float("inf")
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def valid(x, y):
    if x < 0 or y < 0: return False
    if x >= len(cave[0]) or y >= len(cave): return False
    return True

def output(cave):
    for line in cave:
        s = ""
        for v in line:
            s += str(v)
        print(s)
    print()

dpmem = [[INF for i in range(len(cave[0]))] for j in range(len(cave))]
dpmem[0][0] = 0

for i in range(5):
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            for d in direction:
                X = x + d[0]
                Y = y + d[1]
                if valid(X, Y):
                    dpmem[y][x] = min(dpmem[y][x], dpmem[Y][X] + cave[y][x])

def expand(cave):
    cave2 = []
    for y in range(5):
        for i in range(len(cave)):
            cave2.append([])
        for x in range(5):
            for i in range(len(cave)):
                for j in range(len(cave[i])):
                    v = cave[i][j] + x + y
                    if v >= 10: v -= 9
                    cave2[i + y * len(cave)].append(v)
    return cave2


print("Part 1:", dpmem[len(cave)-1][len(cave[0])-1])

cave = expand(cave)
dpmem = [[INF for i in range(len(cave[0]))] for j in range(len(cave))]
dpmem[0][0] = 0

print("done cave")
#output(cave)

noChange = True
while noChange:
    noChange = False
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            for d in direction:
                X = x + d[0]
                Y = y + d[1]
                last = dpmem[y][x]
                if valid(X, Y):
                    dpmem[y][x] = min(dpmem[y][x], dpmem[Y][X] + cave[y][x])
                if last != dpmem[y][x]: noChange = True

    print(dpmem[len(cave)-1][len(cave[0])-1])
