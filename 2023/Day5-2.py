
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
        x = list(map(int, line.split()))
        a = x[0]
        x[0] = x[1]
        x[1] = a
        convert.append(x)
if len(convert) > 0:
    conversions.append(convert)

for i in range(len(conversions)):
    conversions[i] = sorted(conversions[i])

#print(conversions)

def convert_range(range, i):
    ranges = []
    for c in conversions[i]:
#        print(c, range)
        # end of range
        if range[0] > c[0] + c[2]:
            continue
        elif range[1] < c[0]:
            ranges.append(range)
            range = [-1,-1]
            break

        # convert
        elif range[0] >= c[0]:
            if range[1] < c[0] + c[2]:
                # nice and easy
                ranges.append([range[0]-c[0]+c[1], range[1]-c[0]+c[1]])
                range = [-1, -1]
                break
            else:
                ranges.append([range[0]-c[0]+c[1], c[1]+c[2]-1])
                range[0] = c[0] + c[2]
        elif range[1] < c[0] + c[2]:
            ranges.append([range[0], c[0]-1])
            ranges.append([c[1], c[1]+range[1]-c[0]])
            range = [-1, -1]
            break

    if range != [-1, -1]:
        ranges.append(range)

    return ranges

def fully_convert_range(Range):
#    print("Check range", Range)
    ranges = [Range]
    for i in range(len(conversions)):
        new_ranges = []
        for r in ranges:
            nr = convert_range(r, i)
            new_ranges += nr
        ranges = new_ranges
#        print("new_ranges:", ranges)

    return ranges

part2 = float("inf")
for i in range(0, len(seeds), 2):
    ranges = fully_convert_range([seeds[i], seeds[i]+seeds[i+1]-1])
#    print(ranges)
    part2 = min(part2, min(ranges)[0])

print("Part 2:", part2)