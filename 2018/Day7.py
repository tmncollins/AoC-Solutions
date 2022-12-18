from _collections import defaultdict

with open("input/7.txt") as f:
    rules = f.readlines()

req = defaultdict(set)
req2 = defaultdict(set)
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cost = {alpha[i] : i+1 for i in range(26)}

tasks = set()
for line in rules:
    line = line.replace("\n", "")
    line = line.split()
    a = line[1]
    b = line[7]

    req[b].add(a)
    req2[b].add(a)
    tasks.add(a)
    tasks.add(b)

tasks = list(tasks)
tasks = sorted(tasks)

TASKS = list(tasks)

def completeTask(i):
    t = tasks[i]
    tasks.remove(t)
    for item in tasks:
        if t in req[item]:
            req[item].remove(t)

ans = ""
while len(tasks) > 0:
    for i in range(len(tasks)):
        if len(req[tasks[i]]) == 0:
            ans += tasks[i]
            completeTask(i)
            break

print("Part 1:", ans)

w_task = ["" for i in range(5)]
w_time = [0 for i in range(5)]
tasks = list(TASKS)

time = 0
W = 5
COST = 60
while len(tasks) > 0:
    for j in range(len(tasks)):
        if len(req2[tasks[j]]) == 0:
            for i in range(W):
                if w_task[i] == "":
                    w_task[i] = tasks[j]
                    w_time[i] = COST + cost[tasks[j]]
                    break
    for item in w_task:
        if item in tasks: tasks.remove(item)

    time += 1
    for i in range(5):
        if w_time[i] > 0:
            w_time[i] -= 1
        if w_time[i] == 0:
            for task in tasks:
                if w_task[i] in req2[task]: req2[task].remove(w_task[i])

            w_task[i] = ""

for item in w_time: time += item
print("Part 2:", time)

