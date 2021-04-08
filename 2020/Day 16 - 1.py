with open('inputs/16 - 1.txt', 'r') as f: #open the file
    rules = f.readlines()
with open('inputs/16 - 2.txt', 'r') as f: #open the file
    tickets = f.readlines()

ranges = []

def inRange(n,r):
    if n > r[1]: return False
    if n < r[0]: return False
    return True

for item in rules:
    item = item.split(": ")[1]
    a, b = item.split(" or ")
    a = list(map(int, a.split("-")))
    b = list(map(int, b.split("-")))
    ranges.append([a,b])

tot = 0
for t in tickets:
    t = list(map(int, t.split(",")))
    for v in t:
        valid = False
        for a,b in ranges:
            if inRange(v,a):
                valid = True
                break
            if inRange(v,b):
                valid = True
                break
        if not valid:
            tot += v

print(tot)



