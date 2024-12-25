from itertools import product

def can_make_target(target, nums, i=0, value=0, part2=False):
    if i == 0: return can_make_target(target, nums, i+1, nums[0], part2)
    if i == len(nums): return value == target
    if value > target: return False

    if can_make_target(target, nums, i+1, value+nums[i], part2): return True
    if can_make_target(target, nums, i+1, value*nums[i], part2): return True
    if part2 and can_make_target(target, nums, i+1, int(str(value)+str(nums[i])), part2): return True
    return False


def calculate(nums, ops):
    value = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            value += nums[i+1]
        elif ops[i] == "x":
            value *= nums[i+1]
        elif ops[i] == "|":
            value = int(str(value) + str(nums[i+1]))
    return value


def try_operators(target, nums, ops=["x","+"]):
    for state in product(ops, repeat = len(nums)-1):
        if calculate(nums, state) == target:
            return True
    return False

with open("inputs/Day7.txt", "r") as f:
    all_data = f.read().split("\n")

part1 = 0
part2 = 0
repeat_data = []
for line in all_data:
    line = list(map(int, line.replace(":", "").split()))
    if can_make_target(line[0], line[1:]):
        part1 += line[0]
        part2 += line[0]
    else:
        repeat_data.append(line)
print("Part 1:", part1)
for line in repeat_data:
    if can_make_target(line[0], line[1:], part2=True):
        part2 += line[0]

print("Part 2:", part2)