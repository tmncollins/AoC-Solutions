with open("inputs/4.txt") as file:
    all_data = file.read().split("\n")

part1 = 0
part2 = 0

for line in all_data:
    line = line.split()
    l2 = set(line)
    if len(line) == len(l2) and len(line) != 0: part1 += 1

    line = ["".join(sorted(item)) for item in line]
    l2 = set(line)
    if len(line) == len(l2) and len(line) != 0: part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
