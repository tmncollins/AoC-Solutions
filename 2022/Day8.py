
with open("inputs/Day8.txt") as f:
    all_data = f.read().split("\n")

trees = [list(map(int, list(line))) for line in all_data]
#print(trees)


def get_visible(row):
    highest = -1
    vis = []
    for i in range(len(row)):
        if row[i] > highest:
            highest = row[i]
            vis.append(i)
    return vis


visible = set()

# check rows
for y in range(len(trees)):
    vis = get_visible(trees[y])
    for x in vis:
        visible.add((x, y))
    vis = get_visible(trees[y][::-1])
    for x in vis:
        visible.add((len(trees[y]) - 1 - x, y))

# check columns
for x in range(len(trees[0])):
    col = []
    for y in range(len(trees)):
        col.append(trees[y][x])
    vis = get_visible(col)
    for y in vis:
        visible.add((x,y))
    vis = get_visible(col[::-1])
    for y in vis:
        visible.add((x,len(trees) - 1 - y))

#print(visible)
print("Part 1:", len(visible))


def see_dir(x, y, m):
    global trees
    h = trees[y][x]
    d = 0
    while True:
        x += m[0]
        y += m[1]
        if x < 0 or y < 0: return d
        if x >= len(trees[0]) or y >= len(trees): return d
        if trees[y][x] >= h: return d + 1
        d += 1


def scenic_score(x,y):
    global trees
    score = 1
    move = [(1,0), (0,1), (-1,0), (0,-1)]
    for i in range(4):
        score *= see_dir(x,y,move[i])
    return score


best_score = 0
best_loc = None
for y in range(len(trees)):
    for x in range(len(trees[0])):
        s = scenic_score(x, y)
#        print(x, y, ":", s)
        if s > best_score:
            best_score = s
            best_loc = (x,y)

print("Part 2:", best_score)
#print(best_loc)


