def output(lights):
    global width, height

    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in lights:
                line += "#"
            else:
                line += "."
        print(line)


with open("inputs/Day18.txt") as f:
    all_data = f.read().split("\n")

lights = set()

for y in range(len(all_data)):
    for x in range(len(all_data[y])):
        if all_data[y][x] == "#":
            lights.add((x,y))

moves = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
height = 100
width = 100
corners = {(0, 0), (0, height-1), (width-1, 0), (width-1, height-1)}


def run(lights, rounds=100, part2 = False):
    global width, height, corners

    lights = set(lights)

    for i in range(rounds):

        new_lights = set()

        for y in range(height):
            for x in range(width):
                if part2 and (x,y) in corners:
                    new_lights.add((x,y))
                    continue

                cnt = 0
                for dx, dy in moves:
                    if (x+dx, y+dy) in lights:
                        cnt += 1

                if (x,y) in lights:
                    if cnt == 2 or cnt == 3:
                        new_lights.add((x,y))
                else:
                    if cnt == 3:
                        new_lights.add((x,y))

        lights = new_lights

    return len(lights)


print("Part 1:", run(lights, 100))

for item in corners: lights.add(item)
print("Part 2:", run(lights, 100, True))
