

def get_both(rucksack):
    a, b = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for i in a:
        if i in b: return i

def get_all(rucksacks):

    for i in rucksacks[0]:
        badge = True
        for r in rucksacks:
            if i not in r:
                badge = False
                break
        if badge: return i

with open("inputs/Day3.txt", "r") as f:
    all_data = f.readlines()

priority = dict()
alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = alpha.upper()

for i in range(26):
    priority[alpha[i]] = i+1
    priority[ALPHA[i]] = i + 27

tot = 0
for line in all_data:
    line = line.replace("\n", "")
    tot += priority[get_both(line)]

tot2 = 0
for i in range(0, len(all_data), 3):
    tot2 += priority[get_all([all_data[i].replace("\n", ""), all_data[i+1].replace("\n", ""), all_data[i+2].replace("\n", "")])]

print("Part 1:", tot)
print("Part 2:", tot2)
