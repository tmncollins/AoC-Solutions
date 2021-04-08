from collections import defaultdict

class maze:

    def __init__(self, maze):
        self.maze = defaultdict(str)
        self.empty = set()
        self.walls = set()
        self.portalNames = set()
        self.portalMap = defaultdict(list)
        self.mazeW = len(maze[0])
        self.mazeH = len(maze)
        self.maxDepth = 99999
        self.getPortalName = defaultdict(str)
        thick = 999999

        top, bottom = 2, len(maze) - 2
        left, right = 2, len(maze[0]) - 2
        for y in range(top, bottom):
            for x in range(left, right):
                self.maze[(x,y)] = maze[y][x]
                if maze[y][x] == "#": self.walls.add((x,y))
                elif maze[y][x] == ".": self.empty.add((x,y))
                else: thick = min(thick, x-2)

        # Generate Portals
        print(thick)
        self.getOuterPortals(maze)
        self.getInnerPortals(maze, thick)
        self.cleanPortals()

    def setMaxDepth(self, m):
        self.maxDepth = m

    def isInnerPortal(self, loc):
        dist = min(loc[0], loc[1], self.mazeH - loc[1], self.mazeW - loc[0])
        if dist < 5: return False
        return True

    def findShortestPath(self):
        pending = [(self.start, 0, 0, [])]
        all_dir = [(1,0),(0,1),(-1,0),(0,-1)]
        seen = set()
        while len(pending) > 0:
            look = pending.pop(0)
            look, depth, dist, portals = look[0], look[1], look[2], look[3]
            seen.add((look, depth))

            if look == self.end:
#                print(look, depth, dist, portals)
                if depth == 0:
                    return dist

            # Look around
            for d in all_dir:
                new = (look[0] + d[0], look[1] + d[1])
                if new in self.empty and (new, depth) not in seen:
                    pending.append((new, depth, dist + 1, portals))

            # Portals?
            if look in self.portalNames:
                new = self.portalMap[look]
                if new != look:
                    if self.isInnerPortal(look):
                        if (new, depth + 1) not in seen and depth < self.maxDepth:
                            pending.append((new, depth + 1, dist+1, portals + [self.getPortalName[look].lower()]))

                    elif depth > 0 and (new, depth - 1) not in seen:
                        pending.append((new, depth - 1, dist+1, portals + [self.getPortalName[look]]))
        print(seen)


    def cleanPortals(self):
        special = ["ZZ", "##", "#.", ".#", "..", "AA"]
        mapp = dict()
        for key, value in self.portalMap.items():
            if " " not in key and key not in special:
                v = []
                for item in value:
                    if item in self.empty:
                        v.append(item)
                print(key, value, v)
                mapp[v[0]] = v[1]
                mapp[v[1]] = v[0]
                self.getPortalName[v[0]] = key
                self.getPortalName[v[1]] = key
            elif "ZZ" == key:
                self.end = value[0]
            elif "AA" == key:
                self.start = value[0]
        self.portalNames = set(mapp.keys())
        self.portalMap = mapp.copy()

    def getInnerPortals(self, maze, thick):
        # Top
        p = []
        pos = []
        for y in range(thick+2, thick+4):
            seen = 0
            for x in range(len(maze[0])):
                if y == thick+2:
                    p.append(maze[y][x])
                    pos.append(x)
                else:
                    p[seen] += maze[y][x]
                seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((pos[i], 1+thick))

        # Bottom
        p = []
        pos = []
        for y in range(len(maze)-4-thick, len(maze)-thick-2):
            seen = 0
            for x in range(len(maze[0])):
                if y == len(maze)-4-thick:
                    p.append(maze[y][x])
                    pos.append(x)
                else:
                    p[seen] += maze[y][x]
                seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((pos[i], len(maze)-2-thick))

        # Left
        p = []
        pos = []
        seen = 0
        for y in range(len(maze)):
            for x in range(len(maze[0]) - 4 - thick, len(maze[0]) - thick-2):
                if x == len(maze[0]) - 4 - thick:
                    p.append(maze[y][x])
                    pos.append(y)
                else:
                    p[seen] += maze[y][x]
                    seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((len(maze[0]) - 2 - thick , pos[i]))

        # Right
        p = []
        pos = []
        seen  = 0
        for y in range(len(maze)):
            for x in range(thick+2, thick + 4):
                if x == thick+2:
                    p.append(maze[y][x])
                    pos.append(y)
                else:
                    p[seen] += maze[y][x]
                    seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((thick+1, pos[i]))

    def getOuterPortals(self, maze):
        # Top
        p = []
        pos = []
        for y in range(2):
            seen = 0
            for x in range(len(maze[0])):
                if y == 0:
                    p.append(maze[y][x])
                    pos.append(x)
                else:
                    p[seen] += maze[y][x]
                seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((pos[i], 2))

        # Bottom
        p = []
        pos = []
        for y in range(len(maze)-2, len(maze)):
            seen = 0
            for x in range(len(maze[0])):
                if y == len(maze)-2:
                    p.append(maze[y][x])
                    pos.append(x)
                else:
                    p[seen] += maze[y][x]
                seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((pos[i], len(maze)-3))

        # Left
        p = []
        pos = []
        seen = 0
        for y in range(len(maze)):
            for x in range(2):
                if x == 0:
                    p.append(maze[y][x])
                    pos.append(y)
                else:
                    p[seen] += maze[y][x]
                    seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((2, pos[i]))

        # Right
        p = []
        pos = []
        seen  = 0
        for y in range(len(maze)):
            for x in range(len(maze[0]) - 2, len(maze[0])):
                if x == len(maze[0]) - 2:
                    p.append(maze[y][x])
                    pos.append(y)
                else:
                    p[seen] += maze[y][x]
                    seen += 1
        for i in range(len(p)):
            portal = p[i]
            self.portalNames.add(portal)
            self.portalMap[portal].append((len(maze[0])-3, pos[i]))

