
n = 1000

grid1 = [[0 for i in range(n)] for j in range(n)]
grid2 = [[0 for i in range(n)] for j in range(n)]

with open("Day5.txt", "r") as f:
    lines = f.readlines()


def add_line(start, end):
    for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            grid1[y][x] += 1
            grid2[y][x] += 1


def add_line_45(start, end):
    if end[0] > start[0]:
        dx = 1
    elif end[0] < start[0]:
        dx = -1
    if end[1] > start[1]:
        dy = 1
    elif end[1] < start[1]:
        dy = -1

    while start != end:
        grid2[start[1]][start[0]] += 1
        start[0] += dx
        start[1] += dy
    grid2[start[1]][start[0]] += 1


def output(grid):
    for y in range(n):
        for x in range(n):
            if grid[y][x] > 0:
                print(grid[y][x], end="")
            else:
                print(" ", end="")
        print()
    print()


def hori_vert(start, end):
    if start[0] == end[0]: return True
    if start[1] == end[1]: return True
    return False


for line in lines:
    line = line.replace("\n", "").split(" -> ")
    start = list(map(int, line[0].split(",")))
    end = list(map(int, line[1].split(",")))
    if hori_vert(start, end):
        add_line(start, end)
    else:
        add_line_45(start, end)

#output(grid2)

part1 = 0
part2 = 0
for y in range(n):
    for x in range(n):
        if grid1[y][x] > 1: part1 += 1
        if grid2[y][x] > 1: part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)


