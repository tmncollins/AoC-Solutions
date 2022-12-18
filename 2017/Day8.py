from collections import *

with open("inputs/8.txt") as f:
    all_data = f.read().split("\n")

reg = defaultdict(int)

def neq(a, b):
    return a != b
def gre(a, b):
    return a >= b
def grt(a, b):
    return a > b
def les(a, b):
    return a < b
def lee(a, b):
    return a <= b
def eql(a, b):
    return a == b

operators = {"!=":neq, ">=":gre, ">":grt, "==":eql, "<":les, "<=":lee}
highest = 0

for line in all_data:
    if len(line) < 5: continue

    func, cond = line.split("if")

    cond = cond.strip().split()
    r = reg[cond[0]]
    if operators[cond[1]](r, int(cond[2])):
        func = func.strip().split()
        v = int(func[2])
        if func[1] == "inc":
            reg[func[0]] += v
        else:
            reg[func[0]] -= v
        highest = max(highest, reg[func[0]])

print("Part 1:", max(reg.values()))
print("Part 1:", highest)
