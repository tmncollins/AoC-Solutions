from _collections import *

def toggle(instruct):

    if len(instruct) == 2:
        if instruct[0] == "inc":
            instruct[0] = "dec"
        else:
            instruct[0] = "inc"
    else:
        if instruct[0] == "jnz":
            instruct[0] = "cpy"
        else:
            instruct[0] = "jnz"

    return instruct


def get_val(v, registers):
    a = 0
    try:
        a = int(v)
    except:
        a = registers[v]
    return a

def factorial(x):
    if x == 1: return x
    return x * factorial(x-1)


def part1(register, instructions):

    ind = 0
    while ind < len(instructions):
        instruct = instructions[ind]
#        print(instruct)
        if instruct[0] == "cpy":
            try:
                a = int(instruct[1])
                register[instruct[2]] = a
            except:
                register[instruct[2]] = register[instruct[1]]
        elif instruct[0] == "inc":
            register[instruct[1]] += 1
        elif instruct[0] == "dec":
            register[instruct[1]] -= 1
        elif instruct[0] == "jnz":
            a = get_val(instruct[1], register)
            if a != 0:
                ind += get_val(instruct[2], register) - 1
        elif instruct[0] == "tgl":
            tgl = ind + get_val(instruct[1], register)
            if tgl >= 0 and tgl < len(instructions):
                print("toggle", tgl)
                instructions[tgl] = toggle(instructions[tgl])

        print(ind, registers, instruct)
        ind += 1

        if ind == 18: input()

    return register["a"]

registers = defaultdict(int)
registers["a"] = 7

with open("inputs/Day23.txt") as f:
    all_data = f.read().split("\n")

instructions = []
for line in all_data:
    line = line.strip()
    if len(line) <= 3: continue
    instructions.append(line.split())

a = int(instructions[19][1])
b = int(instructions[20][1])
add = a*b

print("Part 1:", factorial(7) + add)
print("Part 1:", factorial(12) + add)


#print(part1(registers, instructions))


"""
1   cpy a b     # b = a
2   dec b       # b -= 1
3   cpy a d     # d = a
4   cpy 0 a     # a = 0
5   cpy b c     # c = b
6   inc a       # a += 1 = 1
7   dec c       # c -= 1
8   jnz c -2    # essentially, a += c (1)
9   dec d       # d -= 1
10  jnz d -5    # essentially, (1) * d
11  dec b       # b -= 1
12  cpy b c     # c = b
13  cpy c d     # d = c
14  dec d       # d -= 1
15  inc c       # c += 1
16  jnz d -2    # essentially, c = 2*b
17  tgl c       # toggle 27, does nothing
18  cpy -16 c   # c = -16
19  jnz 1 c     # go to 3
20  cpy 73 c    # c = 73
21  jnz 71 d    # d = 71
22  inc a       # a += 1
23  inc d       # d -= 1
24  jnz d -2    # essentially, a += d (3)
25  inc c       # 
26  jnz c -5    # essentially, (3) * c
"""
