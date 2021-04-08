with open('inputs/13.txt', 'r') as f: #open the file
    contents = f.readlines()

n = int(contents[0])
bus = contents[1].split(",")
b = set()
for i in bus:
    if i.isnumeric():
        b.add(int(i))

best = float("inf")
score = 0

for i in b:
    x = n % i
    x = i - x
    print(i, x)
    if x < best:
        best = x
        score = i * x

print(score)
