players = 411
last_marble = 71170

from collections import deque

def run(players, last_marble):
    marbles = deque()
    marbles.append(2)
    marbles.append(1)
    marbles.append(0)

    scores = [0 for i in range(players)]

    player = 0
    for marble in range(3, last_marble + 1):
        if marble % 23 == 0:
            scores[player] += marble
            marbles.rotate(7)
            scores[player] += marbles.popleft()
        else:
            marbles.rotate(-2)
            marbles.appendleft(marble)

        player += 1
        player %= players

    return max(scores)

print("Part 1:", run(players, last_marble))
print("Part 2:", run(players, last_marble*100))
