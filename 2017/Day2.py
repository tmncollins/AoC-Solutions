with open("inputs/2.txt") as f:
    spreadsheet = f.read().split("\n")

part1 = 0
part2 = 0
for line in spreadsheet:
    line = list(map(int, line.split()))
    part1 += max(line) - min(line)

    for i in range(len(line)):
        for j in range(i):
            if line[i] % line[j] == 0:
                part2 += line[i] // line[j]
            if line[j] % line[i] == 0:
                part2 += line[j] // line[i]

print("Part 1:", part1)
print("Part 2:", part2)