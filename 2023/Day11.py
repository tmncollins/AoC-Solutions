from collections import defaultdict

with open("inputs/Day11.txt") as file:
    data = file.read().strip().split()

rows = defaultdict(list)
cols = defaultdict(list)
galaxies = []
row_map = defaultdict(int)
col_map = defaultdict(int)
row_map_2 = defaultdict(int)
col_map_2 = defaultdict(int)

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "#":
            rows[y].append(x)
            cols[x].append(y)
            galaxies.append((x,y))

PART2 = 1000000
i = 0
i2 = 0
for y in range(len(data)):
    if len(rows[y]) == 0:
        i += 1
        i2 += PART2 - 1
    row_map[y] = i
    row_map_2[y] = i2
    i += 1
    i2 += 1

i = 0
i2 = 0
for x in range(len(data[2])):
    if len(cols[x]) == 0:
        i += 1
        i2 += PART2 - 1
    col_map[x] = i
    col_map_2[x] = i2
    i += 1
    i2 += 1

galaxies_2 = list(galaxies)
for i in range(len(galaxies)):
    galaxies[i] = (col_map[galaxies[i][0]], row_map[galaxies[i][1]])
    galaxies_2[i] = (col_map_2[galaxies_2[i][0]], row_map_2[galaxies_2[i][1]])


part1 = 0
part2 = 0
for i in range(len(galaxies)):
    for j in range(i):
        dx = abs(galaxies[i][0] - galaxies[j][0])
        dy = abs(galaxies[i][1] - galaxies[j][1])
        part1 += dx + dy
        dx = abs(galaxies_2[i][0] - galaxies_2[j][0])
        dy = abs(galaxies_2[i][1] - galaxies_2[j][1])
        part2 += dx + dy

print(part1)
print(part2)