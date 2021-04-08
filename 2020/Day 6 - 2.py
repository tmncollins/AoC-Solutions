with open('inputs/6.txt', 'r') as f: #open the file
    contents = f.readlines()

alpha = list("abcdefghijklmnopqrstuvwxyz")
last = []
tot = 0
for line in contents:
    line = list(line.replace("\n", ""))
    if len(line) == 0:
        count = 0
        a = set(alpha)
        for item in last:
            a = a.intersection(item)
        tot += len(a)
        last = []
    else:
        last.append(set(line))

print(tot)