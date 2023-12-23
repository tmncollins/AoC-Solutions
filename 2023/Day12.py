from functools import lru_cache

@lru_cache(maxsize=None)
def can_place(run_ptr, hash_ptr, dot_ptr, i):
    global current_input, current_runs, n, current_hash_pos, current_dot_pos

    # base case
    if run_ptr >= len(current_runs):
        return int(hash_ptr >= len(current_hash_pos))
    if i >= n:
        return 0

    # can we start the next run here?
    end = i + current_runs[run_ptr]
    do_run = 0
    dont_run = 0

    # choose not to end run
    if hash_ptr >= len(current_hash_pos) or i != current_hash_pos[hash_ptr]:
        dot_ptr_2 = dot_ptr
        if dot_ptr < len(current_dot_pos) and current_dot_pos[dot_ptr] == i:
            dot_ptr_2 += 1
        dont_run = can_place(run_ptr, hash_ptr, dot_ptr_2, i+1)

    # is there a dot in this run?
    if end <= n and (dot_ptr >= len(current_dot_pos) or current_dot_pos[dot_ptr] >= end):
        # we can start the run here
        while hash_ptr < len(current_hash_pos) and current_hash_pos[hash_ptr] < end:
            hash_ptr += 1
        while dot_ptr < len(current_dot_pos) and current_dot_pos[dot_ptr] <= end:
            dot_ptr += 1

        # the next position cannot be a hash
        if hash_ptr >= len(current_hash_pos) or current_hash_pos[hash_ptr] > end:
            do_run = can_place(run_ptr+1, hash_ptr, dot_ptr, end+1)

#    print(i, dont_run, do_run)

    return int(do_run + dont_run)

with open("inputs/Day12.txt") as file:
    data = file.read().strip().split("\n")

part1 = 0
part2 = 0
for line in data:
    if len(line) > 3:
        # input
        current_input, runs = line.split()

        # part 1
        can_place.cache_clear()
        current_runs = list(map(int, runs.split(",")))
        n = len(current_input)
        current_hash_pos = []
        current_dot_pos = []
        for i in range(n):
            if current_input[i] == "#":
                current_hash_pos.append(i)
            elif current_input[i] == ".":
                current_dot_pos.append(i)

        ways = can_place(0, 0, 0, 0)
        part1 += ways

        # part 2
        can_place.cache_clear()
        ci = current_input
        for i in range(4):
            current_input += "?" + ci
        cr = runs
        for i in range(4):
            runs += "," + cr

        n = len(current_input)
        current_runs = list(map(int, runs.split(",")))
        current_hash_pos = []
        current_dot_pos = []
        for i in range(n):
            if current_input[i] == "#":
                current_hash_pos.append(i)
            elif current_input[i] == ".":
                current_dot_pos.append(i)

        ways = can_place(0, 0, 0, 0)
        part2 += ways

print("Part 1:", part1)
print("Part 2:", part2)

