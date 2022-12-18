
with open("input/5.txt") as f:
    alchemy = f.readline().replace("\n", "")

ALCHEMY = alchemy

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
combust = [lower[i] + upper[i] for i in range(26)]
for i in range(26): combust.append(upper[i] + lower[i])

stable = False
while not stable:
    stable = True
    for c in combust:
        if alchemy.count(c):
            alchemy = alchemy.replace(c, "")
            stable = False

#print(alchemy)
print("Part 1:", len(alchemy))

MIN = 999999
for unit in range(26):
    alchemy = ALCHEMY
    alchemy = alchemy.replace(lower[unit], "").replace(upper[unit], "")

    stable = False
    while not stable:
        stable = True
        for c in combust:
            if alchemy.count(c):
                alchemy = alchemy.replace(c, "")
                stable = False
    MIN = min(MIN, len(alchemy))
#    print(upper[unit], len(alchemy))

print("Part 2:", MIN)

