
f = open("Day21.txt", "r")
text = f.read().split("\n")

twodict = dict()
threedict = dict()

def rotate(arr):
    arr = arr.split("/")
    print(list(zip(*arr[::-1])))
    arr = list(zip(*arr[::-1]))
    for i in range(len(arr)):
        arr[i] = "".join(arr[i])
    return "/".join(arr)

def flipx(arr):
    arr = arr.split("/")
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return "/".join(arr)

def flipy(arr):
    arr = arr.split("/")
    return "/".join(arr[::-1])

def twox(arr):
    arr = twodict["/".join(arr)]
    return arr.split("/")

def threex(arr):
    arr = threedict["/".join(arr)]
    return arr.split("/")

def output(fractal):
    for i in fractal: print(i)

# read in the rules
for line in text:
    a, b = line.split(" => ")
    if len(a) == 5:
        twodict[a] = b
        twodict[flipx(a)] = b
        twodict[flipy(a)] = b
        #
        a = rotate(a)
        twodict[a] = b
        twodict[flipx(a)] = b
        twodict[flipy(a)] = b
        #
        a = rotate(a)
        twodict[a] = b
        twodict[flipx(a)] = b
        twodict[flipy(a)] = b
        #
        a = rotate(a)
        twodict[a] = b
        twodict[flipx(a)] = b
        twodict[flipy(a)] = b
    else:
        threedict[a] = b
        threedict[flipx(a)] = b
        threedict[flipy(a)] = b
        #
        a = rotate(a)
        threedict[a] = b
        threedict[flipx(a)] = b
        threedict[flipy(a)] = b
        #
        a = rotate(a)
        threedict[a] = b
        threedict[flipx(a)] = b
        threedict[flipy(a)] = b
        #
        a = rotate(a)
        threedict[a] = b
        threedict[flipx(a)] = b
        threedict[flipy(a)] = b

fractal = [".#.", "..#", "###"]
#fractal = threex(fractal)

# n is iterations
n = 18
for i in range(n):
#    print(i)
    if (len(fractal) % 2 == 0):
        # split by two
        newfractal = []
        for y in range(0, len(fractal), 2):
            newfractal += ["", "", ""]
            for x in range(0, len(fractal[y]), 2):
                arr = [fractal[y][x] + fractal[y][x+1], fractal[y+1][x] + fractal[y+1][x+1]]
                arr = twox(arr)
                newfractal[-3] += arr[0]
                newfractal[-2] += arr[1]
                newfractal[-1] += arr[2]
        fractal = list(newfractal)
    else:
        newfractal = []
        for y in range(0, len(fractal), 3):
            newfractal += ["", "", "", ""]
            for x in range(0, len(fractal[y]), 3):
                arr = [fractal[y][x] + fractal[y][x+1] + fractal[y][x+2],
                       fractal[y+1][x] + fractal[y+1][x+1] + fractal[y+1][x+2],
                       fractal[y+2][x] + fractal[y+2][x+1] + fractal[y+2][x+2]
                       ]
                arr = threex(arr)
                newfractal[-4] += arr[0]
                newfractal[-3] += arr[1]
                newfractal[-2] += arr[2]
                newfractal[-1] += arr[3]
        fractal = list(newfractal)

    if i == 4:
        tot = 0
        for i in fractal:
            for j in i:
                if j == "#": tot += 1
        print("Part 1:", tot)
#    print()
#    output(fractal)

tot = 0
for i in fractal:
    for j in i:
        if j == "#": tot += 1
print("Part 2:", tot)

