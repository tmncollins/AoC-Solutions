from copy import deepcopy
from functools import lru_cache

with open("inputs/Day22.txt") as f:
    data = f.read().strip().split("\n")
    enemy_hp = int(data[0].split()[2])
    enemy_dmg = int(data[1].split()[1])


@lru_cache(maxsize=None)
def turn(mana, mana_used, hp, enemy_hp, effects, player_turn, hard=False):
    global enemy_dmg

    expired_effects = []
    current_effects = [False for i in range(3)]
    armour = 0
    effects = list(effects)
    for i in range(len(effects)):
        effect = effects[i]
        if effect[0] == 0:
            # poison
            enemy_hp -= 3
        elif effect[0] == 1:
            # shield
            armour = 7
        elif effect[0] == 2:
            # recharge
            mana += 101

        effects[i] = (effect[0], effect[1]-1)
        if effect[1] <= 1:
            expired_effects.append(effects[i])
        else:
            current_effects[effect[0]] = True

    for effect in expired_effects:
        effects.remove(effect)

    effects = tuple(effects)

    if hard and player_turn == 0:
        hp -= 1

    # has either person won?
    if enemy_hp <= 0:
        # enemy is dead
        return mana_used
    if hp <= 0 or mana < 53:
        # player is dead or cannot cast a spell
        return float("inf")

    if player_turn == 0:
        # player turn
        # choose each spell to cast
        min_mana = float("inf")
        # magic missile
        if mana >= 53:
            min_mana = min(min_mana, turn(mana - 53, mana_used + 53, hp, enemy_hp - 4, deepcopy(effects), 1, hard))
        # drain
        if mana >= 73:
            min_mana = min(min_mana, turn(mana - 73, mana_used + 73, hp + 2, enemy_hp - 2, deepcopy(effects), 1, hard))
        # shield
        if mana >= 113 and not current_effects[1]:
            new_effects = list(deepcopy(effects))
            new_effects.append((1, 6))
            min_mana = min(min_mana, turn(mana - 113, mana_used + 113, hp, enemy_hp, tuple(new_effects), 1, hard))
        # poison
        if mana >= 173 and not current_effects[0]:
            new_effects = list(deepcopy(effects))
            new_effects.append((0, 6))
            min_mana = min(min_mana, turn(mana - 173, mana_used + 173, hp, enemy_hp, tuple(new_effects), 1, hard))
        # recharge
        if mana >= 229 and not current_effects[2]:
            new_effects = list(deepcopy(effects))
            new_effects.append((2, 5))
            min_mana = min(min_mana, turn(mana - 229, mana_used + 229, hp, enemy_hp, tuple(new_effects), 1, hard))

        return min_mana

    else:
        # enemy turn
        hp -= max(1, enemy_dmg - armour)
        return turn(mana, mana_used, hp, enemy_hp, effects, 0, hard)


print("Part 1:", turn(500, 0, 50, enemy_hp, (), 0))
print("Part 2:", turn(500, 0, 50, enemy_hp, (), 0, True))
