class Eris:

    def __init__(self, board):

        self.board = []
        for line in board:
            self.board.append(list(line))

        self.seen = set()
        self.score = 0

    def update(self):

        string = self.toString()
        self.seen.add(string)

        newBoard = [["." for _ in range(5)] for _ in range(5)]
        full = self.getFull()
        print(full)
        all_dir = [(1,0),(0,1),(-1,0),(0,-1)]

        for y in range(5):
            for x in range(5):
                c = 0

                if self.board[y][x] == "#":

                    for dir in all_dir:
                        if (x+dir[0], y+dir[1]) in full: c += 1

                    if c == 1:
                        newBoard[y][x] = "#"

                else:
                    for dir in all_dir:
                        if (x+dir[0], y+dir[1]) in full: c += 1
                    if c == 1 or c == 2:
                        newBoard[y][x] = "#"

        self.board = []
        for line in newBoard:
            self.board.append(list(line))

    def getFull(self):
        full = set()
        for y in range(5):
            for x in range(5):
                if self.board[y][x] == "#": full.add((x,y))
        return full

    def toString(self):
        string = ""
        for line in self.board:
            string += "".join(line)
        return string

    def repeat(self):
        string = self.toString()
        return string in self.seen

    def calculateScore(self):
        string = self.toString()
        score = 0
        for i in range(len(string)):
            if string[i] == "#": score += 2**i
        return score

    def print(self):
        for line in self.board:
            print("".join(line))
        print()

with open("input/24.txt") as f:
    board = f.readlines()

for i in range(len(board)):
    board[i] = board[i].replace("\n", "")

er = Eris(board)

while not er.repeat():
    er.print()
    er.update()

er.print()
print(er.calculateScore())