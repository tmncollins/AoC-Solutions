data = open("Day10.txt").read().split("\n")

close = {")":3, "]":57, "}":1197, ">":25137}
opend = {"(":1, "[":2, "{":3, "<":4}
conv = {")":"(", "]":"[", "}":"{", ">":"<"}

score1 = 0
scores = []
for line in data:
    q = []
    corrupt = False
    for i in line:
        if i in close:
            if conv[i] != q[-1]:
                score1 += close[i]
                corrupt = True
                break
            q.pop()
        else:
            q.append(i)
    if not corrupt:
        score = 0
        q = q[::-1]
        for i in q:
            score *= 5
            score += opend[i]
        scores.append(score)


print("Part 1:", score1)
scores = sorted(scores)
print("Part 2:", scores[len(scores) // 2])