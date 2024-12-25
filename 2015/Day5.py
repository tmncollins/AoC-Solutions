def nice(s):
    vowels = set("aeiou")
    banned = {"ab", "cd", "pq", "xy"}

    double = False
    vowel_cnt = 0
    if s[0] in vowels: vowel_cnt += 1

    for i in range(1, len(s)):
        if s[i] in vowels: vowel_cnt += 1
        dbl = s[i-1] + s[i]
        if dbl in banned: return False
        if s[i] == s[i-1]: double = True

    return double and (vowel_cnt >= 3)


def nice_v2(s):
    double = False
    split = False

    for i in range(2, len(s)):
        if s[i-2] == s[i]:
            split = True
            break

    for i in range(1, len(s)):
        x = s[i-1] + s[i]
        if x in s[i+1:]:
            double = True
            break

    return double and split


with open("inputs/Day5.txt") as f:
    all_data = f.read().split("\n")

cnt = 0
cnt2 = 0
for line in all_data:
    if nice(line):
        cnt += 1
    if nice_v2(line):
        cnt2 += 1

print("Part 1:", cnt)
print("Part 2:", cnt2)
