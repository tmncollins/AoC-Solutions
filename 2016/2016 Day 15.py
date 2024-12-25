
with open("inputs/Day15.txt") as f:
    all_data = f.read().split("\n")

discs = []
start = []

for line in all_data:
    if len(line) < 5: continue

    line = line.split()
    d = int(line[3])
    s = int(line[-1].replace(".", ""))
    discs.append(d)
    start.append(s)


def run():
    time = 0
    while True:
        passed = True
        for i in range(0, len(discs)):
            next = (start[i] + time+i+1) % discs[i]
            if next != 0:
                passed = False
                break
        if passed:
            return time
        time += 1


print("Part 1:", run())
start.append(0)
discs.append(11)
print("Part 2:", run())
