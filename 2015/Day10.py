def look_and_say(s):
    s.append(-1)
    last = -1
    cnt = 0
    new = []

    for c in s:
        if c != last:
            if last != -1:
                new.append(cnt)
                new.append(last)
#                new += str(cnt) + last
            cnt = 0
            last = c
        cnt += 1

    return new

pzl_inp = input("Enter puzzle input:    ").strip()
pzl_inp = list(map(int, list(pzl_inp)))

for i in range(50):
    pzl_inp = look_and_say(pzl_inp)
#    print(i)
    if i == 39:
        print("Part 1:", len(pzl_inp))

print("Part 2:", len(pzl_inp))

