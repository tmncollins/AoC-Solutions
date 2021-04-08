with open('inputs/5.txt', 'r') as f: #open the file
    contents = f.readlines()


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

maxa = 0
for line in contents:
    p = boarding(line)
    if p > maxa: maxa = p


print(maxa)