# checking how many of numbers 108100 -> 125100 are prime adding 17 each time

from math import *

from _collections import defaultdict

f = open("inputs/23.txt", "r")
ins = f.read().split("\n")

reg = defaultdict(int)

pos = 0

def output():
    print(reg["a"], reg["b"], reg["c"], reg["d"], reg["e"], reg["f"], reg["g"], reg["h"])

ans = 0

# part 2
reg["a"] = 1

cnt = 0
while pos < len(ins) and cnt < 50:
    line = ins[pos].split(" ")
    cnt += 1
#    print(line)
    cmd, r, v = line[0], line[1], line[2]
    try:
        v = int(v)
    except:
        v = reg[v]
    if (cmd == "set"):
        reg[r] = int(v)
    elif cmd == "sub":
        reg[r] -= int(v)
    elif cmd == "mul":
        ans += 1
        reg[r] *= int(v)
    elif cmd == "jnz":
        try:
            r = int(r)
        except:
            r = reg[r]
        if (r != 0):
            pos += int(v) - 1

    pos += 1
#    output()
#    input()

def isPrime(n):
    for i in range(2, n // 2):
        if n % i == 0: return False
    return True

ans = 0
start = reg["b"]
end = reg["c"]
for i in range(start, end+1, 17):
    if not isPrime(i): ans += 1
print("Part 2:", ans)

"""
1  set b 67         # b = 67
2  set c b          # c = b = 67
3  jnz a 2          # jump to 5
4  jnz 1 5          
5  mul b 100        # b *- 100 = 6700
6  sub b -100000    # b += 100000 = 106700
7  set c b          # c = b = 106700
8  sub c -17000     # c += 17000 = 123700
9  set f 1          # f = 1
10 set d 2          # d = 2
11 set e 2          # e = 2
12 set g d          # g = d = 2
13 mul g e          # g *= e = 4
14 sub g b          # if g != b:
15 jnz g 2          #   jump to 17
16 set f 0          # f = 0
17 sub e -1         # e += 1
18 set g e          # g = e
19 sub g b          # if e != b:
20 jnz g -8         #   jump to 12
21 sub d -1         # d += 1
22 set g d          # g = d
23 sub g b          # if d != b:
24 jnz g -13        #   jump to 11
25 jnz f 2          # if f != 0:
                    #   jump to 27
26 sub h -1         # h += 1            h is added to if f = 0      f = 0 if b is not prime
27 set g b          # g = b
28 sub g c          # if b != c:
29 jnz g 2          #   jump to 31
30 jnz 1 3          # terminate
31 sub b -17        # b += 17
32 jnz 1 -23        # jump to 9
"""