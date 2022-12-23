
with open("inputs/20.txt") as f:
    all_data = f.read().split("\n")

class Tile():

    def __init__(self):
        self.tile = ""
        self.id = 0

    def rotate(self, n=1):

        for i in range(n):
            self.tile = list(zip(*self.tile[::-1]))

    def flip_x(self):

        for i in range(len(self.tile)):
            self.tile[i] = self.tile[i][::-1]

    def flip_y(self):

        self.rotate(1)
        self.flip_x()
        self.rotate(3)

    def __str__(self):
        string = "Tile " + str(self.id) + ":\n"
        for line in self.tile:
            string += "".join(line) + "\n"
        return string + "\n"

    def edges(self):
        edges = []
        for i in range(4):
            edges.append("".join(self.tile[0]))
            self.rotate()
        return edges

    def top_edge(self):
        return "".join(self.tile[0])

    def left_edge(self):
        edge = ""
        for i in range(len(self.tile)):
            edge += self.tile[i][0]
        return edge

    def right_edge(self):
        edge = ""
        for i in range(len(self.tile)):
            edge += self.tile[i][-1]
        return edge

    def bottom_edge(self):
        return "".join(self.tile[-1])

    def remove_edges(self):
        self.tile.pop()
        self.tile.pop(0)
        for i in range(len(self.tile)):
            self.tile[i] = self.tile[i][1:-1]

tile_id = -1
tiles = []
img = []

# parse the tiles
for line in all_data:

    if line == "":
        t = Tile()
        t.id = tile_id
        t.tile = list(img)
        img = []
        tiles.append(t)
        tile_id = -1

    elif line[0] == "T":
        t,i = line.split()
        tile_id = int(i.replace(":", ""))

    else:
        img.append(list(line))

if tile_id != -1:
    t = Tile()
    t.id = tile_id
    t.tile = list(img)
    img = []
    tiles.append(t)

edges = set()
unique_edges = set()

for tile in tiles:
    for e in tile.edges():
        edges.add(e)
        if e in unique_edges:
            unique_edges.remove(e)
        elif e[::-1] in unique_edges:
            unique_edges.remove(e[::-1])
        else:
            unique_edges.add(e)
        tile.rotate()

# grab a corner
part1 = 1
corner = tiles[0]
for tile in tiles:
    uni = 0
    for e in tile.edges():
        if e in unique_edges or e[::-1] in unique_edges:
            uni += 1

    if uni == 2:
        # corner!
        corner = tile
        part1 *= tile.id

print("Part 1:", part1)

# rotate corner
while True:
    if corner.top_edge() in unique_edges or corner.top_edge()[::-1] in unique_edges:
        if corner.left_edge() in unique_edges or corner.left_edge()[::-1] in unique_edges:
            break
    corner.rotate()

jigsaw = [[corner]]

# remove corner tile
for tile in tiles:
    if tile.id == corner.id:
        tiles.remove(tile)
        break

while tiles:
    for tile in tiles:
        if len(jigsaw[-1]) == 0:
            # add below
            for i in range(4):
                if tile.top_edge() == jigsaw[-2][0].bottom_edge():
                    # add tile
                    jigsaw[-1].append(tile)
                    tiles.remove(tile)
                    break
                if tile.top_edge()[::-1] == jigsaw[-2][0].bottom_edge():
                    # flip and add tile
                    tile.flip_x()
                    jigsaw[-1].append(tile)
                    tiles.remove(tile)
                    break
                tile.rotate()
        else:
            # add to the right
            for i in range(4):
                if tile.left_edge() == jigsaw[-1][-1].right_edge():
                    # add tile
                    jigsaw[-1].append(tile)
                    tiles.remove(tile)
                    break
                if tile.left_edge()[::-1] == jigsaw[-1][-1].right_edge():
                    # flip and add tile
                    tile.flip_y()
                    jigsaw[-1].append(tile)
                    tiles.remove(tile)
                    break
                tile.rotate()
    r = jigsaw[-1][-1].right_edge()
    if r in unique_edges or r[::-1] in unique_edges:
        jigsaw.append([])

# assemble image
img = []
offset = 0
for y in range(len(jigsaw)-1):
    for i in range(len(jigsaw[y][0].tile)-2):
        img.append("")
    for x in range(len(jigsaw[y])):
        jigsaw[y][x].remove_edges()
        for i in range(len(jigsaw[y][x].tile)):
            img[offset + i] += "".join(jigsaw[y][x].tile[i])
    offset += len(jigsaw[y][0].tile)

def print_img(img):
    for line in img:
        print(line)

def rotate_img(img):
    img = list(zip(*img[::-1]))
    for i in range(len(img)):
        img[i] = "".join(img[i])
    return img

def flip_img_y(img):
    return img[::-1]

sea_monster = ["..................#.",
               "#....##....##....###",
               ".#..#..#..#..#..#..."]
hash_per_monster = 15

def count_monsters(img):
    cnt = 0
    for y in range(len(img) - len(sea_monster)):
        for x in range(len(img[y]) - len(sea_monster[0])):

            monster = True
            for Y in range(len(sea_monster)):
                for X in range(len(sea_monster[Y])):
                    if sea_monster[Y][X] == "#" and img[Y+y][x+X] != "#":
                        monster = False
                        break
            if monster: cnt += 1

    return cnt

part2 = 0
for line in img: part2 += line.count("#")

for i in range(4):
    cnt = count_monsters(img)
    if cnt > 0:
        print("Part 2:", part2 - cnt * hash_per_monster)
#        break
    cnt = count_monsters(flip_img_y(img))
    if cnt > 0:
        print("Part 2:", part2 - cnt * hash_per_monster)
#        break
    img = rotate_img(img)

"""
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

"""

