with open("inputs/Day10.txt") as f:
    all_data = f.read().split("\n")

cycle = 1
x = 1
ans = 0
target = 20
img = "#"
for line in all_data:
    if line == "noop":
        cycle += 1
    elif line == "":
        continue
    else:
        line = line.split()

        if cycle < target and cycle + 2 > target:
            ans += target * x
            target += 40

        if (cycle) % 40 in [x - 1, x, x + 1]:
            img += "#"
        else:
            img += "."

        if (cycle+1) % 40 == 0: img += "\n"

        cycle += 2
        x += int(line[1])

    if cycle-1 == target:
        ans += target * x
#        print(target, x, target * x)
        target += 40

    if (cycle-1) % 40 in [x - 1, x, x + 1]:
        img += "#"
    else:
        img += "."

    if (cycle) % 40 == 0: img += "\n"

print("Part 1:", ans, cycle)
print(img)
# RZHFGJCB