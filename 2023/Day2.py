from collections import defaultdict
from math import *

with open("inputs/Day2.txt") as file:
    data = file.read().split("\n")

red = 12
green = 13
blue = 14

numbers = {"red": red, "green":green, "blue":blue}

part1 = 0
part2 = 0
for line in data:
    id, line = line.split(":")
    possible = True
    max_c = defaultdict(int)
    for hand in line.split(";"):
        for i in hand.split(","):
            n, c = i.split()
            max_c[c] = max(max_c[c], int(n))
            if int(n) > numbers[c]:
                possible = False
    if possible:
        id = int(id.split()[1])
        part1 += id
    part2 += prod(max_c.values())

print("Part 1:", part1)
print("Part 2:", part2)