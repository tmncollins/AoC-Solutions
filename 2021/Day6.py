FISH = [0 for i in range(7)]
toadd = [0, 0]

f = open("Day6.txt")
data = f.read().split("\n")
data = list(map(int, data[0].split(",")))

fish = 0
for i in data:
    FISH[i] += 1
    fish += 1

days = 256
for day in range(days+2):
    d = day % 7
#    print(d, sum(FISH))
    if day == 82: print("Part 1:", sum(FISH))
    toadd.append(FISH[d])
    FISH[d] += toadd.pop(0)

print("Part 2:", sum(FISH))
