with open("inputs/Day6.txt") as f:
    all_data = f.read().split("\n")

lights = [[0 for _ in range(1000)] for i in range(1000)]
lights2 = [[0 for _ in range(1000)] for i in range(1000)]

for line in all_data:

    if len(line) < 5: continue
    line = line.split()

    if line[0] == "toggle":
        start_x, start_y = list(map(int, line[1].split(",")))
        end_x, end_y = list(map(int, line[3].split(",")))

        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                lights[y][x] = (lights[y][x] + 1) % 2
                lights2[y][x] += 2


    else:

        start_x, start_y = list(map(int, line[2].split(",")))
        end_x, end_y = list(map(int, line[4].split(",")))

        if line[1] == "on":
            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    lights[y][x] = 1
                    lights2[y][x] += 1
        elif line[1] == "off":
            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    lights[y][x] = 0
                    lights2[y][x] = max(0, lights2[y][x] - 1)

all_on = 0
tot_bright = 0
for i in range(1000):
    all_on += lights[i].count(1)
    tot_bright += sum(lights2[i])

print("Part 1:", all_on)
print("Part 2:", tot_bright)