data = """                                           C   I         O     M       H             G                                       
                                           T   F         E     C       U             C                                       
  #########################################.###.#########.#####.#######.#############.#####################################  
  #...................#...#.......#.#.#.#.....#.#...#.....#...#...#.....#...#.......#.#.....#.#...#.#.#...#...#.#...#...#.#  
  #.###.#######.###.#####.#.#.#.###.#.#.#####.#.#.#.###.#.#.#.#.###.###.###.###.#.#.#.###.###.#.###.#.#.###.###.###.#.###.#  
  #.#.#.#.#.....#...........#.#.......#.......#...#...#.#.#.#.#.#.#.#.#.#.....#.#.#.#.#...#...#.#.#.....#.#.#...#.........#  
  ###.#.#.###.#####.#.###.#########.###.###.#.#######.#.###.#.#.#.###.#.#.#.###.#.#.#.#.#####.#.#.###.###.#.###.###.#.#.#.#  
  #.....#...#.#.....#.#...#.#...#.....#.#.#.#.#.#...#.#.....#.#.#.#...#...#.#.#.#.#.#...#...#...#...#...#.#.#.#.#.#.#.#.#.#  
  #.#######.###############.#.#####.###.#.#.###.#.#.#.###.###.#.###.#.###.###.#.#.#.#.###.###.#####.#.###.#.#.#.#.#.#.#.###  
  #.#...........#.#.#...#.................#.#.#...#.....#.#.#.#.....#.#.....#...#.#.#.#.......#.#.#.#.#.#...........#.#...#  
  #############.#.#.###.###.#.#.###.#####.###.#.#####.#####.#.###.###.#.#.#.#.#.#.#.#.#.#######.#.#.#.#.#.#.###.###.#.###.#  
  #.#.....#.#.#.............#.#.#...#.....#.#.....#...#...#...#.#.#...#.#.#.#.#.#.#...........#.#.#.#.....#...#...#.#.#...#  
  #.###.#.#.#.#.#.###.###.###.#######.#.###.###.#######.#.#.#.#.###.#######.###.###.#.###.###.#.#.#.#.###.#############.#.#  
  #...#.#.#.....#.#.#.#...#.#.#.#.....#.....#.#.....#...#...#.....#...#.....#.#.#.#.#.#...#.............#.......#...#.#.#.#  
  ###.#.#####.#.###.#.#.#.#.###.#.#######.###.#.#######.###.###.###.#.#.#####.#.#.###.#.###.#.###.#.#.#.###.#####.###.###.#  
  #...........#...#...#.#.#.#...#.#.....#.....#...#...#.#.....#.#...#.#.......#.....#.#...#.#.#.#.#.#.#...#.............#.#  
  #.#.#######.#.#.###.###.#.###.###.###.#####.#.###.###.#.#.#########.#.#.#.#.###.###.#.#######.#.#.###########.###########  
  #.#.#.#.#...#.#.#.....#.#...#.....#.#.#.....#...#...#.#.#.#.#.#.#.#.#.#.#.#.#.....#.#.......#...#.......#...#...#.......#  
  #.###.#.#.###.#######.#####.#######.#.#.#####.#####.#.#####.#.#.#.#.###.###.#.#.###.#############.###.###.#######.#######  
  #.#.....#.#.#.....#...#.............#...#.#...#.#.....#.......#.#.#...#.#.#.#.#...#.....#.....#...#...#...#...#.#.#.#...#  
  #.###.#.###.#.#####.###.###########.#.###.###.#.#####.#.###.#.#.#.#.###.#.#.#.#######.###.###############.#.#.#.#.#.#.#.#  
  #.#.#.#.....#.#...#.#.#.#.......#...........#.......#...#.#.#.#.......#.#...#.....#.#.#...#.#.........#.....#.#.....#.#.#  
  ###.###.###.#.#.#####.#########.#.#.#.#.#####.#.###.#.#.#.#####.#.#######.#.###.###.#####.#.###.#########.#######.###.#.#  
  #.....#.#.#.#.#...#...............#.#.#.....#.#.#.#.#.#.......#.#.....#...#...#.....#.......#.#...#...#.......#.#.....#.#  
  ###.###.#.#####.###.#.###.#.#.###.#.###.#####.###.#####.###.#.###.#.###.###.#.#.#.###.#.#.#.#.#.#.#.###.#######.#.#.#####  
  #...#...#...#...#.#.#...#.#.#...#.#.#.....#.#...#...#...#...#.#...#.#.#.#...#.#.#...#.#.#.#.#...#.#.#...#...#...#.#.#...#  
  ###.###.#.#####.#.#####################.#.#.###.#.#########.#######.#.###.#######.#.#.#####.#.#.###.###.###.###.#.#.###.#  
  #.#.....#.#.#.........#...........#.....#.#...#.#.#...#.#.#...#...#...#...#.....#.#.#...#.....#.#...#.......#.#...#.#.#.#  
  #.#####.#.#.#####.###########.###.###.###.###.#.#.#.###.#.#.###.#.#.###.#.###.#####.#.#.#####.#####.#.#######.#.#####.#.#  
  #...#.......#.#...#.#.....#...#.....#...#...#.....#.......#...#.#...#.#.#.#...........#...#.#.#.......#.#.#...#.....#...#  
  #.#######.###.###.#.#####.#####.###.#.#######.###.###.###.#.###.###.#.###.###.#########.#.#.#######.###.#.#.#####.###.###  
  #.#...#.#.......#.#.#.#...#.#...#.......#.#...#...#...#.#.#.#...#.#.#...#...#.........#.#.#.#.#.#.#.#.......#.#.....#...#  
  #.###.#.#.#######.#.#.#.###.#########.###.###.#######.#.#.#.#.###.###.#.###.###.#.#.#######.#.#.#.#.#.#######.#####.#.###  
  #...........#.#.....#.....#.....#...........#...#.......#...#.......#.#.......#.#.#...#...#.......#.#.....#.#.#.........#  
  #.#####.#.#.#.###.#.#.#.###.###.#########.#####.#####.###########.###.#########.#########.#.#######.###.###.#.#####.#####  
  #.#.#.#.#.#.#.#.#.#...#.#...#...#        G     N     H           Q   I         H        #...#...#.#.#.....#.#.#...#.#.#.#  
  ###.#.###.###.#.#####.#########.#        C     W     L           B   F         U        #.#####.#.#.###.###.#.#.###.#.#.#  
  #...#...#...#.#.#.#.#...#.#...#.#                                                       #...#.......#...................#  
  #.###.###.###.#.#.#.#.#.#.###.#.#                                                       #.#.#.#####.#.###.###.#.#.###.###  
  #.#.#...#...#.....#.#.#.#...#...#                                                     IH..#...#.#...#.#.#...#.#.#...#...#  
  #.#.#.###.#.###.###.###.#.###.###                                                       #.#.#.#.###.#.#.#######.#######.#  
  #.......#.#.......#.#...........#                                                       #.#.#.#.#.....#.#.#.#...#.#.#....WD
  #.#.#########.#.###.#####.#.#####                                                       #######.#######.#.#.###.#.#.#####  
  #.#.....#...#.#.#.#...#.#.#...#.#                                                       #.#.#...#.............#.#.#.#...#  
  #.#.#####.#.#.#.#.#.###.#.###.#.#                                                       #.#.#.#.#.###.#.###.#.###.#.#.#.#  
UQ..#.....#.#...#...#.#.#.....#....XT                                                   UZ....#.#.....#.#...#.#.......#.#.#  
  ###.###.#.###.#.#.#.#.#####.#.###                                                       ###.#.###.#.###.#.#.#######.#.#.#  
  #.#.#.....#.#.#.#...........#.#.#                                                       #...#.#.#.#.#...#.#.#.#.....#.#..AH
  #.###.#####.#####.#.#.#########.#                                                       #.###.#.#######.#####.#####.#.###  
YI....#.#.#.#.....#.#.#.#..........RV                                                     #...........#.#.#...#.....#...#.#  
  ###.###.#.#.#######.###.#####.###                                                       #########.###.###.#####.#.#####.#  
  #.....#.......#...#.#...#.......#                                                       #.......#.#...#.#...#.#.#.....#..OS
  ###.#.#####.###.#########.###.#.#                                                       #.#####.#####.#.#.#.#.###.###.#.#  
  #...#.#.#.......#.#.....#...#.#.#                                                       #.#.......#.....#.#.#.....#...#.#  
  #.#.###.###.#.#.#.#.###.###.###.#                                                       #.#.#########.#####.#####.#.###.#  
  #.#.........#.#.....#.#.....#...#                                                       #.#...#.#.....#.#.#.#.#.#.#.#...#  
  #######.#######.###.#.#.###.#####                                                       #.###.#.#####.#.#.#.#.#.#.#.###.#  
  #.....#.#...#...#.#.#.....#.#....ZO                                                   AH..#.#.....................#.....#  
  #.#.#####.#######.###.#.###.###.#                                                       ###.#.#######################.###  
UZ..#...#.....#.#.#.#.#.#...#.#.#.#                                                     UP..#.#...#.#.............#.#.#.#.#  
  ###.###.###.#.#.#.#.#########.#.#                                                       #.#.#.###.###.###.###.#.#.#.###.#  
  #.....#...#.......#...#.#.....#.#                                                       #...#.#...#.....#...#.#.......#..KD
  #.#######.#.#.#.#.#.#.#.###.###.#                                                       #.#####.#.###.#.###.#######.###.#  
  #.........#.#.#.#...#...........#                                                       #.......#.#...#.#.....#.#.....#.#  
  ###.###.#######.#.###.#.#########                                                       ###.#.#######.###.#####.#####.#.#  
  #.....#.#...#.#.#...#.#.#.#...#.#                                                       #.#.#.........#.#.#.....#.......#  
  ###########.#.###########.#.#.#.#                                                       #.#############.###.###.#######.#  
  #.#.#.#.#.....#.#.#.....#...#...#                                                     YI....#...........#.....#.#.#.#...#  
  #.#.#.#.###.#.#.#.###.###.###.#.#                                                       ###.#.###.###.#.#.#.#.###.#.#####  
  #.........#.#.#.#.......#...#.#.#                                                       #...#.#.....#.#...#.#.....#.....#  
  #.#####.###.###.#####.#.###.#.###                                                       #.#.#.#####.#.#########.###.#.###  
MI......#...............#.....#....KD                                                     #.#.#.#.#.#.#.#...#.#.....#.#.#..ZZ
  #.#######################.#######                                                       #.###.#.#.#######.#.###.#.###.#.#  
  #.....#...#...........#.#.#.....#                                                       #.....#.....#.#.#...#.#.#........ZO
  #.#####.#.#.#.#.#.#.#.#.###.###.#                                                       #.#####.###.#.#.#.###.###########  
  #.#.#.#.#...#.#.#.#.#.....#...#..CT                                                     #.#.#.....#.#.........#.........#  
  ###.#.#.#####.###########.#.#.###                                                       ###.#.#.#.###.#######.###.#.#.###  
UP......#...#.#.....#.#.....#.#....NG                                                     #...#.#.#.......#.........#.#...#  
  #.#.#.#.#.#.###.###.#.#########.#                                                       #.#.#.#.#####.#########.#.#####.#  
VH..#.#...#.#...#.#...#...........#                                                       #.#.#.#.....#.....#.....#...#...#  
  #.#########.#######.#########.###                                                       #.#.#####.###.###.#.#.#.#######.#  
  #...#.......#.#...#...#...#...#.#                                                     VO..#.......#...#...#.#.#.#...#....IH
  #####.#####.#.###.#.#.#.#.###.#.#                                                       #.#########################.#####  
AA....#.#...#...#.#...#...#.#.#.#.#                                                       #.#.#...#...............#........VO
  ###.#.###.#.###.###.#####.#.#.#.#                                                       ###.#.#.#.###.#.###.###.#.#.###.#  
NW....#.....#.#.#.#.#...#.#...#.#..MI                                                   IU..#...#...#...#...#.#.....#...#.#  
  #.#######.#.#.#.#.###.#.###.###.#                                                       #.###.#.#######.#######.###.#.###  
  #.........#...........#.........#                                                       #...#.#.......#.#.........#.#...#  
  #.#.#####.###.#.#.###.###.###.###                                                       #.#.#.#########.###.###.#####.###  
  #.#...#...#.#.#.#...#.#.#.#.#...#                                                       #.#.........#...#.#.#.......#...#  
  #.#.###.###.#.#.###.#.#.#.#.#.###      V         N M     O       O     W         U      #.#.#.#.###.#####.#.#######.#####  
  #.#.#.......#.#...#.#...#...#...#      H         B C     S       E     D         Q      #.#.#.#...#.....#.........#.....#  
  #.###.#.#.#####.#####.#.#####.#.#######.#########.#.#####.#######.#####.#########.###########.###########.#.#####.#.#.#.#  
  #...#.#.#.#.....#.....#.#.....#.#.#.....#.........#.#.......#.....#.#.#.....#...#.#.......#.....#.....#.#.#.#.#.#.#.#.#.#  
  #.#.#.#.#######.#######.###.#.###.#.###.###.###.###.#.#.#######.###.#.###.#####.#.#######.#.###.#.#####.###.#.#.###.###.#  
  #.#.#.#.#.#.#.......#.....#.#...#.....#.#.....#.#...#.#.#...#.........#...#.....#.....#.....#.....#.#.....#.......#...#.#  
  #.#.#.###.#.###.#######.###########.#########.#####.###.###.#########.###.###.#####.#####.#.#.#.#.#.#.#.#.#####.#####.#.#  
  #.#.#.#.............#.....#.......#.#.....#...#...#...#.......#.........#.......#.....#...#.#.#.#.#...#.#...#.....#.#.#.#  
  #.#.###.#.#.#####.#####.#.#######.#.#.#.###.#.###.###.###.#####.###.#.#######.###.###############.#.#.###.#####.###.###.#  
  #.#...#.#.#.#.#.#.#.#...#...#...#...#.#...#.#.......#.#.......#...#.#.#.....#.#.......#.......#.....#...#.#.......#.....#  
  #.#.###.#.###.#.#.#.###.#####.#####.#.#.#########.###.#######.#.#######.###.#.#####.#####.#.#####.#.#.#########.#.#####.#  
  #.#.#.#.#.#.........#.....#.........#.#...#.......#.....#.#.#.#.....#...#.....#.#.#.......#.#.....#.#...#.#.#...#.#.....#  
  #.###.###.###.###.#########.#.###.#.#.###.###.###.#.#####.#.#.#.#######.###.###.#.###.###.#####.#.#######.#.#########.#.#  
  #.......#.#.#.#.#...#...#.#.#.#...#.#.#.#.#.....#.#...#.#.....#...#.#.#.#...#...#.....#.....#...#...............#.....#.#  
  #.#.#######.#.#.###.#.#.#.#########.#.#.#.###.###.###.#.###.#.#.#.#.#.#.#####.#####.#.#####.#.#.###.#####.###.#.#######.#  
  #.#...#...........#.#.#.#...#...........#...#...#.#...#.#...#.#.#...#.#...#.........#...#...#.#...#.....#.#.#.#.....#...#  
  #.#.#.#.#.#.#.#.#######.###.#.#.#.###.#.#.#######.#.###.#####.#.#####.#.#######.#.###.###.#####.###.###.###.###.#.###.###  
  #.#.#.#.#.#.#.#.#.#.#.........#.#.#.#.#.#...#...#.#.......#.#.#.#...#...#...#.#.#.#.#...#.#.......#.#.........#.#...#...#  
  #.#.#######.#.###.#.###.###########.#.#.#.#####.#.###.#####.#.#.###.###.#.###.#.###.###.#.#####.#.###.#.#.#.#############  
  #.#.#.....#.#.#.....#...#...#...#.#.#.#.#...#.....#.....#.#...#.......#...#.#.......#.#.#.#.....#...#.#.#.#...#.........#  
  ###.#####.#########.#######.###.#.#.#####.###.#.###.#####.###.#.#.#####.###.###.#####.#########.#.#####.###.#.#####.###.#  
  #.#.#.........#.#...#.#...............#.#.#.#.#...#.....#.#.#.#.#.#.......#.....#...........#...#.#.......#.#.#.#.....#.#  
  #.#.#######.###.###.#.#####.#.#.#.#.###.#.#.#####.#.###.#.#.#.#.#####.#.#######.#.#####.#######.#####.#.###.###.#.#.#####  
  #...#.....#.#...#.#.....#.#.#.#.#.#.#.......#.....#.#.#.#.....#...#...#...#.........#.#.#.#.#.#.....#.#...#.......#.#...#  
  #.#.###.###.#.###.###.###.#######.###.###########.#.#.###.#.###.#######.#######.#.###.###.#.#.#################.#.#.#.#.#  
  #.#.#.....#.#.#.#.#...#.#.#.......#...........#.#.#...#...#...#.#...#...#.....#.#.#...........#.............#...#.#...#.#  
  #.#.###.#.#.#.#.#.###.#.#.###.###.#######.#.###.#.###.###.#.#.#.###.###.###.#.#.#.#.#######.#.#.###.###.#.#####.#.###.###  
  #.#.#.#.#.........#...#.#.#...#.#.........#...#.....#.#...#.#.#.......#.....#.#.#.#...#...#.#.....#...#.#.#.....#.#.....#  
  #.###.#####.#####.###.#.#.#.###.###.###.#.#######.###.#.#######.#####.#.#####.#.###.#####.###.#.#.#######.###.#######.#.#  
  #.#.......#.#...............#.........#.#.#.........#.#...#...#.#.#...#.#.....#.#.....#.#.#.#.#.#.....#...#.........#.#.#  
  #########.#######.#.#.###.#.###.#.#.#########.#######.###.#.###.#.###.###.#####.###.###.#.#.#####.#.#####.#####.#.#.###.#  
  #.#.#.#.#.#...#.#.#.#.#...#...#.#.#.........#.......#...#.#...#.....#.#.....#.......#...#...#.#.#.#...#.#...#...#.#...#.#  
  #.#.#.#.#.###.#.#.#.###.#######.#######.#####.###.###.###.#.#######.###.###########.###.#.#.#.#.#.#.###.#######.###.#####  
  #.................#...#.....#...#.........#.....#.#...#.....#.........#.........#.........#.....#.#...........#...#.....#  
  #####################################.###########.###.#####.###.#########.#########.#####################################  
                                       N           I   R     H   N         X         Q                                       
                                       B           U   V     L   G         T         B                                       """.split("\n")

m = maze(data)
m.setMaxDepth(120)
print(m.portalMap)

print("ANS", m.findShortestPath())