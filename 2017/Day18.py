from _collections import *

with open("inputs/18.txt") as f:
    all_data = f.read().split("\n")

ins = []
for line in all_data:
    if len(line) < 4: continue
    ins.append(line.split())


def get_val(a):
    try:
        return int(a)
    except:
        return reg[a]


reg = defaultdict(int)

ptr = 0
last_snd = -1
while ptr >= 0 and ptr < len(ins):
#    print(ptr, reg)
    if ins[ptr][0] == "snd":
        last_snd = get_val(ins[ptr][1])
    elif ins[ptr][0] == "rcv":
        if get_val(ins[ptr][1]) != 0:
            print("Part 1:", last_snd)
            break
    else:
        cmd, a, b = ins[ptr]
        b = get_val(b)
        if cmd == "add":
            reg[a] += b
        elif cmd == "set":
            reg[a] = b
        elif cmd == "mul":
            reg[a] *= b
        elif cmd == "mod":
            reg[a] %= b
        elif cmd == "jgz":
            if reg[a] > 0:
                ptr += b - 1

    ptr += 1
