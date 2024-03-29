import time

with open("inputs/Day6.txt") as f:
    packet = f.read().strip()

for i in range(len(packet)):
    if len(set(packet[i:i+4])) == 4:
        print("Part 1:", i+4)
        break

for i in range(len(packet)):
    if len(set(packet[i:i+14])) == 14:
        print("Part 2:", i+14)
        break