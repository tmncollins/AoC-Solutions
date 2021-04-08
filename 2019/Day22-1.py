from collections import deque

class Deck:

    def __init__(self,n):
        self.deck = deque()
        for i in range(n):
            self.deck.append(i)

    def dealToNewStack(self):
        self.deck.reverse()

    def cutTop(self, n):
        add = []
        for i in range(n):
            add.append(self.deck.popleft())
#        add = add[::-1]
        for item in add:
            self.deck.append(item)

    def cutBottom(self, n):
        add = []
        for i in range(n):
            add.append(self.deck.pop())
#        add = add[::-1]
        for item in add:
            self.deck.appendleft(item)

    def cut(self, n):
        if n > 0:
            self.cutTop(n)
        else:
            self.cutBottom(abs(n))

    def printDeck(self):
        print(self.deck)

    def dealWithIncrement(self, n):
        pos = 0
        items = list(self.deck)
        maxa = len(items)
        for item in items:
            self.deck.popleft()
            self.deck.appendleft(item)
            self.deck.rotate(-n)
            pos += 0
            pos = pos % maxa
        self.deck.rotate(pos)

    def getIndex(self, n):
        l = list(self.deck)
        return l.index(n)


deck = Deck(10007)

with open("input/22.txt") as f:
    ins = f.readlines()

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

print(deck.getIndex(2019))
#deck.printDeck()
