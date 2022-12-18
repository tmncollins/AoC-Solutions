
with open("inputs/Day5.txt", "r") as f:
    all_data = f.readlines()

stacks = [" ", "RQGPCF", "PCTW", "CMPHB", "RPMSQTL", "NGVZJHP", "JPD", "RTJFZPGL", "JTPFCHLN", "WCTHQZVG"]
stacks2 = [" ", "RQGPCF", "PCTW", "CMPHB", "RPMSQTL", "NGVZJHP", "JPD", "RTJFZPGL", "JTPFCHLN", "WCTHQZVG"]
#stacks = [" ", "NZ", "DCM", "P"]

for line in all_data:
    line = line.replace("\n", "").split()
    a, b, c = list(map(int, [line[1], line[3], line[5]]))
    # part 1
    start = stacks[b]
    move = start[:a][::-1]
    stacks[b] = stacks[b][a:]
    stacks[c] = move + stacks[c]
    # part 2
    stacks2[c] = stacks2[b][:a] + stacks2[c]
    stacks2[b] = stacks2[b][a:]

msg = ""
msg2 = ""
for s in stacks:
    msg += s[0]
for s in stacks2:
    msg2 += s[0]

print("Part 1:", msg)
print("Part 1:", msg2)


