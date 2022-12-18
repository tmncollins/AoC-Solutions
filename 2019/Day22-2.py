import math

from collections import deque

def nTermGeometricSequence(a, r, n, mod=0):
#    print(mod)
    if mod == 0:
        mult = pow(r, (n-1))
    else:
        mult = 1 - pow(r, n, mod)
        mult2 = pow(1-r, mod - 2, mod)
        mult *= mult2
    term = a * mult

    return term

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / math.gcd(a, b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b//a)*y, y)

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g != 1:
        raise Exception("Modulo Inverse does not exist for", a, "%", m)
    else:
        return x % m

class Deck:

    def __init__(self,n):
        self.diff = 1
        self.start = 0
        self.length = n

    def dealToNewStack(self):
        self.diff *= -1
        self.start += self.diff

    def cut(self, n):
        new = self.getCardAt(n)
        self.start = new

    def dealWithIncrement(self, n):
        a = modinv(n, self.length)
        self.diff *= a
        self.diff = self.diff % self.length

    def getCardAt(self, n):
        card = self.start + (self.diff * n)
        card = card % self.length
        return card

    def printDeck(self):
        for i in range(self.length):
            print(self.getCardAt(i), end=" ")

    def setValues(self, start, diff):
        self.start = start
        self.diff = diff

with open("input/22.txt") as f:
    ins = f.readlines()

numCards = 119315717514047
iterations = 101741582076661

deck = Deck(numCards)

lastDiff = 1
lastStart = 0
from time import *

for item in ins:
    item = item.replace("\n", "").split()
    if item[-1] == "stack":
        deck.dealToNewStack()
    elif item[0] == "cut":
        cut = int(item[1])
        deck.cut(cut)
    elif item[0] == "deal":
        inc = int(item[-1])
        deck.dealWithIncrement(inc)

start_diff = deck.start
diff_mult = deck.diff
diff = deck.diff
start = deck.start

#iterations = 2

finalDiff = pow(diff_mult, iterations, numCards)
# Geometric series
finalStart = nTermGeometricSequence(start_diff, diff_mult, iterations, numCards)

deck.setValues(finalStart, finalDiff)
print(deck.getCardAt(2020))