with open('inputs/13.txt', 'r') as f: #open the file
    contents = f.readlines()

n = int(contents[0])
bus = contents[1].split(",")
b = []
m = 0
for i in bus:
    if i.isnumeric():
        b.append(i)
        if int(i) > int(m):
            m = i

m = b[0]
mindex = 0
dist = []
print(mindex)
for item in b:
    if item != m:
        dist.append((int(item), int(item) - ((bus.index(item) - mindex) % int(item))))

v = 0
m = int(m)
print(dist)
prod = m
while dist:
    v += prod
    if v % dist[0][0] == dist[0][1]:
        prod *= dist[0][0]
        dist.pop(0)
        print(v, prod)

print(v)



