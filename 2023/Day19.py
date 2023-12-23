from copy import deepcopy
from math import *

with open("inputs/Day19.txt") as file:
    data = file.read().strip().split("\n")

parts = []
checks = dict()
val = {"x":0, "m":1, "a":2, "s":3}

for line in data:
    if len(line) < 5: continue

    if line[0] == "{":
        line = line.replace("{", "").replace("}", "").replace("x=", "").replace("m=", "").replace("a=", "").replace("s=", "")
        line = list(map(int, line.split(",")))
        parts.append(line)

    else:
        name, line = line.replace("}", "").split("{")
        line = line.split(",")
        op = []
        for i in line:
            if "<" in i or ">" in i:
                a,b,c = i.replace("<", ":").replace(">", ":").split(":")
                b = int(b)
                a = val[a]
                if "<" in i: o = 0
                else: o = 1
                op.append([a,o,b,c])
            else:
                op.append([i])
        checks[name] = op

def process(part, op="in"):
    workflow = checks[op]
    for i in workflow:
        if len(i) == 1:
            i = i[0]
            if i == "A": return True
            if i == "R": return False
            return process(part, i)
        else:
            if i[1] == 0: # less than
                if part[i[0]] < i[2]:
                    if i[3] == "A": return True
                    if i[3] == "R": return False
                    return process(part, i[3])
            else: # greater than
                if part[i[0]] > i[2]:
                    if i[3] == "A": return True
                    if i[3] == "R": return False
                    return process(part, i[3])


valid = []


def add_valid(ranges):
    valid.append(ranges)


def part_two(ranges, op="in"):
    workflow = checks[op]
    for i in workflow:
        if len(i) == 1:
            i = i[0]
            if i == "A":
                add_valid(ranges)
            elif i == "R": pass
            else:
                part_two(ranges, i)
        else:
            if i[1] == 0: # less than
                new_ranges = deepcopy(ranges)
                a, b = new_ranges[i[0]]
                b = min(b, i[2] - 1)
                if b >= a:
                    new_ranges[i[0]] = (a, b)
                    if i[3] == "A":
                        add_valid(new_ranges)
                    elif i[3] == "R": pass
                    else:
                        part_two(new_ranges, i[3])
                a, b = ranges[i[0]]
                a = max(a, i[2])
                if b >= a:
                    ranges[i[0]] = (a, b)
                else:
                    return
            else: # greater than
                new_ranges = deepcopy(ranges)
                a, b = new_ranges[i[0]]
                a = max(a, i[2] + 1)
                if b >= a:
                    new_ranges[i[0]] = (a, b)
                    if i[3] == "A":
                        add_valid(new_ranges)
                    elif i[3] == "R": pass
                    else:
                        part_two(new_ranges, i[3])
                a, b = ranges[i[0]]
                b = min(b, i[2])
                if b >= a:
                    ranges[i[0]] = (a, b)
                else:
                    return



part1 = 0
for part in parts:
    if process(part):
#        print(part)
        part1 += sum(part)

print("Part 1:", part1)

part_two([(1,4000), (1,4000), (1,4000), (1,4000)])

part2 = 0
for item in valid:
    x = []
    for a,b in item:
        x.append(b + 1 - a)
    part2 += prod(x)

print("Part 2:", part2)

