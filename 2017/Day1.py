with open("inputs/1.txt") as f:
    nums = f.read().strip()

part1 = 0
part2 = 0
x = len(nums) // 2
for i in range(len(nums)):
    if nums[i] == nums[(i+1)%len(nums)]:
        part1 += int(nums[i])
    if nums[i] == nums[(i+x) % len(nums)]:
        part2 += int(nums[i])

print("Part 1:", part1)
print("Part 2:", part2)