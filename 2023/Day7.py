from collections import defaultdict

def strength(hand):
    counter = defaultdict(int)
    for i in hand: counter[i] += 1
    if 5 in counter.values(): return 7 # 5 of a kind
    if 4 in counter.values(): return 6 # 4 of a kind
    if 3 in counter.values() and 2 in counter.values(): return 5 # full house
    if 3 in counter.values(): return 4 # three of a kind
    if list(counter.values()).count(2) == 2: return 3 # two pair
    if 2 in counter.values(): return 2 # one pair
    return 1 # high card

def hand_to_score(hand):
    score = []
    rank = "23456789TJQKA"
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

part1 = 0
for i in range(len(hands)):
    part1 += (i+1)*hands[i][-1]

print("Part 1:", part1)