from collections import defaultdict

f = open('inputs/Day4.txt', 'r').read().strip().split("\n")

grid = defaultdict(int)

for y in range(len(f)):
    for x in range(len(f[y])):
        if f[y][x] == "@": grid[(x,y)] = 1

moves = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
part1 = 0
keys = list(grid.keys())
for x,y in keys:
    counter = 0
    for dx, dy in moves:
        _x = dx+x; _y = dy+y
        counter += grid[(_x, _y)]
    if counter < 4: part1 += 1

print('Part 1:', part1)

part2 = 0
while True:
    keys = list(grid.keys())
    to_remove = []
    for x, y in keys:
        if grid[(x,y)] == 0: continue
        counter = 0
        for dx, dy in moves:
            _x = dx + x
            _y = dy + y
            counter += grid[(_x, _y)]
        if counter < 4:
            part2 += 1
            to_remove.append((x, y))
    for x, y in to_remove:
        grid.pop((x,y))
    if len(to_remove) == 0: break

print('Part 2:', part2)
