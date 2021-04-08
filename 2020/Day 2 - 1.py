with open('inputs/2.txt', 'r') as f: #open the file
    contents = f.readlines()

v = 0
for line in contents:
    num, l, password = line.split()
    l = l[0]
    minn, maxn = list(map(int, num.split("-")))
    if password.count(l) <= maxn and password.count(l) >= minn: v += 1
print(v)
