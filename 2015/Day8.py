def len_string(s):
    i = 1
    length = 0

    while i < len(s) - 1:
        if s[i] == "\\":
            if s[i+1] == "x":
                i += 3
            else:
                i += 1

        length += 1
        i += 1

    return length


def len_encode(s):
    length = 2

    for char in s:
        if char == "\\" or char == "\"":
            length += 1
        length += 1

    return length


with open("inputs/Day8.txt") as f:
    all_strings = f.read().split("\n")

part1 = 0
part2 = 0
for s in all_strings:
    s = s.strip().replace(" ", "")
    part1 += len(s) - len_string(s)
    part2 += len_encode(s) - len(s)

print("Part 1:", part1)
print("Part 2:", part2)
