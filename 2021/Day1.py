
f = open("Day1.txt")
data = list(map(int, f.read().split("\n")))

inc = 0
for i in range(1, len(data)):
    if (data[i] > data[i-1]): inc += 1

print("Part 1:", inc)

inc = 0
for i in range(3, len(data)):
    if (data[i] > data[i-3]): inc += 1

print("Part 2:", inc)