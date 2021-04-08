with open("input/1.txt") as f:
    inp = f.readlines()

tot = 0
for item in inp:
    a = int(item) // 3
    a -= 2
    tot += a
    while a > 0:
        a = a // 3
        a -= 2
        a = max(0, a)
        tot += a
print(tot)