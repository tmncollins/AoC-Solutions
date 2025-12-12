import re
from itertools import combinations
from functools import lru_cache
from collections import deque
from pulp import *

f = open('inputs/Day10.txt').read().strip().split('\n')

def min_presses(l, wiring):
    lights = []
    for i in l: lights.append(i=='#')
    for i in range(1, len(wiring)+1):
        for c in combinations(wiring, r=i):
            values = [False for i in range(len(lights))]
            for j in c:
                for k in j: values[k] = not values[k]
            if lights == values: return i

def min_joltage(target_joltage, buttons):
    import pulp

    # --- Problem parameters ---
    N = len(buttons)  # number of variables
    subsets = []
    _subsets = [[] for _ in range(len(target_joltage))]
    for i in range(len(buttons)):
        for j in buttons[i]: _subsets[j].append(i)

    for subset, total in zip(_subsets, target_joltage):
        subsets.append((subset, total))

    # You can add more subsets of the form: (list_of_indices, required_sum)

    # --- Define ILP problem ---
    prob = LpProblem("Minimize_Sum", LpMinimize)

    # --- Create integer variables ---
    x = LpVariable.dicts("x", range(N), lowBound=0, upBound=None, cat=LpInteger)

    # --- Objective: minimize sum of all variables ---
    prob += lpSum([x[i] for i in range(N)]), "TotalSum"

    # --- Add subset equality constraints ---
    for k, (idx_list, rhs_value) in enumerate(subsets):
        prob += lpSum([x[i] for i in idx_list]) == rhs_value, f"Subset_{k}"

    # --- Solve ---
    solver = pulp.PULP_CBC_CMD(msg=0)
    prob.solve(solver)

#    print("Objective value:", value(prob.objective))

    return int(value(prob.objective))

part1 = 0
part2 = 0

idx = 0
for line in f:
#    idx += 1
#    print(f'At {idx} out of {len(f)}')
    lights = re.findall(r"\[(.*?)\]", line)[0]
    wiring = re.findall(r"\((.*?)\)", line)
    joltage = re.findall(r"\{(.*?)\}", line)[0]
    joltage = list(map(int, joltage.split(',')))

    for i in range(len(wiring)):
        wiring[i] = tuple(map(int, wiring[i].split(',')))
    wiring = tuple(wiring)

    m = min_presses(lights, wiring)
    part1 += m

#    print(joltage, wiring)
    j = min_joltage(joltage, wiring)
#    print(j)
    part2 += j

print('Part 1:', part1)
print('Part 2:', part2)
