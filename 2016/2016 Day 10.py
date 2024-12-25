from _collections import *

bots = defaultdict(list)
OUTPUT = 100000

with open("inputs/Day10.txt") as f:
    all_data = f.read().split("\n")

instructions = []
comp = [61,17]

for line in all_data:
    line = line.strip()
    if len(line) < 5: continue

    line = line.split()

    if line[0] == "value":
        v = int(line[1])
        b = int(line[5])
        bots[b].append(v)

    elif line[0] == "bot":
        b = int(line[1])
        low = int(line[6])
        if line[5] == "output": low += OUTPUT
        high = int(line[11])
        if line[10] == "output": high += OUTPUT

        instructions.append((b, low, high))

while instructions:
    for b, low, high in instructions:
        if len(bots[b]) == 2:
            min_v = min(bots[b])
            max_v = max(bots[b])
            if min_v == min(comp) and max_v == max(comp):
                print("Part 1:", b)

            bots[low].append(min_v)
            bots[high].append(max_v)
            instructions.remove((b, low, high))
            bots.pop(b)
            break

#print(bots)
part2 = bots[OUTPUT+0][0] * bots[OUTPUT+1][0] * bots[OUTPUT+2][0]
print("Part 2:", part2)