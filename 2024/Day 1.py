import time
from collections import defaultdict

with open("inputs/Day1.txt", "r") as f:
    all_data = f.read().split("\n")

left = []
right = []
for line in all_data:
    x,y = list(map(int, line.split()))
    left.append(x)
    right.append(y)
left = sorted(left)
right= sorted(right)

part1 = 0
for i in range(len(left)):
    part1 += abs(left[i]-right[i])

part2 = 0
for item in left:
    part2 += item * right.count(item)

print("Part 1:", part1)
print("Part 2:", part2)
