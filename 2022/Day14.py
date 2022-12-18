
with open("inputs/Day14.txt") as f:
    all_data = f.read().split("\n")


rock = set()
sand = set()
flowing = set()


def add_rock(rocks):
    global rock, bottom
    _x,_y = -1, -1
    for point in rocks:
        x,y = list(map(int, point.split(",")))
#        print((x,y), (_x,_y))
        if _x != -1:
            for ny in range(min(_y, y), max(_y, y)+1):
                for nx in range(min(_x, x), max(x, _x)+1):
                    rock.add((nx,ny))
                    bottom = max(bottom, ny)
        _x, _y = x, y


def free(x,y):
    return (x,y) not in rock and (x,y) not in sand


def place_sand(part2 = False):
    global sand_y, sand_x, bottom
    x,y = sand_x, sand_y
    flowing.clear()
    while True:
        flowing.add((x,y))

        if y == bottom - 1:
            flowing.add((x, y+1))
            if part2:
                sand.add((x, y))
                return True
            else: return False

        if free(x,y+1):
            y += 1
        elif free(x-1, y+1):
            x -= 1
            y += 1
        elif free(x+1, y+1):
            x += 1
            y += 1
        else:
            sand.add((x,y))
            return True


def output(min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x,y) in rock:
                line += "#"
            elif (x, y) in sand:
                line += "o"
            elif (x, y) in flowing:
                line += "~"
            else:
                line += "."
        print(line)


bottom = 0

for line in all_data:
    if len(line) < 3: continue
    add_rock(line.split("->"))

#print(rock)
sand_x = 500
sand_y = 0
bottom += 2

while True:
    if not place_sand():
        break

output(450, 600, 0, bottom)
print("Part 1:", len(sand))

# part 2
sand.clear()

while (sand_x, sand_y) not in sand:
    if not place_sand(True):
        break
print("Part 2:", len(sand))
