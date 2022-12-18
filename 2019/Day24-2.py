from collections import defaultdict

class MAP:

    def __init__(self):

        self.map = [["." for i in range(5)] for j in range(5)]

    def set(self, x, y, value):

        self.map[y][x] = value

    def get(self, x, y):

        return self.map[y][x]

    def update(self, board):

        for y in range(5):

            for x in range(5):

                self.set(x,y,board[y][x])


class Eris:

    global EDGE_TILES, EDGE_MAP, OUTER_TILES
    EDGE_TILES = set()
    EDGE_MAP = defaultdict(list)
    OUTER_TILES = set()

    def __init__(self, board):

        self.level = defaultdict(MAP)
        self.level[0].update(board)
        self.levelsSeen = set()
        self.levelsSeen.add(0)



        for y in range(5):
            for x in range(5):
                if x == 0:
                    EDGE_TILES.add((x,y))
                    OUTER_TILES.add((x,y))
                    EDGE_MAP[(x,y)].append((1,2))

                if y == 0:
                    EDGE_TILES.add((x,y))
                    OUTER_TILES.add((x,y))
                    EDGE_MAP[(x,y)].append((2,1))

                if x == 4:
                    EDGE_TILES.add((x, y))
                    OUTER_TILES.add((x, y))
                    EDGE_MAP[(x,y)].append((3,2))

                if y == 4:
                    EDGE_TILES.add((x,y))
                    OUTER_TILES.add((x,y))
                    EDGE_MAP[(x,y)].append((2,3))

        inner_tiles = [(1,2),(2,1),(3,2),(2,3)]

        for item in inner_tiles:
            EDGE_TILES.add(item)
            if item == (1,2): con = [(0, y) for y in range(5)]
            elif item == (3,2): con = [(4, y) for y in range(5)]
            elif item == (2,1): con = [(x, 0) for x in range(5)]
            elif item == (2,3): con = [(x, 4) for x in range(5)]
            else: con = []
            EDGE_MAP[item] = con

    def update(self):

        self.levelsSeen.add(min(self.levelsSeen) - 1)
        self.levelsSeen.add(max(self.levelsSeen) + 1)

        newLevel = defaultdict(MAP)

        for level in self.levelsSeen:

            newBoard = [["." for _ in range(5)] for _ in range(5)]
            full = self.getFull(level)
#            print(full)
            all_dir = [(1,0),(0,1),(-1,0),(0,-1)]

            board = self.level[level]

            for y in range(5):
                for x in range(5):
                    c = 0

                    if y == 2 and x == 2: continue # Centre space

                    if (x,y) in EDGE_TILES:
                        if (x,y) in OUTER_TILES:
                            # level - 1
                            for newTile in EDGE_MAP[(x,y)]:
                                NX, NY = newTile[0], newTile[1]

                                if self.level[level - 1].get(NX, NY) == "#": c += 1

                        else:
                            for newTile in EDGE_MAP[(x, y)]:
                                NX, NY = newTile[0], newTile[1]

                                # level + 1
                                if self.level[level + 1].get(NX, NY) == "#": c += 1


                    if board.get(x,y) == "#":

                        for dir in all_dir:
                            if (x+dir[0], y+dir[1]) in full: c += 1

                        if c == 1:
                            newBoard[y][x] = "#"

                    else:
                        for dir in all_dir:
                            if (x+dir[0], y+dir[1]) in full: c += 1
                        if c == 1 or c == 2:
                            newBoard[y][x] = "#"

            for y in range(5):
                for x in range(5):
                    newLevel[level].set(x,y,newBoard[y][x])

        self.level = newLevel.copy()


    def getFull(self, level):
        full = set()
        board = self.level[level]
        for y in range(5):
            for x in range(5):
                if board.get(x,y) == "#": full.add((x,y))
        return full

    def toString(self, board):
        string = ""
        for y in range(5):
            for x in range(5):
                string += board.get(x,y)
        return string

    def countBugs(self):
        tot = 0
        for level in self.levelsSeen:
            board = self.level[level]
            tot += self.countBugsOnLevel(board)
        return tot

    def countBugsOnLevel(self, board):
        string = self.toString(board)
        return string.count("#")

    def calculateScore(self):
        string = self.toString()
        score = 0
        for i in range(len(string)):
            if string[i] == "#": score += 2**i
        return score

    def print(self, level):
        board = self.level[level]
        for y in range(5):
            for x in range(5):
                print(board.get(x,y), end="")
            print()
        print()

with open("input/24.txt") as f:
    board = f.readlines()

for i in range(len(board)):
    board[i] = board[i].replace("\n", "")

er = Eris(board)

debug = False
for i in range(200):
    print(i)
    if debug:
        print(er.countBugs())
        for item in er.levelsSeen:
            print("LEVEL " + str(item))
            er.print(item)
        print(er.levelsSeen)
    er.update()

print(er.countBugs())

print(EDGE_MAP)