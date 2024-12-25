
with open("inputs/Day5.txt") as file:
    data = file.read().strip().split("\n")

conversions = []

convert = []
seeds = []
for line in data:
    if "seeds" in line:
        line = line.split()[1:]
        seeds = list(map(int, line))
    elif "map" in line:
        if len(convert) > 0:
            conversions.append(convert)
        convert = []
    elif len(line) >= 5:
        convert.append(list(map(int, line.split())))
if len(convert) > 0:
    conversions.append(convert)


def convert_num(n, i):
    for c in conversions[i]:
        if n >= c[1] and n < c[1] + c[2]:
            d = n - c[1]
            return d + c[0]
    return n

def fully_convert_num(n):
    print(n, end=" ")
    for i in range(len(conversions)):
        n = convert_num(n, i)
        print(n, end=" ")
    print()
    return n

part1 = float("inf")
for s in seeds:
    l = fully_convert_num(s)
    part1 = min(part1, l)

print("Part 1:", part1)