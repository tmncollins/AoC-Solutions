from math import *

with open("inputs/Day6.txt") as file:
    data = file.read().strip().split("\n")

def quad(t, m):
    a = 0.5*(t+sqrt(t**2-(4*m)))
    b = 0.5*(t-sqrt(t**2-(4*m)))
    return a,b

times = []
time_2 = 0
distance_2 = 0
distances = []
for line in data:
    if "Time" in line:
        line = line.split()[1:]
        time_2 = int("".join(line))
        times = list(map(int, line))
    elif "Distance" in line:
        line = line.split()[1:]
        distance_2 = int("".join(line))
        distances = list(map(int, line))

part1 = 1
for i in range(len(times)):
    a, b = quad(times[i], distances[i]+1)
    if a != int(a): a = int(a)
    if b != int(b): b = int(b) + 1
    range = a+1-b
    part1 *= range

print("Part 1:", part1)

a, b = quad(time_2, distance_2)
if a != int(a): a = int(a)
if b != int(b): b = int(b) + 1
part2 = a + 1 - b

print("Part 2:", part2)

