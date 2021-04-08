with open("input/16.txt") as f:
    inp = list(map(int, list(f.readline().replace("\n", ""))))

length = len(inp) * 10000
offset = ""
for item in inp[:7]:
    offset = offset + str(item)
offset = int(offset)
print(offset)
inp = [inp[i%len(inp)] for i in range(offset, length)]
#print(inp)
n = 100
for x in range(n):
    print(x)
    for i in range(1, len(inp))[::-1]: inp[i-1] += inp[i]
    for i in range(len(inp)): inp[i] = inp[i] % 10

print(''.join(map(str, inp[:8])))
