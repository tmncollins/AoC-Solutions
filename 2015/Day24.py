from math import prod
from functools import lru_cache
import time


def reset():
    global MIN_ITEMS, MIN_QE

    MIN_ITEMS = float("inf")
    MIN_QE = float("inf")


def min_qe(i=0, w=0, num_item=0, qe=1):
    global weights, compartment, MIN_ITEMS, MIN_QE, sum_remaining

    if num_item > MIN_ITEMS: return
    elif num_item == MIN_ITEMS and qe > MIN_QE: return

    if w + sum_remaining[i] < compartment:
        return
#        return float("inf"), float("inf")

    if w == compartment:
        if num_item < MIN_ITEMS:
            MIN_ITEMS = num_item
            MIN_QE = qe
        elif num_item == MIN_ITEMS:
            MIN_QE = min(MIN_QE, qe)
        return
#        return num_item, qe

    if i >= len(weights) or w > compartment:
        return
#        return float("inf"), float("inf")

    min_qe(i+1, w, num_item, qe)
    min_qe(i+1, w+weights[i], num_item+1, qe*weights[i])


with open("inputs/Day24.txt") as f:
    weights = list(map(int, f.read().strip().split("\n")))

sum_remaining = []
weights.sort()
weights.reverse()
sum_remaining.append(sum(weights))
for i in weights:
    sum_remaining.append(sum_remaining[-1] - i)

start = time.time()

reset()
compartment = sum(weights) / 3
min_qe()
print("Part 1:", MIN_QE)

reset()
compartment = sum(weights) / 4
min_qe()
print("Part 2:", MIN_QE)

#print(time.time() - start)

