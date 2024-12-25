

with open("inputs/Day6.txt", "r") as f:
    grid = f.read().split("\n")

Y = len(grid)
X = len(grid[0])
d = (0, -1)
pos = (-1, -1)

for i in range(Y):
    grid[i] = list(grid[i])
    if "^" in grid[i]:
        x = grid[i].index("^")
        pos = (x, i)
        grid[i][x] = "."

def output():
    for line in grid:
        print("".join(line))

def in_grid(pos):
    x,y = pos
    if x < 0 or y < 0 or x >= X or y >= Y:
        return False
    return True

def gets_stuck(pos, d):
    global grid
    seen = set()
    while in_grid(pos):
        if (pos, d) in seen: return True
        seen.add((pos, d))
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if in_grid(next_pos) and grid[next_pos[1]][next_pos[0]] == "#":
            # rotate
            d = (-d[1], d[0])
        else:
            pos = next_pos
    return False

def walk(pos, d):
    global grid
    seen = set()
    while in_grid(pos):
#        print(pos)
        seen.add(pos)
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if in_grid(next_pos) and grid[next_pos[1]][next_pos[0]] == "#":
            # rotate
            d = (-d[1], d[0])
        else:
            pos = next_pos
    return seen

def part2(pos, d):
    global grid
    path = walk(pos, d)
    ans = 0
    x = 0
    for p in path:
        if x % 100 == 0:
            print(x, "/", len(path))
        grid[p[1]][p[0]] = "#"
        if gets_stuck(pos, d):
            ans += 1
        grid[p[1]][p[0]] = "."
        x += 1
    return ans

print("Part 1:", len(walk(pos, d)))
print("Part 2:", part2(pos, d))