c = list(map(int, list("364297581")))
#cups = list(map(int, list("389125467")))

cups = dict()
for i in range(len(c)-1):
    cups[c[i]] = c[i+1]

cups[c[-1]] = 10
for i in range(10, 1000000):
    cups[i] = i+1

cups[1000000] = c[0]

curr = c[0]
for m in range(10000000):
    if m % 100000 == 0: print(m)
    a = cups[curr]
    b = cups[a]
    c = cups[b]
    d = cups[c]
    #
    n = curr
    while n in [a,b,c,curr]:
        n -= 1
        if n <= 0: n = 1000000
    #
    nxt = cups[n]
    cups[n] = a
    cups[c] = nxt
    cups[curr] = d
    #
    curr = cups[curr]

a = cups[1]
b = cups[a]

print(a,b,a*b)




