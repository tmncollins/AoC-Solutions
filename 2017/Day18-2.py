from _collections import *

regA, regB = defaultdict(int), defaultdict(int)

f = open("inputs/18.txt").read().split("\n")

regB["p"] = 1

qA, qB = deque(), deque()

apause, bpause = False, False
a = 0
b = 0

def get(v, isA):
    try:
        return int(v)
    except:
        if isA: return regA[v]
        else:   return regB[v]

count = 0

def process(line, isA):
    global a, b, apause, bpause, count
    line = line.split()
    cmd = line[0]
    if cmd == "set":
        v = get(line[2], isA)
        if isA: regA[line[1]] = v
        else:   regB[line[1]] = v
    elif cmd == "add":
        v = get(line[2], isA)
        if isA: regA[line[1]] += v
        else:   regB[line[1]] += v
    elif cmd == "mul":
        v = get(line[2], isA)
        if isA: regA[line[1]] *= v
        else:   regB[line[1]] *= v
    elif cmd == "mod":
        v = get(line[2], isA)
        if isA: regA[line[1]] %= v
        else:   regB[line[1]] %= v
    elif cmd == "jgz":
        v = get(line[1], isA)
        j = get(line[2], isA)
        if v > 0:
            if isA: a += j
            else:   b += j
            return
    elif cmd == "snd":
        v = get(line[1], isA)
        if isA:
            qB.append(v)
        else:
            count += 1
            qA.append(v)
    elif cmd == "rcv":
        if isA:
            if len(qA) > 0:
                apause = False
                regA[line[1]] = qA.popleft()
            else:
                apause = True
                return
        else:
            if len(qB) > 0:
                bpause = False
                regB[line[1]] = qB.popleft()
            else:
                bpause = True
                return
    if isA: a += 1
    else:   b += 1



i = 0
while not apause or not bpause:
#    print(i)
#    i += 1
#    print(f[a], f[b])
    if a < len(f):
        process(f[a], True)
    else:
        print("ended")
        apause = True
    if b < len(f):
        process(f[b], False)
    else:
        print("ended")
        bpause = True


print("Part 2:", count)
