with open('inputs/22 - 1.txt', 'r') as f: #open the file
    cards1 = list(map(int,f.readlines()))

with open('inputs/22 - 2.txt', 'r') as f:
    cards2 = list(map(int, f.readlines()))

while len(cards1) > 0 and len(cards2) > 0:
    a = cards1.pop(0)
    b = cards2.pop(0)
    if a > b:
        cards1.append(a)
        cards1.append(b)
    else:
        cards2.append(b)
        cards2.append(a)

def score(cards):
    cards = cards[::-1]
    tot = 0
    for n in range(len(cards)):
        tot += cards[n] * (n+1)
    return tot

if len(cards1) == 0:
    print(score(cards2))
else:
    print(score(cards1))


