from collections import defaultdict

rank = "J23456789TQKA"

def strength(hand):
    global rank
    counter = defaultdict(int)
    jokers = 0
    for i in hand:
        if i == "J":
            jokers += 1
        else:
            counter[i] += 1
    if jokers == 5: return 7
    if max(counter.values()) + jokers >= 5: return 7 # 5 of a kind
    if max(counter.values()) + jokers >= 4: return 6 # 4 of a kind
    if (3 in counter.values() and 2 in counter.values()) or \
            (list(counter.values()).count(2) == 2 and jokers >= 1): return 5 # full house
    if max(counter.values()) + jokers >= 3: return 4 # three of a kind
    if list(counter.values()).count(2) == 2 or \
            (list(counter.values()).count(2) == 2 and jokers >= 1) or \
            jokers >= 2: return 3 # two pair
    if max(counter.values()) + jokers >= 2: return 2 # one pair
    return 1 # high card

def hand_to_score(hand):
    global rank
    score = []
    for i in hand: score.append(rank.index(i))
    return score

with open("inputs/Day7.txt") as file:
    data = file.read().strip().split("\n")

hands = []
for line in data:
    hand, bid = line.split()
    bid = int(bid)
    hands.append([strength(hand), hand_to_score(hand), hand, bid])

hands = sorted(hands)
print(hands)
part2 = 0
for i in range(len(hands)):
    part2 += (i+1)*hands[i][-1]

print("Part 2:", part2)