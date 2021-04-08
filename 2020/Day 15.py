from _collections import defaultdict

numbers = [0,3,1,6,7,5]

said = dict()

s = -1
rep = 30000000
for i in range(rep):
    if i % 200000 == 0: print("At:", i, "out of", rep)
    if i < len(numbers):
        said[s] = i-1
        s = numbers[i]
    elif s not in said:
        said[s] = i-1
        s = 0
    else:
        last = said[s]
        said[s] = i-1
        s = i - last - 1

print(s)

