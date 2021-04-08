with open('inputs/5.txt', 'r') as f: #open the file
    contents = f.readlines()


ids = set()
for row in range(128):
    for col in range(8):
        ids.add(row * 8 + col)

def boarding(id):
    min = 0
    max = 128
    for i in id[:7]:
        dif = max - min
        if i == "F":
            max -= dif // 2
        else:
            min += dif // 2
    row = min
    min = 0
    max = 8
    for i in id[7:]:
        dif = max - min
        if i == "L":
            max -= dif // 2
        else:
            min += dif // 2
    col = min
    return row * 8 + col

for line in contents:
    p = boarding(line)
    ids.remove(p)

for id in ids:
    if id + 1 not in ids and id - 1 not in ids:
        print(id)

