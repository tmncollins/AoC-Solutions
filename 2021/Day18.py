from math import *

def canExplode(snailfish):
    if type(snailfish[0]) is int and type(snailfish[1]) is int: return True
    return False

def reduceExplode(snailfish, depth=1):
    print(depth)

    if canExplode(snailfish):
        return snailfish, [0,0]

    changed = False

    if type(snailfish[0]) is not int:
        if depth >= 4 and canExplode(snailfish[0]):
            # explode
            print("explode!")
            return [0, snailfish[1] + snailfish[0][1]], [snailfish[0][0], 0]
        else:
            x = reduceExplode(snailfish[0], depth + 1)
            if x[0] != snailfish[0]:
                snailfish[0] = x[0]
                if snailfish[1] is int:
                    snailfish[1] += x[1][1]
                    x[1][1] = 0
                return snailfish, x[1]

    if type(snailfish[1]) is not int:
        if depth >= 4 and canExplode(snailfish[1]):
            print("explode!")
            return [snailfish[0] + snailfish[1][0], 0], [0, snailfish[1][1]]
        else:
            x = reduceExplode(snailfish[1], depth + 1)
            print(x, "right")
            if x[0] != snailfish[1]:
                snailfish[1] = x[0]
                if snailfish[0] is int:
                    snailfish[0] += x[1][0]
                    x[1][0] = 0
                return snailfish, x[1]

    return snailfish, [0, 0]

def redExp(nums):
    depth = 0
    exp, left, right = 0,0,0
    for i in range(len(nums)):
        if nums[i] == "[":
            depth += 1
        elif nums[i] == "]":
            depth -= 1
        else:
            if depth >= 5 and type(nums[i]) is int and type(nums[i+1]) is int:
                # explode
                exp = i
                left = nums[i]
                right = nums[i+1]
                for _ in range(4):
                    nums.pop(i-1)
                nums.insert(i-1, 0)
                break
    li = exp - 1
    while li > 0:
        li -= 1
        if type(nums[li]) is int:
            nums[li] += left
            break
    ri = exp
    while ri < len(nums):
        if type(nums[ri]) is int:
            nums[ri] += right
            break
        ri += 1

    return nums

    print(exp, left, right)
    print(nums)

def add(a, b):
    return ["["] + a + b + ["]"]

def redSplit(nums):
    for i in range(len(nums)):
        if type(nums[i]) is int and nums[i] >= 10:
            v = nums.pop(i)
            nums.insert(i, "]")
            nums.insert(i, ceil(v/2))
            nums.insert(i, floor(v/2))
            nums.insert(i, "[")
            break
    return nums

def process(string):
    a = []
    for i in string:
        try:
            i = int(i)
            a.append(i)
        except:
            if i in ["[", "]"]:
                a.append(i)
    return a

def reduce(nums):
    last = list(nums)
    while True:
        nums = redExp(nums)
        if nums == last:
            nums = redSplit(nums)
            if nums == last:
                return nums
        last = list(nums)
#        print(nums)

def mag(nums):
    for i in range(len(nums)):
        if type(nums[i]) is int and type(nums[i+1]) is int:
            v = 3 * nums[i] + nums[i+1] * 2
            for _ in range(4):
                nums.pop(i-1)
            nums.insert(i-1, v)
            break

    return nums

def magnitude(nums):
    last = list(nums)
    while True:
        nums = mag(nums)
        if len(nums) == 1:
            return nums[0]
        last = list(nums)
#        print(nums)



data = open("Day18.txt").read().split("\n")
snailfish = add(process(data[0]), process(data[1]))
snailfish = reduce(snailfish)
for i in range(2, len(data)):
    snailfish = add(snailfish, process(data[i]))
    snailfish = reduce(snailfish)
print("Part 1:", magnitude(snailfish))

best = 0
for i in range(len(data)):
    for j in range(len(data)):
        if i != j:
            a, b = data[i], data[j]
            snail = add(process(a), process((b)))
            snail = reduce(snail)
            m = magnitude(snail)
            best = max(m, best)

print("Part 2:", best)