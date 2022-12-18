def addr(r, a, b, c):
    r[c] = r[a] + r[b]
    return r
def addi(r, a, b, c):
    r[c] = r[a] + b
    return r
def mulr(r, a, b, c):
    r[c] = r[a] * r[b]
    return r
def muli(r, a, b, c):
    r[c] = r[a] * b
    return r
def banr(r, a, b, c):
    r[c] = r[a] & r[b]
    return r
def bani(r, a, b, c):
    r[c] = r[a] & b
    return r
def borr(r, a, b, c):
    r[c] = r[a] | r[b]
    return r
def bori(r, a, b, c):
    r[c] = r[a] | b
    return r
def setr(r, a, b, c):
    r[c] = r[a]
    return r
def seti(r, a, b, c):
    r[c] = a
    return r
def gtir(r, a, b, c):
    r[c] = 1 if a > r[b] else 0
    return r
def gtri(r, a, b, c):
    r[c] = 1 if r[a] > b else 0
    return r
def gtrr(r, a, b, c):
    r[c] = 1 if r[a] > r[b] else 0
    return r
def eqir(r, a, b, c):
    r[c] = 1 if a == r[b] else 0
    return r
def eqri(r, a, b, c):
    r[c] = 1 if r[a] == b else 0
    return r
def eqrr(r, a, b, c):
    r[c] = 1 if r[a] == r[b] else 0
    return r

def get_factors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0: factors.append(i)
    return factors

def run(r, instructions, inp):

    last = [[] for _ in range(len(r))]

    opcodes = {"addi":addi, "addr":addr, "mulr":mulr, "muli":muli, "banr":banr, "bani":bani, "borr":borr, "bori":bori,
               "gtir":gtir, "gtrr":gtrr, "gtri":gtri, "eqir":eqir, "eqri":eqri, "eqrr":eqrr, "seti":seti, "setr":setr}

    cnt = 0
    while r[inp] >= 0 and r[inp] < len(instructions):

        ins = instructions[r[inp]].split()
        opcode, a, b, c = ins
        a, b, c = int(a), int(b), int(c)
        r = opcodes[opcode](r, a, b, c)

        r[inp] += 1

        cnt += 1
        if cnt == 100:
            break

        for i in range(len(r)):
            last[i].append(r[i])
            if len(last[i]) >= 50:
                last[i].pop(0)

    num = 1
    for i in range(len(r)):
        if len(set(last[i])) == 1 and last[i][0] > 50:
            num = last[i][0]
            break

    return num + sum(get_factors(num))


r = [0 for i in range(6)]
r[0] = 1

instructions = []

with open("input/19.txt") as f:
    all_data = f.read().split("\n")

inp = 0
for line in all_data:
    if len(line) < 4: continue
    if line[:3] == "#ip":
        line = line.split()[1]
        inp = int(line)
    else:
        instructions.append(line)

r = [0 for i in range(6)]

print("Part 1:", run(r, instructions, inp))

r = [0 for i in range(6)]
r[0] = 1

print("Part 2:", run(r, instructions, inp))

"""
1  3  6  12  
 +2 +3 +6

#ip 3
0 addi 3 16 3 # go to 17
1 seti 1 3 4 # set 4 to 1
2 seti 1 8 5 # set 5 to 1
3 mulr 4 5 1 # multiply registers 4 and 5, store in register 1 = 1
4 eqrr 1 2 1 # are registers 1 and 2 equal?
5 addr 1 3 3 # if so, go to 7
6 addi 3 1 3 # go to 8
7 addr 4 0 0 # add register 4 to register 0
8 addi 5 1 5 # add 1 to register 5
9 gtrr 5 2 1 # is register 5 > register 2?
10 addr 3 1 3 # if so, go to 12
11 seti 2 6 3 # go to 3
12 addi 4 1 4 # add 1 to register 4
13 gtrr 4 2 1 # is register 4 > register 2?
14 addr 1 3 3 # if so, go to 16 (break)
15 seti 1 1 3 # go to 2
16 mulr 3 3 3 # break
17 addi 2 2 2 # add 2 to register 2 = 2
18 mulr 2 2 2 # sqr register 2 = 4
19 mulr 3 2 2 # times register 2 by register 3 = 76
20 muli 2 11 2 # times register 2 by 11 = 836
21 addi 1 5 1 # add 5 to register 1 = 5
22 mulr 1 3 1 # times register 1 by register 3 = 110
23 addi 1 8 1 # add 8 to register 1 = 118
24 addr 2 1 2 # add register 1 to register 2 = 954
25 addr 3 0 3 # add register 0 to register 3 = 25
26 seti 0 5 3 # go to 1
27 setr 3 9 1
28 mulr 1 3 1
29 addr 3 1 1
30 mulr 3 1 1
31 muli 1 14 1
32 mulr 1 3 1
33 addr 2 1 2
34 seti 0 9 0
35 seti 0 9 3
"""