from time import time

def match(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]: return False
    return True

def get_vertical_plane(grid):
    planes = [i+1 for i in range(len(grid[0])-1)]
    for line in grid:
        new_planes = []
        for p in planes:
            left = line[:p][::-1]
            right = line[p:]
            if match(left, right):
                new_planes.append(p)
        planes = new_planes

    if len(planes) == 0: return None
    return planes[0]

def match_smudge(a, b):
    s = False
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            if not s: s = True
            else: return False
    return True

def get_vertical_smudge(grid):
    planes = [[i+1, False] for i in range(len(grid[0])-1)]
    for line in grid:
        new_planes = []
        for p, s in planes:
            left = line[:p][::-1]
            right = line[p:]
            if match(left, right):
                new_planes.append([p, s])
            elif (not s) and match_smudge(left, right):
                new_planes.append([p, True])
        planes = new_planes

    ans = [p[0] for p in planes]
    return ans

start = time()
with open("inputs/Day13.txt") as file:
    data = file.read().strip().split("\n")
data.append("")

grid = []
part1 = 0
part2 = 0
for line in data:
    line = line.strip()
    if len(line) < 3:
        if len(grid) > 1:
            # part 1
            v = get_vertical_plane(grid)
            h = get_vertical_plane(list(zip(*grid[::-1])))
            if v != None: part1 += v
            elif h != None:
                h = len(grid) - h
                part1 += h * 100

            # part 2
            v2 = get_vertical_smudge(grid)
            h2 = get_vertical_smudge(list(zip(*grid[::-1])))
            for i in range(len(h2)): h2[i] = len(grid) - h2[i]

            if v != None and v in v2: v2.remove(v)
            if h != None and h in h2: h2.remove(h)

            if len(v2) > 0: part2 += v2[0]
            elif len(h2) > 0: part2 += 100 * h2[0]

        grid = []
    else:
        grid.append(line)

print("Part 1:", part1)
print("Part 2:", part2)
print(time() - start)
