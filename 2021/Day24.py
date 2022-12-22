from math import prod
from _collections import *

div_z = []
add_y = []
add_x = []
max_z = []

# run instructions with no input to get
# div_z, add_y, add_x
def run(instructions):
    global add_x, div_z, add_y
    inp = "79197919993985"

    r = defaultdict(int)
    last_line = []
    for line in instructions:
        if len(line) < 3: continue
        line = line.split()
        if line[0] == "add":
            try: v = int(line[2])
            except: v = r[line[2]]
            if line[1] == "y" and line[2] not in "xywz" and last_line == ["add", "y", "w"]:
                add_y.append(v)
            if line[1] == "x" and line[2] not in "xywz" and last_line[0] == "div" and last_line[1] == "z":
                add_x.append(v)
            r[line[1]] += v
        elif line[0] == "mul":
            try: v = int(line[2])
            except: v = r[line[2]]
            r[line[1]] *= v
        elif line[0] == "div":
            try: v = int(line[2])
            except: v = r[line[2]]
            if line[1] == "z" and line[2] not in "xywz":
                div_z.append(v)
            r[line[1]] = int(r[line[1]] / v)
        elif line[0] == "mod":
            try: v = int(line[2])
            except: v = r[line[2]]
            r[line[1]] %= v
        elif line[0] == "eql":
            try: v = int(line[2])
            except: v = r[line[2]]
            r[line[1]] = 1 if r[line[1]] == v else 0
        elif line[0] == "inp":
            r[line[1]] = int(inp[0])
            inp = inp[1:]
        last_line = line
    print(r)


with open("inputs/Day24.txt") as f:
    all_data = f.read().split("\n")
    run(all_data)
print(add_x)
print(add_y)
print(div_z)


# z value must reduce whenever 26 comes up

valid = {("", 0)}

f = open("inputs/Day24.txt").read().split("\n")

# each section has an order of instructions
# inp w
# x = (z % 26) + add_x
# z = z // div_z
# if x != w:
#   y = 26
# else:
#   y = 1
# z = z * y
# y = (w + add_y) * x
# z = z + y

# we want z = 0 at the end, so after every div_z = 26, z must be less than the prod of the remaining div_z

# valid dictionaries for values of z and what numbers they correspond to (maximum poss, and minimum poss, respectively)
valid_max, valid_min = defaultdict(str), defaultdict(str)
remaining_div = prod(div_z)
print(remaining_div)
valid_max[0], valid_min[0] = "", ""
for i in range(14):
    v2_max = defaultdict(str)
    remaining_div = remaining_div // div_z[i]
    for z in valid_max:
        # check each possible new digit
        for w in range(1, 10):
            z2 = z // div_z[i]
            if w != (z % 26) + add_x[i]:
                z2 *= 26
                z2 += w + add_y[i]
            # prune options where z is too large to go to 0
            if z2 <= remaining_div:
                v2_max[z2] = max(v2_max[z2], valid_max[z] + str(w))
    valid_max = v2_max

    # do the same for minimum
    v2_min = defaultdict(str)
    for z in valid_min:
        for w in range(1, 10):
            z2 = z // div_z[i]
            if w != (z % 26) + add_x[i]:
                z2 *= 26
                z2 += w + add_y[i]
            # prune options where z is too large to go to 0
            if z2 <= remaining_div:
                if v2_min[z2] == "": v2_min[z2] = valid_min[z] + str(w)
                else: v2_min[z2] = min(v2_min[z2], valid_min[z] + str(w))
    valid_min = v2_min
    #print(i, len(valid_max.keys()), len(valid_min.keys()))

print("Part 1:", valid_max[0])
print("Part 2:", valid_min[0])
