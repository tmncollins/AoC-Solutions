from _collections import *

jump = 304
spinlock = deque()
spinlock.append(0)

num = 50000000
for i in range(num):
    if i % 1000000 == 0: print(i)
    spinlock.rotate(-jump)
#    print(spinlock)
    spinlock.append(i+1)
    if i == 2016:
        print("Part 1:", spinlock[0])

while spinlock[0] != 0: spinlock.rotate(1)
spinlock.rotate(-1)
print("Part 2:", spinlock[0])