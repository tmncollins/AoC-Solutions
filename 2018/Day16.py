with open("input/16.txt") as f:
    all_data = f.read().split("\n")

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

codes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
opcodes = [{j for j in range(16)} for i in range(16)]

before = []
after = []
program = []
part1 = 0
line_ptr = 0

for line in all_data:

    line_ptr += 1
    if line == "":

        if before == []:
            break # finished

        # execute
        pos_code = 0
        for o in range(len(codes)):
            opcode = codes[o]
            output = opcode(list(before), program[1], program[2], program[3])
            if output == after:
                pos_code += 1
            elif o in opcodes[program[0]]:
                opcodes[program[0]].remove(o)

        if pos_code >= 3: part1 += 1

        # reset
        before = []
        after = []
        program = []

    elif len(before) == 0:
        line = line.replace("Before: ", "")
        line = line.replace("[", "").replace("]", "").split(",")
        before = list(map(int, line))

    elif program == []:
        program = list(map(int, line.split()))

    else:
        line = line.replace("After: ", "")
        line = line.replace("[", "").replace("]", "").split(",")
        after = list(map(int, line))

print("Part 1:", part1)

while True:
    done = True

    for c in opcodes:
        if len(c) == 1:
            code = list(c)[0]
            for i in range(len(opcodes)):
                if len(opcodes[i]) > 1 and code in opcodes[i]:
                    opcodes[i].remove(code)
        else:
            done = False

    if done: break

for i in range(len(opcodes)):
    opcodes[i] = codes[list(opcodes[i])[0]]

# run
r = [0, 0, 0, 0]

for i in range(line_ptr, len(all_data)):
    line = all_data[i]
    if len(line) > 4:
        program = list(map(int, line.split()))
        r = opcodes[program[0]](r, program[1], program[2], program[3])

print("Part 2:", r[0])