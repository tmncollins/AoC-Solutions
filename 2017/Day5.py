with open("inputs/5.txt") as f:
    all_data = f.read().split("\n")

REG = []
for line in all_data:
    if line != "":
        REG.append(int(line))

reg = list(REG)
ptr = 0
cnt = 0

while ptr >= 0 and ptr < len(reg):
    cnt += 1
    reg[ptr] += 1
    ptr += reg[ptr]-1

print("Part 1:", cnt)

reg = list(REG)
ptr = 0
cnt = 0

while ptr >= 0 and ptr < len(reg):
    cnt += 1
    if reg[ptr] >= 3:
        reg[ptr] += -1
        ptr += reg[ptr]+1
    else:
        reg[ptr] += 1
        ptr += reg[ptr]-1

print("Part 2:", cnt)
