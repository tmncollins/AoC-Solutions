import time
from collections import defaultdict

with open("inputs/Day5.txt", "r") as f:
    all_data = f.read().split("\n")

while len(all_data[0]) < 5: all_data.pop(0)

start = -1
num_stacks = 0
stacks = defaultdict(str)
for i in range(len(all_data)):
    cnt = 1
    for j in range(1, len(all_data[i]), 4):
        num_stacks = max(num_stacks, cnt)
        if all_data[i][j] == "1":
            start = i+2
            break
        if all_data[i][j] != " ":
            stacks[cnt] += all_data[i][j]
        cnt += 1
    if start != -1:
        break

stacks2 = dict(stacks)

for i in range(start, len(all_data)):
    line = all_data[i]
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
for i in range(1, num_stacks):
    msg += stacks[i][0]
for i in range(1, num_stacks):
    msg2 += stacks2[i][0]

print("Part 1:", msg)
print("Part 2:", msg2)