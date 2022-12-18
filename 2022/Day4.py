

with open("inputs/Day4.txt", "r") as f:
    all_data = f.readlines()

for i in range(len(all_data)):
    all_data[i] = all_data[i].replace("\n", "").split(",")

def contains(s1, e1, s2, e2):
    if s1 <= s2 and e1 >= e2: return True
    return False

def overlap(s1, e1, s2, e2):
    if s1 <= s2 and e1 >= s2: return True
    if s2 <= s1 and e2 >= s1: return True
    return False

p1 = 0
p2 = 0
for r in all_data:
    s1, e1 = list(map(int, r[0].split("-")))
    s2, e2 = list(map(int, r[1].split("-")))
    if contains(s1, e1, s2, e2) or contains(s2, e2, s1, e1):
        p1 += 1
    if overlap(s1, e1, s2, e2):
        p2 += 1

print("Part 1:", p1)
print("Part 1:", p2)

