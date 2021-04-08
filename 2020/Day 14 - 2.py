def allPos(n):
    if "X" not in n: return [int(n,2)]
    all = []
    i = n.index("X")
    all += allPos(n[:i] + "1" + n[i+1:])
    all += allPos(n[:i] + "0" + n[i+1:])
    return all

def overwrite(mask, n):
    mask = list(mask[::-1])
    n = bin(n)[2:][::-1]
    for i in range(min(len(n), len(mask))):
        if mask[i] == "0": mask[i] = n[i]
    return "".join(mask[::-1])

with open('inputs/14.txt', 'r') as f: #open the file
    contents = f.readlines()

from _collections import defaultdict

register = defaultdict(int)

mask = ""
for line in contents:
    line = line.split()
    if line[0] == "mask":
        mask = line[2]
    else:
        f = line[0].split("[")
#        print(f)
        f = f[1].replace("]", "")
        allReg = allPos(overwrite(mask, int(f)))
        for i in allReg:
            register[i] = int(line[2])

print(sum(register.values()))
