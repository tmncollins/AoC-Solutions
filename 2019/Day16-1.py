
with open("input/16.txt") as f:
    inp = list(map(int, list(f.readline().replace("\n", ""))))

base = [0,1,0,-1]
n = 100
for j in range(n):
    print(j)
    newInp = []
    for i in range(len(inp)):
        b = []
        for item in base:
            b += [item for _ in range(i+1)]
#        print(b)
        p = 0
        for j in range(len(inp)):
            p += b[(j+1)%len(b)] * inp[j]
#            print(p)
        p = abs(p)
        newInp.append(p%10)
    inp = list(newInp)
for i in range(8):
    print(inp[i], end="")
#print(inp[offset:offset+8])