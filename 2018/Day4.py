from _collections import defaultdict

with open("input/4.txt") as f:
    data = f.readlines()

data = sorted(data)
#print(data)

asleep = defaultdict(list)

def timeElapsed(ID, a, b):
    dayA, timeA = a.split()
    dayB, timeB = b.split()
    dayA = int(dayA.split("-")[2])
    dayB = int(dayB.split("-")[2])

    minutes = (dayB - dayA) * 24 * 60
    dH = int(timeB.split(":")[0]) - int(timeA.split(":")[0]) * 60
    minutes += dH
    dM = int(timeB.split(":")[1]) - int(timeA.split(":")[1])
    minutes += dM
    start = int(timeA.split(":")[1])

    for i in range(minutes):
        asleep[ID].append(i + start % 60)

    return minutes

last = [""]
ID = 0
IDS = []
for item in data:
    item = item.replace("\n", "").replace("[", "").split("] ")
    if "shift" in item[-1]:
        s = item[-1].split()
        ID = s[1]
        IDS.append(ID)
    elif "wakes" in item[-1]:
        timeElapsed(ID, last[0], item[0])
    last = item

MAX_ASLEEP = 0
val1 = 0
val2 = 0
MAX_MODE_COUNT = 0

#print(asleep)

for ID in IDS:
    mode = -1
    modeCount = 0
    for i in asleep[ID]:
        if asleep[ID].count(i) > modeCount:
            modeCount = asleep[ID].count(i)
            mode = i
    if len(asleep[ID]) > MAX_ASLEEP:
        MAX_ASLEEP = len(asleep[ID])
        val1 = int(ID[1:]) * mode
    if modeCount > MAX_MODE_COUNT:
        MAX_MODE_COUNT = modeCount
        val2 = int(ID[1:]) * mode

print("Part 1:", val1)
print("Part 1:", val2)

