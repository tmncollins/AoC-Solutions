from functools import lru_cache

P1, P2 = 9, 3
p1, p2 = P1, P2

die = 0

def roll():
    global die

    m = 0
    for i in range(3):
        m += (die % 100) + 1
        die += 1
    return m

s1, s2 = 0, 0

turn = True
while s1 < 1000 and s2 < 1000:
    m = roll() % 10
    if turn:
        p1 += m
        while p1 > 10:
            p1 -= 10
        s1 += p1
    else:
        p2 += m
        while p2 > 10:
            p2 -= 10
        s2 += p2

    turn = not turn

rolls = []

loser = s1 if s2 >= 1000 else s2
print("Part 1:", die * loser)

for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            rolls.append(a+b+c)

@lru_cache(maxsize=None)
def dirac(p1, p2, s1, s2, p):
    if s1 >= 21:
        return [1,0]
    if s2 >= 21:
        return [0,1]

    global rolls
    ans = [0,0]
    if p:
        for i in rolls:
            np = p1 + i
            while np > 10: np -= 10
            ns = s1 + np
            x = dirac(np, p2, ns, s2, False)
            ans[0] += x[0]
            ans[1] += x[1]

    else:
        for i in rolls:
            np = p2 + i
            while np > 10: np -= 10
            ns = s2 + np
            x = dirac(p1, np, s1, ns, True)
            ans[0] += x[0]
            ans[1] += x[1]

    return ans

print("Part 2:", max(dirac(P1, P2, 0, 0, True)))
