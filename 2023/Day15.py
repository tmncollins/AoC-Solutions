from _collections import defaultdict

def hash(string):
    val = 0
    for i in string:
        val += ord(i)
        val *= 17
        val %= 256
    return val

with open("inputs/Day15.txt") as file:
    data = file.read().strip().replace("\n","").split(",")

part1 = 0
for i in data: part1 += hash(i)
print("Part 1:", part1)

boxes = defaultdict(list)
foci = defaultdict(int)
for i in data:
    if "=" in i:
        label, lens = i.split("=")
        box = hash(label)
        lens = int(lens)
        if label not in boxes[box]:
            boxes[box].append(label)
        foci[(box, label)] = lens
    elif "-" in i:
        label = i[:-1]
        box = hash(label)
        if label in boxes[box]:
            boxes[box].remove(label)

part2 = 0
for box in range(256):
    for i in range(len(boxes[box])):
        part2 += (box+1) * (i+1) * foci[(box, boxes[box][i])]

print("Part 2:", part2)


