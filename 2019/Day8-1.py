from collections import defaultdict

with open("input/8.txt") as f:
    data = f.readline().replace("\n", "")
    data = list(data)

X,Y = 25,6
Z = len(data) // (X*Y)
image = []
for z in range(Z):
    image.append([])
    for y in range(Y):
        image[z].append([])
        for x in range(X):
            image[z][y].append(data.pop(0))
print(image)

min0 = 99999999
min1x2 = 0
for layer in image:
    counter = defaultdict(int)
    for y in range(Y):
        for x in range(X):
            counter[layer[y][x]] += 1
    if counter["0"] < min0:
        min0 = counter["0"]
        min1x2 = counter["1"] * counter["2"]
print(min0, min1x2)