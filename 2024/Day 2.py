import time
from collections import defaultdict

with open("inputs/Day2.txt", "r") as f:
    all_data = f.read().split("\n")

def increasing(seq):
    for i in range(len(seq)-1):
        if seq[i+1] > seq[i] or abs(seq[i+1] - seq[i]) < 1 or abs(seq[i+1] - seq[i]) > 3: return False
    return True

def decreasing(seq):
    for i in range(len(seq)-1):
        if seq[i+1] < seq[i] or abs(seq[i+1] - seq[i]) < 1 or abs(seq[i+1] - seq[i]) > 3: return False
    return True

def tolerance(seq):
    if increasing(seq) or decreasing(seq): return True
    for i in range(len(seq)):
        seq2 = list(seq)
        seq2.pop(i)
        if increasing(seq2) or decreasing(seq2): return True
    return False

part1 = 0
part2 = 0
for line in all_data:
    line = list(map(int, line.split()))
    if increasing(line) or decreasing(line):
        part1 += 1
    if tolerance(line):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)