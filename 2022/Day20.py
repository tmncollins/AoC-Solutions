from collections import *
import time

with open("inputs/Day20.txt") as f:
    all_data = f.read().split("\n")

nums = deque()

def mix(nums):

    x = len(nums)
    #print(nums)
    for j in range(x):
        i, cnt = nums[0]
        while cnt != j:
            nums.rotate(-1)
            i, cnt = nums[0]

        nums.popleft()

        I = i % len(nums)
        nums.rotate(-I)
        nums.appendleft((i, cnt))
        nums.rotate(I)
        nums.rotate(-1)
    #    print(nums)

    return nums

cnt = 0
for line in all_data:
    if len(line) > 0:
        nums.append((int(line), cnt))
        cnt += 1

start1 = time.time()
part1 = mix(deque(nums))
while part1[0][0] != 0:
    part1.rotate(-1)
coordinates = 0
for i in range(3):
    part1.rotate(-1000)
    coordinates += part1[0][0]
print("Part 1:", coordinates)
#print(time.time() - start1)

#print(nums)
part2 = deque(nums)
for i in range(len(nums)):
    part2[0] = (part2[0][0] * 811589153, part2[0][1])
    part2.rotate(-1)
for i in range(10):
    print(i)
#    print(part2)
    part2 = mix(part2)

while part2[0][0] != 0:
    part2.rotate(-1)
coordinates = 0
for i in range(3):
    part2.rotate(-1000)
    coordinates += part2[0][0]
print("Part 2:", coordinates)
