with open("input/3.txt") as f:
    line1 = f.readline().replace("\n", "").split(",")
    line2 = f.readline().replace("\n", "").split(",")

set1 = set()
set2 = set()
start = (0,0)
curr = start
dist1 = dict()
dist2 = dict()

steps = 0
for item in line1:
    a = item[0]
    b = int(item[1:])
    for i in range(b):
        if a == "R":
            curr = (curr[0] + 1, curr[1])
        if a == "U":
            curr = (curr[0], curr[1] - 1)
        if a == "L":
            curr = (curr[0] - 1, curr[1])
        if a == "D":
            curr = (curr[0], curr[1] + 1)
        set1.add(curr)
        steps += 1
        dist1[curr] = steps

steps = 0
curr = start
for item in line2:
    a = item[0]
    b = int(item[1:])
    for i in range(b):
        if a == "R":
            curr = (curr[0] + 1, curr[1])
        if a == "U":
            curr = (curr[0], curr[1] - 1)
        if a == "L":
            curr = (curr[0] - 1, curr[1])
        if a == "D":
            curr = (curr[0], curr[1] + 1)
        set2.add(curr)
        steps += 1
        dist2[curr] = steps

points = set1.intersection(set2)
smallest = 999999999999999999999999
for item in points:
    dist = dist1[item] + dist2[item]
    if dist < smallest: smallest = dist
print(int(smallest))

