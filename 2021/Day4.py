
class bingo:

    def __init__(self, board):
        self.board = board
        self.marked = [[False for i in range(5)] for _ in range(5)]

    def score(self):
        tot = 0
        for y in range(5):
            for x in range(5):
                if not self.marked[y][x]: tot += self.board[y][x]
        return tot

    def haveWon(self, x, y):
        # check row
        won = True
        for X in range(5):
            if not self.marked[y][X]:
                won = False
                break
        if won: return True
        # check col
        won = True
        for Y in range(5):
            if not self.marked[Y][x]:
                won = False
                break
        if won: return True

    def mark(self, n):
        for y in range(5):
            for x in range(5):
                if self.board[y][x] == n:
                    self.marked[y][x] = True
                    if self.haveWon(x, y):
                        return self.score() * n
        return 0

    def output(self):
        for y in range(5):
            for x in range(5):
                if not self.marked[y][x]:
                    print(self.board[y][x], end = " ")
                else: print(" X", end = " ")
            print()

f = open("inputs/Day4.txt")
data = f.read().split("\n")

nums = list(map(int, data[0].split(",")))

boards = []
i = 2
while i < len(data):
    b = []
    for j in range(i, i+5):
#        print(data[j])
        data[j] = data[j].replace("  ", " ").split()
        b.append(list(map(int, data[j])))

    B = bingo(b)
    boards.append(B)
    i += 6

done = False
LEN = len(boards)
for n in nums:
#    if done: break
    toremove = []
    for b in boards:
        ans = b.mark(n)
#        b.output()
#        print()
        if ans != 0:
            if len(boards) == 1:
                print("Part 2:", ans)
            elif len(boards) == LEN:
                print("Part 1:", ans)
            #done = True
            toremove.append(b)
    for b in toremove: boards.remove(b)

