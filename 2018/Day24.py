from math import *

class group:

    def __init__(self, units, hp, weak, immune, attack, attack_type, initiative):
        self.units = units
        self.hp = hp
        self.weak = set(weak)
        self.immune = set(immune)
        self.attack = attack
        self.attack_type = attack_type
        self.initiative = initiative

    def expected_damage(self, attack, attack_type):
        if attack_type in self.weak: return attack * 2
        elif attack_type in self.immune: return 0
        else: return attack

    def effective_power(self):
        return self.attack * self.units

    def damage(self, attack, attack_type):
        if attack_type in self.weak: attack *= 2
        elif attack_type in self.immune: attack = 0
        units_dead = attack // self.hp
#        print(attack, self.hp, units_dead)
        self.units -= units_dead
        return self.units <= 0

def copy(army):
    new_army = []
    for i in army:
        j = group(i.units, i.hp, i.weak, i.immune, i.attack, i.attack_type, i.initiative)
        new_army.append(j)
    return new_army

with open("input/24.txt") as f:
    all_data = f.read().split("\n")

immune = []
infection = []
curr = []
ptr = 0
while ptr < len(all_data):
    line = all_data[ptr]
    if len(line) < 5:
        ptr += 1
        continue
    line = line.strip().split()

    if line[0] == "Immune":
        curr = immune
        ptr += 1
    elif line[0] == "Infection:":
        curr = infection
        ptr += 1

    else:
        _units = int(line[0])
        _hp = int(line[4])

        _weak = set()
        _immune = set()
        if "(" in all_data[ptr]:
            l = all_data[ptr].replace("(", ")").split(")")[1].split(";")
            _curr = set()
            for item in l:
                item = item.split()
                if item[0] == "weak": _curr = _weak
                elif item[0] == "immune": _curr = _immune

                for i in range(2, len(item)):
                    attack_type = item[i].replace(",", "").strip()
                    _curr.add(attack_type)

        i = 0
        while line[i] != "does": i += 1
        _attack = int(line[i+1])
        _attack_type = line[i+2]
        _initiative = int(line[-1])

#        print(_units, _hp, _weak, _immune, _attack, _attack_type, _initiative)
        soldier = group(_units, _hp, _weak, _immune, _attack, _attack_type, _initiative)
        curr.append(soldier)

        ptr += 1

#print("syart")

def run(immune, infection, boost=0):

    for i in immune:
        i.attack += boost

    while len(infection) > 0 and len(immune) > 0:
        order = []
        for i in infection:
            order.append((i.effective_power(), i.initiative, i, "infection"))
        for i in immune:
            order.append((i.effective_power(), i.initiative, i, "immune"))
        order = sorted(order)[::-1]
    #    print(order)
        can_target_immune = list(immune)
        can_target_infection = list(infection)
        attack_order = []

        for a, b, soldier, side in order:
            targets = []
            _attack = soldier.attack * soldier.units
            if side == "immune":
                for i in can_target_infection:
                    targets.append((i.expected_damage(_attack, soldier.attack_type), i.effective_power(), i.initiative, i))
            else:
                for i in can_target_immune:
                    targets.append((i.expected_damage(_attack, soldier.attack_type), i.effective_power(), i.initiative, i))
            targets = sorted(targets)[::-1]
            if len(targets) > 0:
                a, b, c, target = targets[0]
                if target.expected_damage(_attack, soldier.attack_type) > 0:
                    attack_order.append((soldier.initiative, soldier, target))
                    if side == "immune":
                        can_target_infection.remove(target)
                    else:
                        can_target_immune.remove(target)

        attack_order = sorted(attack_order)[::-1]
        if len(attack_order) == 0:
#            print("!!!")
            return False, 0
    #    print(attack_order)

        dead = 0
        for a, soldier, target in attack_order:
            if soldier.units > 0:
                # attack!
#                print(soldier.initiative, "attacks", target.initiative)
                before = target.units
                target.damage(soldier.attack * soldier.units, soldier.attack_type)
                dead += before - target.units
#                print("kills", before - target.units, "units")
#                print(soldier.attack * soldier.units)

        if dead == 0:
#            print("!!")
            return False, 0

        new_immune = []
        new_infection = []
        for i in immune:
            if i.units > 0: new_immune.append(i)
        for i in infection:
            if i.units > 0: new_infection.append(i)
        immune = new_immune
        infection = new_infection

        """
        print("immune:")
        for item in immune:
            print(item.initiative, item.units)
        print("infection:")
        for item in infection:
            print(item.initiative, item.units)
        """

    ans = 0
    if len(immune) > 0:
        for i in immune:
            ans += i.units
        return True, ans
    if len(infection) > 0:
        for i in infection:
            ans += i.units
        return False, ans


print("Part 1:", run(copy(immune), copy(infection))[1])
#print(run(copy(immune), copy(infection), 1570))
boost = 0
lower = 1
upper = 10000
while True:
    boost = int((upper + lower) / 2)
#    if boost % 100 == 0: print(boost)
    win, ans = run(copy(immune), copy(infection), boost)
    if win:
        upper = boost
        if lower == upper:
            print("Part 2:", ans)
            break
    else:
        lower = boost+1

#print("Done")



