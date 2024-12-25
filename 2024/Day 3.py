import time
from collections import defaultdict

with open("inputs/Day3.txt", "r") as f:
    all_data = f.read().replace("\n", "")

def process_mul(text):
#    print(text)
    try:
        a,b = text.split(",")
        a = int(a)
        b = int(b)
        return a*b
    except:
        return 0

def process(data, part2=False):
    idx = 0
    ans = 0
    mul = True
    while idx < len(data):
        if part2:
            if data[idx:idx+4] == "do()": mul = True
            if data[idx:idx+7] == "don't()": mul = False
        if data[idx:idx+4] == "mul(" and mul:
            idx2 = idx+4
            while data[idx2] != ")": idx2 += 1
            v = process_mul(data[idx+4:idx2])
            if v:
                idx = idx2
                ans += v
        idx += 1
    return ans

print("Part 1", process(all_data))
print("Part 2", process(all_data, True))

