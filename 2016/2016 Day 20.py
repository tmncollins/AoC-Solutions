data = open("inputs/Day20.txt").read().split("\n")

ranges = []
for line in data:
    r = list(map(int, line.split("-")))
    ranges.append(r)

ranges = sorted(ranges)
i = 1
while i < len(ranges):
    # do ranges intersect?
    if ranges[i][0] - 1 <= ranges[i-1][1]:
        # merge ranges
        newr = [ranges[i-1][0], max(ranges[i][1], ranges[i-1][1])]
        ranges.pop(i-1)
        ranges.pop(i-1)
        ranges.insert(i-1, newr)
    else:
        i+=1

#print(ranges)
print("Part 1:", ranges[0][1]+1)

allowed = 4294967296
#allowed = 10
for r in ranges:
    allowed -= r[1] + 1 - r[0]

print("Part 2:", allowed)