from collections import defaultdict

with open("inputs/Day25.txt") as f:
    instructions = f.read().split("\n")

def part1(register):

    ind = 0
    target = 0
    cnt = 0
    while ind < len(instructions):
        instruct = instructions[ind].split()
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
            try:
                a = int(instruct[1])
                if a != 0:
                    ind += int(instruct[2]) - 1
            except:
                if register[instruct[1]] != 0:
                    ind += int(instruct[2]) - 1
        elif instruct[0] == "out":
            if register[instruct[1]] != target: return False
            target += 1
            target %= 2
            cnt += 1
            if cnt == 10: return True

        ind += 1

    return False


i = 0

while True:
    r = defaultdict(int)
    if i % 10 == 0:
        print(i)
    r["a"] = i
    if part1(r):
        print("Part 1:", i)
        break
    i += 1

"""
1   cpy a d         # d = a = inp
2   cpy 4 c         # c = 4
3   cpy 633 b       # b = 633
4   inc d           # d += 1 = inp + 1
5   dec b           # b -= 1 = 632
6   jnz b -2        # essentially d += b = inp + 633 (1)
7   dec c           # c -= 1
8   jnz c -5        # essentially apply (1) 4 times d = inp + 633*4
9   cpy d a         # a = d = inp + 633*4
10  jnz 0 0         # nothing?
11  cpy a b         # b = a
12  cpy 0 a         # a = 0
13  cpy 2 c         # c = 2
14  jnz b 2         # go to 16
15  jnz 1 6         # go to 21
16  dec b           # b -= 1 = a - 1
17  dec c           # c -= 1
18  jnz c -4        # essentially b -= c
19  inc a           # a += 1 = 1
20  jnz 1 -7        # go to 16
21  cpy 2 b         # b = 2
22  jnz c 2
23  jnz 1 4
24  dec b
25  dec c
26  jnz 1 -4        
27  jnz 0 0         # does nothing
28  out b
29  jnz a -19
30  jnz 1 -21

"""