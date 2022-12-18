from _collections import defaultdict

f = open("inputs/23.txt")
ins = f.read().split("\n")

reg = defaultdict(int)

pos = 0

def output():
    print(reg["a"], reg["b"], reg["c"], reg["d"], reg["e"], reg["f"], reg["g"], reg["h"])

ans = 0

while pos < len(ins):
    line = ins[pos].split(" ")
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

print("Part 1:", ans)
