
with open("inputs/Day3.txt") as f:
    all_data = f.read().split("\n")


def valid_tri(tri):
    if tri[0] + tri[1] <= tri[2]: return False
    if tri[2] + tri[1] <= tri[0]: return False
    if tri[0] + tri[2] <= tri[1]: return False
    return True


part1 = 0
col1 = []
col2 = []
col3 = []
for line in all_data:
    line = line.strip()
    if len(line) < 3: continue

    line = list(map(int, line.split()))
    col1.append(line[0])
    col2.append(line[1])
    col3.append(line[2])

    if valid_tri(line):
        part1 += 1

print("Part 1:", part1)

part2 = 0
for i in range(0, len(col1), 3):
    if valid_tri(col1[i:i+3]): part2 += 1
    if valid_tri(col2[i:i+3]): part2 += 1
    if valid_tri(col3[i:i+3]): part2 += 1
print("Part 2:", part2)

