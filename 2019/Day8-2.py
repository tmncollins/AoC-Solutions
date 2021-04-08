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

final = [[0 for _ in range(X)] for _ in range(Y)]
for y in range(Y):
    for x in range(X):
        for layer in range(Z):
            if image[layer][y][x] != "2":
                final[y][x] = image[layer][y][x]
                break

for row in final:
    print("".join(row).replace("0", ".").replace("1","#"))