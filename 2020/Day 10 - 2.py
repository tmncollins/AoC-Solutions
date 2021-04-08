with open('inputs/10.txt', 'r') as f: #open the file
    contents = list(map(int, f.readlines()))

from functools import lru_cache

onedif = 0
threedif = 0
contents = sorted(contents)
contents.append(contents[-1] + 3)

@lru_cache(maxsize=None)
def ways(curr, arr):
#    print(curr, arr)
    if len(arr) == 0 or curr > arr[-1]: return 1
    tot = 0
    for i in range(len(arr)):
        if arr[i] > curr + 3: break
        tot += ways(arr[i], arr[i+1:])
    return tot


print(ways(0, tuple(contents)))