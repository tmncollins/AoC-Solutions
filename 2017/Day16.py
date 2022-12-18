
with open("inputs/16.txt") as f:
    all_data = f.read().strip().split(",")


alpha = "abcdefghijklmnopqrstuvwxyz"
size = 16
dancers = {i:alpha[i] for i in range(size)}

def output():
    line = ""
    for i in range(size):
        line += dancers[i]
    return line

def swap(a, b):
    global dancers
    x = dancers[a]
    dancers[a] = dancers[b]
    dancers[b] = x

def dance():
    global dancers
    for line in all_data:
        if len(line) <= 1: continue

        if line[0] == "s":
            line = int(line[1:])
            new_dancers = dict(dancers)
            for i in range(size):
                new_dancers[(i+line)%size] = dancers[i]
            dancers = new_dancers

        elif line[0] == "x":
            a,b = list(map(int, line[1:].split("/")))
            swap(a,b)

        elif line[0] == "p":
            a,b = list(line[1:].split("/"))
            A,B = 0,0
            for i in range(size):
                if dancers[i] == a: A = i
                if dancers[i] == b: B = i
            swap(A, B)

dance()
print("Part 1:", output())
seen = dict()
seen[output()] = 0
dances = [output()]

target = 1000000000
#target = 200
target -= 1

for i in range(1, 1000000000):
    dance()
    d = output()
    if d in seen:
        j = seen[d]
        cycle = i - j
        k = target % cycle
        print("Part 2:", dances[k])
        break
    else:
        seen[d] = i
    dances.append(d)

#print(dances)

