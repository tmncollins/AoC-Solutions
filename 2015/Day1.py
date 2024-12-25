
with open("inputs/Day1.txt") as f:
    line = f.read().strip()

print("Part 1:", line.count("(") - line.count(")"))

pos = 0
cnt = 0
for i in line:
    cnt += 1
    if i == "(": pos += 1
    elif i == ")":
        pos -= 1
        if pos == -1:
            print("Part 2:", cnt)
            break
