with open('inputs/14.txt', 'r') as f: #open the file
    contents = f.readlines()

from _collections import defaultdict

register = defaultdict(int)

def bitMask(n, mask):
    n = bin(n)[2:][::-1]
    mask = list(mask[::-1])
    for i in range(min(len(mask), len(n))):
        if mask[i] == "X":
            mask[i] = n[i]
    return int("".join(mask[::-1]).replace("X", "0"), 2)

mask = ""
for line in contents:
    line = line.split()
    if line[0] == "mask":
        mask = line[2]
    else:
        f = line[0].split("[")
        print(f)
        f = f[1].replace("]", "")
        register[int(f)] = bitMask(int(line[2]), mask)

print(sum(register.values()))