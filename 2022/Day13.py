from functools import cmp_to_key
from copy import deepcopy
import time

with open("inputs/Day13.txt") as f:
    all_data = f.read().split("\n")


def compare_sort(a,b):
    return compare(deepcopy(a), 0, deepcopy(b), 0)

def compare(a, ptr_a, b, ptr_b):

#    print(a, b)

    if ptr_a >= len(a):
        if ptr_b >= len(b): return 0
        return 1
    if ptr_b >= len(b):
        return -1

    if type(a[ptr_a]) == int:
        if type(b[ptr_b]) == int:
            if a[ptr_a] < b[ptr_b]: return 1
            if a[ptr_a] > b[ptr_b]: return -1
            return compare(a, ptr_a+1, b, ptr_b+1)

        else:
            a[ptr_a] = [a[ptr_a]]
            return compare(a, ptr_a, b, ptr_b)

    else:
        if type(b[ptr_b]) == int:
            b[ptr_b] = [b[ptr_b]]
            return compare(a, ptr_a, b, ptr_b)

        else:
            result = compare(a[ptr_a], 0, b[ptr_b], 0)
            if result == 0:
                return compare(a, ptr_a+1, b, ptr_b+1)
            return result

    return 0

a = -1
b = -1
all_data.append("")

cnt = 0
part1 = 0
all_packets = []

for line in all_data:
    if len(line) < 2:
        if type(a) == list and type(b) == list:
            result = compare(a, 0, b, 0)
            cnt += 1
#            print(a, b, result, cnt)
            if result == 1:
                part1 += cnt
        a = -1
        b = -1

    elif a == -1:
        a = eval(line)
        all_packets.append(a)

    else:
        b = eval(line)
        all_packets.append(b)

print("Part 1:", part1)

all_packets.append([[2]])
all_packets.append([[6]])

#all_packets = sorted(all_packets, key=compare)
all_packets.sort(key=cmp_to_key(compare_sort))
all_packets = all_packets[::-1]

#for item in all_packets:
#    print(item)
try:
    idx_1 = all_packets.index([[2]]) + 1
    idx_2 = all_packets.index([[6]]) + 1
except:
    idx_1 = all_packets.index([[[2]]]) + 1
    idx_2 = all_packets.index([[[6]]]) + 1

print("Part 2:", idx_1 * idx_2)

