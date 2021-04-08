from math import prod

with open('inputs/3.txt', 'r') as f: #open the file
    slope = list(f.readlines())

for i in range(len(slope)):
    slope[i] = slope[i].replace("\n", "")

right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

i = 0
ans = []
for i in range(len(right)):
    y = 0
    x = 0
    trees = 0
    while y < len(slope):
        if slope[y][x] == "#": trees += 1
        y += down[i]
        x += right[i]
        x = x % len(slope[0])
    ans.append(trees)
print(ans)
print(prod(ans))
