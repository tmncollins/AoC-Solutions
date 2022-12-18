
all_data = ""
with open("inputs/Day1.txt", "r") as f:
    all_data = f.readlines()

cal = 0
ans = []
for line in all_data:
    try:
        cal += int(line)

    except:
        ans.append(cal)
        cal = 0

ans = sorted(ans)
print("Part 1:", ans[-1])
print("Part 2:", sum(ans[-3:]))