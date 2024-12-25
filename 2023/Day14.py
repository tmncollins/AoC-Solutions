
with open("inputs/Day14.txt") as file:
    data = file.read().strip().split("\n")

fixed = set()
rocks = set()
width = len(data[2])
height = len(data)
order = []

def output():
    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in rocks: line += "O"
            elif (x,y) in fixed: line += "#"
            else: line += "."
        print(line)
    print()

def fixed_rock(rock, rocks, dx, dy):
    if rock[0] < 0 or rock[1] < 0: return True
    if rock[0] >= width or rock[1] >= height: return True
    if rock in fixed: return True
    if rock not in rocks: return False
    return fixed_rock((rock[0]+dx, rock[1]+dy), rocks, dx, dy)

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "O": rocks.add((x,y))
        if data[y][x] == "#": fixed.add((x,y))

#print(len(rocks))

def roll(dx, dy):
    global rocks
    while True:
        new_rocks = set()
        for rock in rocks:
            new_rock = (rock[0] + dx, rock[1] + dy)
            if new_rock in fixed: new_rocks.add(rock)
            elif fixed_rock(new_rock, rocks, dx, dy): new_rocks.add(rock)
            else: new_rocks.add(new_rock)
        if new_rocks == rocks: break
        rocks = new_rocks

#seen = [set(rocks)]
seen = {frozenset(rocks):0}
order.append(frozenset(rocks))
roll(0, -1)

# part 1
part1 = 0
for rock in rocks:
#    print(rock, height - rock[1])
    part1 += height - rock[1]


#output()
print("Part 1:", part1)

# part 2
cycle = [(0,-1), (-1,0), (0,1), (1,0)]
i = 1
counter = 1
while True:
    while True:
        roll(cycle[i][0], cycle[i][1])
        i += 1
        i %= 4
        if i == 0: break
    if frozenset(rocks) in seen.keys():
        break
    seen[frozenset(rocks)] = counter
    order.append(frozenset(rocks))
    counter += 1
    print(counter)

idx = seen[frozenset(rocks)]
cycle_len = len(order) - idx
nth = ((1000000000 - idx) % cycle_len) + idx
rocks = set(order[nth])

# short cut
part2 = 0
for rock in rocks:
    part2 += height - rock[1]

print("Part 2:", part2)