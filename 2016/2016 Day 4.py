
with open("inputs/Day4.txt") as f:
    all_data = f.read().split("\n")

alpha = "abcdefghijklmnopqrstuvwxyz"

def decrypt(name, id):
    acc_name = ""

    for c in name:
        if c in alpha:
            i = alpha.index(c) + id
            i %= len(alpha)
            acc_name += alpha[i]

        else:
            acc_name += c

    return acc_name


def valid_room(room):
    global alpha

    a, b = room.replace("]", "").split("[")
    b = set(b)
    if len(b) != 5: return 0, ""

    a = a.split("-")
    id = int(a[-1])
    a = "-".join(a[:-1])

    cnt = []
    for c in alpha:
        cnt.append((-a.count(c), c))

    cnt.sort()

    for i in range(5):
        if cnt[i][1] not in b: return 0, ""

    return id, decrypt(a, id)


part1 = 0
for line in all_data:
    line = line.strip()
    if len(line) < 5: continue

    id, name = valid_room(line)
    part1 += id
    if "pole" in name:
        print("Part 2:", name, id)


print("Part 1:", part1)