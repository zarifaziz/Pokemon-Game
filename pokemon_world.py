# Author: Zarif Aziz


from random import randint
from random import choice
import time
import math

class Pokemon(object):

    # state variable that needs to be seen my the other class
    defending = 0

    def __init__(self, name):
        self.name = name

    # Pokemon has an attack function
    def attack(self,  target, action):

        user.defending = 0
        damage = 0
        time.sleep(1)
        # If your opponent is defending
        if target.defending == 1:
            print "%s attacks %s with %s, but it's defending!" % (self.name, target.name, action)
            # Inflict relatively smaller damage
            damage = int(self.moves[action]) - randint(1,5)
            target.hp = target.hp - damage
        else:
            print "%s attacks %s with %s,  it's very effective!" % (self.name, target.name, action)
            # Inflict relatively higher damage
            damage = int(self.moves[action]) + randint(6,15)
            target.hp = target.hp - damage

        time.sleep(1)
        print "%s's HP decreases by %s points" % (target.name, damage)

    # Pokemon has a defend function
    def defend(self):
        self.defending = 1
        print "%s is trying to defend" % (self.name)

# 1) Pikachu
# 2) Lapras
# 3) Gengar
# 4) Charizard

    arsenal ={
        '1' : 'Pikachu',
        '2' : 'Lapras',
        '3' : 'Gengar',
        '4' : 'Charizard'
    }
    # Learn how to make a dictionary to obtain pokemon

    def choose(self, number):
        return Pokemon.arsenal.get(number)
