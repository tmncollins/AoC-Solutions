with open('inputs/2.txt', 'r') as f: #open the file
    contents = f.readlines()

v = 0
for line in contents:
    num, l, password = line.split()
    l = l[0]
    minn, maxn = list(map(int, num.split("-")))
    c = 0
    if password[minn-1] == l: c += 1
    if password[maxn-1] == l: c += 1
    if c == 1: v += 1
print(v)
