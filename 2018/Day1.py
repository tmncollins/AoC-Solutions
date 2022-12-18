
with open("input/1.txt") as f:
    freq = f.readlines()

v = 0
for item in freq:
    v += int(item)
print("Part 1:", v)

v = 0
seen = set()
found = False

while not found:
    for item in freq:
        seen.add(v)
        v += int(item)
        if v in seen:
            print("Part 2:", v)
            found = True
            break