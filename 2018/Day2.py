
with open("input/2.txt") as f:
    boxes = f.readlines()

two = set()
three = set()

for check in boxes:
    check = check.replace("\n", "")
    for i in check:
        if check.count(i) == 2: two.add(check)
        if check.count(i) == 3: three.add(check)

print("Part 1:", len(two) * len(three))

for i in range(len(boxes)):
    for j in range(i):
        a = boxes[i]
        b = boxes[j]

        d = 0
        for k in range(len(a)):
            if a[k] != b[k]: d += 1

        if d == 1:
            print("Part 2:", end=" ")
            for k in range(len(a)):
                if a[k] == b[k]: print(a[k], end="")
            print()
