from _collections import defaultdict

with open("inputs/Day4.txt") as file:
    data = file.read().strip().split("\n")

part1 = 0
MAX_CARD = 0
copies = defaultdict(int)
for card in data:
    card = card.replace(":", "|").split("|")
    winning_numbers = set(map(int, card[1].split()))
    numbers = list(map(int, card[2].split()))
    i = 0
    y = int(card[0].split()[1])
    copies[y] += 1

    for j in numbers:
        if j in winning_numbers: i += 1
    if i > 0: part1 += pow(2, i-1)

    for j in range(y, y+i):
        copies[j+1] += copies[y]

    MAX_CARD = max(MAX_CARD, y)

part2 = 0
for i in range(1, MAX_CARD+1):
    part2 += copies[i]

print("Part 1:", part1)
print("Part 2:", part2)