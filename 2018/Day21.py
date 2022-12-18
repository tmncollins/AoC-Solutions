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


def run(r, num):

    last = [[] for _ in range(len(r))]

    opcodes = {"addi":addi, "addr":addr, "mulr":mulr, "muli":muli, "banr":banr, "bani":bani, "borr":borr, "bori":bori,
               "gtir":gtir, "gtrr":gtrr, "gtri":gtri, "eqir":eqir, "eqri":eqri, "eqrr":eqrr, "seti":seti, "setr":setr}

    last = 0
    seen = set()
    part1 = False

    while True:
        r[3] = 65536 | r[4]
        r[4] = num

        while True:
            r[2] = 255 & r[3]
            r[4] += r[2]
            r[4] = ((16777215 & r[4]) * 65899) & 16777215

            if 256 > r[3]:
                if not part1:
                    part1 = True
                    print("Part 1:", r[4])
                    seen.add(r[4])
                    break
                else:
                    if r[4] not in seen:
                        seen.add(r[4])
                        last = r[4]
                        break
                    else:
                        print("Part 2:", last)
                        return

            else:
                r[3] = int(r[3] / 256)


instructions = []

with open("input/21.txt") as f:
    all_data = f.read().split("\n")

inp = 0
for line in all_data:
    if len(line) < 4: continue
    if line[:3] == "#ip":
        line = line.split()[1]
        inp = int(line)
    else:
        instructions.append(line)

num = instructions[7].split()[1]
num = int(num)

r = [0 for i in range(6)]

run(r, num)

"""
#ip 5
0  seti 123 0 4        # register 4 = 123
1  bani 4 456 4        # register 4 = 123 & 456
2  eqri 4 72 4         # if register 4 == 72
3  addr 4 5 5          # then go to 5
4  seti 0 0 5          # else go to  0 # infinite loop
5  seti 0 8 4          # register 4 = 0
6  bori 4 65536 3      # register 3 = 65536 | register 4 = 65536
7  seti 707129 0 4     # register 4 = 707129
8  bani 3 255 2        # register 2 = 255 & register 3 = 0
9  addr 4 2 4          # add register 2 to register 4 = 65536
10 bani 4 16777215 4   # register 4 = 16777215 & register 4 = 65536
11 muli 4 65899 4      # times register 4 by 65899 = 4318756864
12 bani 4 16777215 4   # register 4 = 16777215 & register 4 = 7012352
13 gtir 256 3 2        # if 256 > register 3
14 addr 2 5 5          # then go to 16
15 addi 5 1 5          # else go to 17
16 seti 27 6 5         # go to 28
17 seti 0 7 2          # register 2 = 0
18 addi 2 1 1          # register 1 = register 2 + 1 = 1
19 muli 1 256 1        # times register 1 by 256
20 gtrr 1 3 1          # if register 1 > 3 then
21 addr 1 5 5          # go to 23
22 addi 5 1 5          # else go to 24
23 seti 25 2 5         # go to register 26
24 addi 2 1 2          # add 1 to register 2
25 seti 17 1 5         # go to 18
26 setr 2 4 3          # register 3 = register 2
27 seti 7 4 5          # go to 7
28 eqrr 4 0 2          # if register 4 == register 0
29 addr 2 5 5          # then terminate
30 seti 5 2 5          # else go to 6
5120 - 4864
"""
