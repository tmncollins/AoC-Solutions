n = 1

d = 20201227
card = 11349501
door = 5107328

#card = 5764801
#door = 17807724

test = 17807724

def getLoop(n, t):
    global d
    v = 1
    i = 0
    while t != v:
        i += 1
        v *= n
        v = v % d
    return i

def transform(n,i):
    global d
    v = 1
    for i in range(i):
        v *= n
        v = v % d
    return v

a = getLoop(7, card)
b = getLoop(7, door)
print(a,b)
print(transform(card, b))

