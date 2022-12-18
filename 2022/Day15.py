with open("inputs/Day15.txt") as f:
    all_data = f.read().split("\n")

sensors = []
beacons = set()

for line in all_data:
    if len(line) < 5: continue
    line = line.split()
    x1 = int(line[2].replace(",", "").replace("x=", ""))
    y1 = int(line[3].replace(":", "").replace("y=", ""))

    x2 = int(line[8].replace(",", "").replace("x=", ""))
    y2 = int(line[9].replace(":", "").replace("y=", ""))

    sensors.append(((x1,y1), (x2,y2)))
    beacons.add((x2, y2))


def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def get_range(sensor, row):
    s, d = sensor
    d -= abs(row - s[1])
    if d < 0: return None
    return s[0] - d, s[0] + d


def get_overlap(range1, range2):
    left = min(min(range1), min(range2))
    right = max(max(range1), max(range2))

    return left, right


def overlap(range1, range2):
    if min(range2) < min(range1): return overlap(range2, range1)
    if min(range2) <= max(range1) + 1: return True


def len_range(r):
    return max(r) + 1 - min(r)


target_row = 2000000

def get_ranges_in_row(target_row):
    ranges = []

    for b in sensors:
        r = get_range(b, target_row)
        if r:
            ranges.append(r)

    ranges = sorted(ranges)
    new_range = []
    for r in ranges:
        if len(new_range) == 0: new_range.append(r)
        else:
            if overlap(new_range[-1], r):
                new_range[-1] = get_overlap(new_range[-1], r)
            else:
                new_range.append(r)

    return new_range


for i in range(len(sensors)):
    sensors[i] = (sensors[i][0], dist(sensors[i][0], sensors[i][1]))

new_range = get_ranges_in_row(target_row)
part1 = 0
for r in new_range:
    part1 += len_range(r)

for b in beacons:
    if b[1] == target_row:
        part1 -= 1

print("Part 1:", part1)


def find_beacons(minx, maxx, miny, maxy):

    for row in range(miny, maxy + 1):
        r = get_ranges_in_row(row)
        while max(r[0]) < minx: r.pop(0)
        if min(r[0]) < minx: r[0] = (minx, max(r[0]))
        while min(r[-1]) > maxx: r.pop()
        if max(r[-1]) > maxx: r[-1] = (min(r[-1]), maxx)

        if row % 100000 == 0:
            print(row)

        if len(r) <= 1: continue


        for i in range(len(r)-1):
            if max(r[i])+1 < min(r[i+1]):
                return (max(r[i])+1, row)


# part 2
pos = find_beacons(0, 4000000, 0, 4000000)
print("Part 2:", pos[1] + pos[0]*4000000)