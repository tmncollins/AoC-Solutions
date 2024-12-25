
with open("inputs/Day9.txt", "r") as f:
    data = f.read().replace("\n", "")

#data = "2333133121414131402"

data = list(map(int, list(data)))

data_length = []
blank_length = []
disk = []
counter = 0
EMPTY = -1
space = False
for item in data:
    if space:
        blank_length.append([len(disk), item])
        for _ in range(item):
            disk.append(EMPTY)
    else:
        data_length.append([len(disk), item])
        for _ in range(item):
            disk.append(counter)
        counter += 1
    space = not space

def fragment_1(disk):
    empty_idx = 0
    while True:
        while empty_idx < len(disk) and disk[empty_idx] != EMPTY:
            empty_idx += 1
        if empty_idx >= len(disk): break
        u = disk.pop()
        while u == EMPTY and empty_idx < len(disk):
            u = disk.pop()
        if empty_idx >= len(disk): break
        disk[empty_idx] = u
    return disk

def fragment_2(disk, data_l, blank_l):
    for i in range(len(data_l)-1, -1, -1):
        if i % 100 == 0:
            print(i, len(data_l))
        for j in range(len(blank_l)):
            if blank_l[j][0] >= data_l[i][0]: break
            if data_l[i][1] <= blank_l[j][1]:
                # move here!
                for p in range(data_l[i][1]):
                    disk[blank_l[j][0] + p] = disk[data_l[i][0]]
                for p in range(data_l[i][1]):
                    disk[data_l[i][0] + p] = EMPTY
                blank_l[j][0] += data_l[i][1]
                blank_l[j][1] -= data_l[i][1]
                if blank_l[j][0] <= 0: blank_l.pop(0)
                break
    return disk


disk1 = fragment_1(list(disk))
part1 = 0
for i in range(len(disk1)):
    if disk1[i] > 0:
        part1 += i * disk1[i]

print("Part 1:", part1)

disk2 = fragment_2(list(disk), data_length, blank_length)
part2 = 0
for i in range(len(disk2)):
    if disk2[i] > 0:
        part2 += i * disk2[i]

print(disk2)
print("Part 2:", part2)
