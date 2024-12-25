from math import sqrt

pzl_inp = int(input("Enter puzzle input:    "))


def part_1(pzl_inp):
    size = int(1e6)
    houses = [0 for i in range(size)]

    for i in range(1, size):
        for j in range(i, size, i):
            houses[j] += 10 * i

    for i in range(size):
        if houses[i] >= pzl_inp:
            return i


def part_2(pzl_inp):
    size = int(1e6)
    houses = [0 for i in range(size)]

    for i in range(1, size):
        cnt = 0
        for j in range(i, size, i):
            houses[j] += 11 * i
            cnt += 1
            if cnt == 50: break

    for i in range(size):
        if houses[i] >= pzl_inp:
            return i


print("Part 1:", part_1(pzl_inp))
print("Part 2:", part_2(pzl_inp))
