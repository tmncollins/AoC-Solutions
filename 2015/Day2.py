from math import prod

with open("inputs/Day2.txt") as f:
    all_data = f.read().split("\n")


def ribbon(d):
    d = sorted(d)
    return 2*(d[0]+d[1]) + prod(d)


def area(d):
    return 2*(d[0]*d[1] + d[1]*d[2] + d[0]*d[2]) + min([d[0]*d[1], d[1]*d[2], d[0]*d[2]])


tot = 0
r = 0
for line in all_data:
    if "x" not in line: continue

    line = list(map(int, line.split("x")))
    tot += area(line)
    r += ribbon(line)

print("Part 1:", tot)
print("Part 2:", r)