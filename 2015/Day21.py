import sys

class player:

    def __init__(self, hp, armour, attack):
        self.hp = hp
        self.armour = armour
        self.attack = attack

    def incArmour(self, v):
        self.armour += v

    def incHealth(self, v):
        self.hp += v

    def incAttack(self, v):
        self.attack += v

    def hurt(self, a):
        self.hp -= max(0, a - self.armour)
        return self.hp <= 0

def simulate(p1, p2):
    while True:
        if p2.hurt(p1.attack): return True
        if p1.hurt(p2.attack): return False

with open("inputs/Day21.txt") as f:
    data = f.read().strip().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split()
    enemy_hp = int(data[0][2])
    enemy_dmg = int(data[1][1])
    enemy_armour = int(data[2][1])

minGold = float("inf")
maxGold = 0

weaponsCost = [8,10,25,40,74]
weaponsAttack = [4,5,6,7,8]
armourCost = [13,31,53,75,102,0]
armourArmour = [1,2,3,4,5,0]
ringsCost = [25,50,100,20,40,80,0,0]
ringsAttack = [1,2,3,0,0,0,0,0]
ringsArmour = [0,0,0,1,2,3,0,0]

for w in range(len(weaponsCost)):
    for a in range(len(armourCost)):
        for r1 in range(len(ringsCost)):
            for r2 in range(r1):
                enemy = player(enemy_hp, enemy_armour, enemy_dmg)
                gold = weaponsCost[w] + armourCost[a] + ringsCost[r1] + ringsCost[r2]
                p = player(100, armourArmour[a] + ringsArmour[r1] + ringsArmour[r2], weaponsAttack[w] + ringsAttack[r1] + ringsAttack[r2])
                if simulate(p, enemy):
                    minGold = min(minGold, gold)
                else:
                    maxGold = max(maxGold, gold)

print("Part 1:", minGold)
print("Part 2:", maxGold)
