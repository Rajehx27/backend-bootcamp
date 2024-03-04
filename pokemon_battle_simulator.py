# each player has 5 pokemons
from enum import Enum
import random


# continue battle

class Ptype(Enum):
    FIRE = 1
    WATER = 2
    EARTH = 3
    WIND = 4


class Pokemon:
    def __init__(self, name, level, strenght, speed, ptype, life):
        self.name = name
        self.level = level
        self.strenght = strenght
        self.speed = speed
        self.ptype: Ptype.value = ptype  # to be sure that's how we use enum in python
        self.life = life

    def isAlive(self):
        if self.life > 0:
            return True


# p1 = Pokemon("pica", 5, 15, 3, 4, 120)
# print(p1.ptype)
# print(Ptype(p1.ptype))

class Player:
    def __init__(self, name, curr_pokemon, pokemons=None):
        self.name = name
        self.curr_pokemon = curr_pokemon
        self.pokemons = pokemons
        self.alive = True


def attack(pokemon1: Pokemon, pokemon2: Pokemon):
    type_modifier = 1
    # match pokemon1.ptype:
    #     case '1':
    if ((pokemon1.ptype == 1 and (pokemon2.ptype == 2 or pokemon2.ptype == 4)) or
            (pokemon1.ptype == 2 and (pokemon2.ptype == 1 or pokemon2.ptype == 3)) or
            (pokemon1.ptype == 3 and (pokemon2.ptype == 1 or pokemon2.ptype == 4)) or
            (pokemon1.ptype == 4 and pokemon2.ptype == 2)):
        type_modifier = 2
    damage = type_modifier * (random.randint(1, 20) + pokemon1.strenght)
    pokemon2.life -= damage
    print(f"pokemon {pokemon1.name} attacks pokemon {pokemon2.name}, deals {damage} damage")
    print(f"pokemon {pokemon2.name} has now {pokemon2.life} amount of life after the attack")


def attack_first(p1: Player, p2: Player):
    tmp1 = random.randint(1, 20) + p1.curr_pokemon.speed
    tmp2 = random.randint(1, 20) + p2.curr_pokemon.speed
    if tmp1 > tmp2:
        return [p1, p2]
    else:
        return [p2, p1]


def battle(p1: Player, p2: Player):
    attacker, defender = attack_first(p1, p2)

    while attacker.alive and defender.alive:
        attack(attacker.curr_pokemon, defender.curr_pokemon)
        if defender.curr_pokemon.life <= 0:
            print("pokemon ", defender.curr_pokemon.name, " has died")
            if len(defender.pokemons) > 0:
                defender.curr_pokemon = defender.pokemons.pop(random.randint(0, len(defender.pokemons) - 1))
                print("pokemon ", defender.curr_pokemon.name, " has joined the fight")
            else:
                defender.alive = False
                continue
        attacker, defender = defender, attacker

    if attacker.alive:
        print("Congrats plyer ", attacker.name, " You won!")
    else:
        print("Congrats plyer ", defender.name, " You won!")


pokemons1 = []
pokemons2 = []
for i in range(5):
    temp1 = Pokemon(i, i, random.randint(1, 10), random.randint(1, 5), random.randint(1, 4), 120)
    temp2 = Pokemon(i, i, random.randint(1, 10), random.randint(1, 5), random.randint(1, 4), 120)
    pokemons1.append(temp1)
    pokemons2.append(temp2)
    # print("name + lvl:", temp.name, temp.level, ",str: ", temp.strenght, ",speed: ", temp.speed, ",type: ", Ptype(temp.ptype), ",life: ", temp.life)

poke1 = pokemons1.pop(random.randint(0, 4))
poke2 = pokemons2.pop(random.randint(0, 4))
print(poke1.name, poke1, "fffffffffffffffffffffffff", poke2.name, poke2)
player1 = Player(1, poke1, pokemons1)
player2 = Player(2, poke2, pokemons2)

print("pokemon1: ", len(player1.pokemons),"fooooooooofff-----------", len(player2.pokemons) , " player2")
print("pokemin2: ", player2.curr_pokemon.name, player2.curr_pokemon)

battle(player1, player2)
