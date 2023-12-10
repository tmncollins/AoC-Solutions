from _collections import *

with open("inputs/Day6.txt") as f:
    all_data = f.read().split("\n")

counters = []

for line in all_data:
    line = line.strip()
    if len(line) < 5: continue

    if len(counters) == 0:
        counters = [defaultdict(int) for _ in range(len(line))]

    for i in range(len(line)):
        counters[i][line[i]] += 1

code = ""
code2 = ""
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(counters)):

    best = 0
    best_c = ""
    worst = float("inf")
    worst_c = ""

    for c in alpha:
        if counters[i][c] > best:
            best = counters[i][c]
            best_c = c
        if counters[i][c] > 0 and counters[i][c] < worst:
            worst = counters[i][c]
            worst_c = c

    code += best_c
    code2 += worst_c

print("Part 1", code)
print("Part 2", code2)
