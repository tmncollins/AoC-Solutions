with open('inputs/22 - 1.txt', 'r') as f: #open the file
    cards1 = list(map(int,f.readlines()))

with open('inputs/22 - 2.txt', 'r') as f:
    cards2 = list(map(int, f.readlines()))

#cards1 = [9, 2, 6, 3, 1]
#cards2 = [5, 8, 4, 7, 10]

def play(cards1, cards2):
    seen1 = set()
    seen2 = set()
    while len(cards1) > 0 and len(cards2) > 0:
        t1 = tuple(cards1)
        t2 = tuple(cards2)
        if t1 in seen1 or t2 in seen2: return True
        seen1.add(t1)
        seen2.add(t2)
        a = cards1.pop(0)
        b = cards2.pop(0)
        if len(cards1) >= a and len(cards2) >= b:
            winner = play(cards1[:a], cards2[:b])
        else:
            winner = a > b

        if winner:
            cards1 += [a,b]
        else:
            cards2 += [b,a]
    return len(cards1) > len(cards2)

def score(cards):
    cards = cards[::-1]
    tot = 0
    for n in range(len(cards)):
        tot += cards[n] * (n+1)
    return tot

win = play(cards1, cards2)
print(cards1, cards2)

if win:
    print(score(cards1))
else:
    print(score(cards2))




