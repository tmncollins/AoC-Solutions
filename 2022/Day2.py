
def score(a, b):
    s_a, s_b = 0, 0
    if a == b:
        s_a, s_b = 3, 3
    elif (a+1)%3 == b:
        s_a, s_b = 0, 6
    elif (a+1)%3 == b:
        s_a, s_b = 6, 0

    s_a += 1 + a
    s_b += 1 + b

    return (s_a, s_b)

conv = {"A":0, "B":1, "C":2, "X":0, "Y":1, "Z":2}

with open("inputs/Day2.txt", "r") as f:
    all_data = f.readlines()

score_1 = 0
score_2 = 0

for line in all_data:
    a, b = line.replace("\n", "").split()
    score_1 += score(conv[a], conv[b])[1]
    play = 0
    if b == "Y": play = conv[a]
    elif b == "X": play = (conv[a] + 2) % 3
    elif b == "Z": play = (conv[a] + 1) % 3
    score_2 += score(conv[a], play)[1]

print("Part 1:", score_1)
print("Part 2:", score_2)