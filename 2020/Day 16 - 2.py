with open('inputs/16 - 1.txt', 'r') as f: #open the file
    rules = f.readlines()
with open('inputs/16 - 2.txt', 'r') as f: #open the file
    tickets = f.readlines()

ranges = []
names = []
myTicket = list(map(int, "61,151,59,101,173,71,103,167,127,157,137,73,181,97,179,149,131,139,67,53".split(",")))

def inRange(n,r):
    if n > r[1]: return False
    if n < r[0]: return False
    return True

for item in rules:
    n, item = item.split(": ")
    names.append(n)
    a, b = item.split(" or ")
    a = list(map(int, a.split("-")))
    b = list(map(int, b.split("-")))
    ranges.append([a,b])

print(len(tickets))

newT = []
for t in tickets:
    t = list(map(int, t.split(",")))
    valid = True
    for v in t:
        va = False
        for a,b in ranges:
            if inRange(v,a) or inRange(v,b):
                va = True
                break
        if not va:
            valid = False
            break
    if valid:
        newT.append(t)

tickets = list(newT)

print(len(tickets))

canBe = [set(names) for _ in range(len(names))]

for t in tickets:
#    print(t)
    for j in range(len(t)):
        v = t[j]
        for i in range(len(ranges)):
            a,b = ranges[i]
            valid = False
            if inRange(v,a):
                valid = True
            if inRange(v,b):
                valid = True
            if not valid:
                if names[i] in canBe[j]:
                    canBe[j].remove(names[i])

#print(canBe)

while True:
    canBreak = True
    for i in range(len(canBe)):
        if len(canBe[i]) == 1:
            item = list(canBe[i])[0]
            for j in range(len(canBe)):
                if i != j:
                    if item in canBe[j]:
                        canBe[j].remove(item)
        else:
            canBreak = False
            for item in canBe[i]:
                unique = True
                for j in range(len(canBe)):
                    if i != j:
                        if item in canBe[j]:
                            unique = False
                            break
                if unique:
#                    print(canBe)
                    canBe[i] = {item}
                    break
    if canBreak:
        break

print(canBe)

tot = 1
for i in range(len(myTicket)):
    if "departure" in list(canBe[i])[0]:
        tot *= myTicket[i]

print(tot)
