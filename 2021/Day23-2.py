from _collections import deque
from heapq import *

H = 11
R = 2

part2 = True

f = open("Day23.txt").read().split("\n")
if part2:
    R = 4
    f.insert(3,"  #D#C#B#A#  ")
    f.insert(4,"  #D#B#A#C#  ")
room = [[0 for i in range(R)], [0 for i in range(R)], [0 for i in range(R)], [0 for i in range(R)]]
erg = {"A":1, "B":10, "C":100, "D":1000}
dest ={"A":H, "B":H+R, "C":H+R+R, "D":H+R+R+R}
hall ={H:2, H+R:4, H+R+R:6, H+R+R+R:8}
hallway = [0,1,3,5,7,9,10]

"""
#############
#PP.P.P.P.PP#
###X#X#X#X###
  #X#X#X#X#
  #X#X#X#X#
  #X#X#X#X#
  #########
  """

for i in range(2,2+R):
    r = 0
    for j in f[i]:
        if j in "ABCD":
            room[r][i-2] = j
            r += 1

print(room)
start = "..........."
for i in range(4):
    for j in range(R): start += room[i][j]
q = [(0, start)]
seen = dict()
before = dict()
seen[start] = 0
fin = "..........." + ("A" * R) + ("B" * R) + ("C" * R) + ("D" * R)
print(fin)

print(start)

def clear(a, b, pos):
    # assumes that both a and b are okay
    d = 0
    if a >= H:
        a = hall[a]
        d += 1
    if b >= H:
        b = hall[b]
        d += 1

    # just moving in hallway
    for i in range(min(a,b) + 1, max(a,b)):
        if pos[i] != ".": return False

    d += abs(b - a)

    return d

def move_to_hall(i, j, pos):
    if pos[j] != ".": return False
    v = pos[i]
    d = 1
    p = list(pos)
    q = i - H
    p[i] = "."
    for o in range(q % R):
        if pos[i - 1] != ".": return False
        d += 1
        i -= 1

    p[j] = v
    i = hall[i]

    c = clear(i, j, pos)
    if not c: return False
    d += c

    return (d * erg[v], "".join(p))


def move_to_room(i, pos):
    v = pos[i]
    r = dest[v]
    a = r - 1
    d = -1
    p = list(pos)
    p[i] = "."
    place = False
    for o in range(R):
        if pos[r+o] == ".":
            d += 1
            a += 1
        elif pos[r+o] != v:
            return False
        if r+o == i: place = True
    p[a] = v

    if place:
        if a <= i: return False

    c = clear(i, r, pos)
    if not c: return False
    d += c

    return (d * erg[v], "".join(p))

def better(d, pos, prev = ""):
    global seen
    if pos not in seen:
        seen[pos] = d
        before[pos] = prev
        return True
    if d < seen[pos]:
        seen[pos] = d
        before[pos] = prev
        return True
    return False

def output(p):
    a = p[:H]
    for i in range(4):
        a += "|" + p[H+i*R:H+(i+1)*R]
    print(a)
t = 100
while q:
    d, pos = heappop(q)

#    if d > 0: continue
    if d >= t:
        print(d)
        t += 100

#    print(d, end=" ")
#    output(pos)

    if pos == fin:
        print(d)
        output(pos)
        while pos != start:
            pos = before[pos]
            print(seen[pos], end=" ")
            output(pos)

        if part2: print("Part 2:", end=" ")
        else: print("Part 1:", end=" ")
        print(d)

        break

    # move people into their room
    for i in range(H):
        if pos[i] != ".":
            # can move to room?
            p = move_to_room(i, pos)
            if p and better(p[0] + d, p[1], pos):
                heappush(q, (p[0] + d, p[1]))

    # move people into the hallway
    for i in range(H, len(pos)):
        if pos[i] != ".":
            for j in hallway:
                # can move to hall?
                p = move_to_hall(i,j,pos)
#                print(i, j, p)
                if p and better(p[0] + d, p[1], pos):
#                    print("!")
                    heappush(q, (p[0] + d, p[1]))
