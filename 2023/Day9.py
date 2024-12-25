


def get_diff(seq):
    diff = []
    for i in range(1, len(seq)):
        diff.append(seq[i] - seq[i-1])
    return diff

def get_next(seq):
    diff = get_diff(seq)
    if len(set(diff)) == 1 and diff[0] == 0:
        return seq[-1]
    else:
        return seq[-1] + get_next(diff)

def get_prev(seq):
    diff = get_diff(seq)
    if len(set(diff)) == 1 and diff[0] == 0:
        return seq[0]
    else:
        return seq[0] - get_prev(diff)

with open("inputs/Day9.txt") as file:
    data = file.read().strip().split("\n")

part1 = 0
part2 = 0
for line in data:
    if len(line) > 3:
        line = list(map(int, line.split()))
        part1 += get_next(line)
        part2 += get_prev(line)

print(part1)
print(part2)