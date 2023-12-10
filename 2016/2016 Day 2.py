
with open("inputs/Day2.txt") as f:
    all_data = f.read().split("\n")

positions = {(-1, -1):"1", (0, -1):"2", (1, -1):"3",
             (-1,0):"4", (0,0):"5", (1,0):"6",
             (-1,1):"7", (0,1):"8", (1,1):"9"}

pos = (0, 0)
move = {"U": (0, -1), "L": (-1, 0), "R": (1, 0), "D": (0, 1)}

code = ""
for line in all_data:
    line = line.strip()
    if len(line) < 3: continue

    for c in line:
        npos = (pos[0] + move[c][0], pos[1] + move[c][1])
        if npos in positions:
            pos = npos

    code += positions[pos]

print("Part 1:", code)

positions = {                               (0, -2):"1",
                            (-1, -1):"2",   (0, -1):"3",    (1, -1):"4",
             (-2, 0):"5",   (-1,  0):"6",   (0,  0):"7",    (1,  0):"8",    (2,  0):"9",
                            (-1,  1):"A",   (0,  1):"B",    (1,  1):"C",
                                            (0,  2):"D"
            }

code = ""
for line in all_data:
    line = line.strip()
    if len(line) < 3: continue

    for c in line:
        npos = (pos[0] + move[c][0], pos[1] + move[c][1])
        if npos in positions:
            pos = npos

    code += positions[pos]

print("Part 2:", code)
