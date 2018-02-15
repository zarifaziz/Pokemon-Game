# Author: Zarif Aziz

from pokemon_world import Pokemon
from random import randint
from random import choice
import time
import math

class Charizard(Pokemon):

    def __init__(self, name):
        super(Charizard, self).__init__(name)

    hp = 500
    healing_rate = 5

    moves = {
        'Flamethrower' : '50',
        'Fire Blast' : '70',
        'Shadow Claw' : '70',
        'Wing Attack' : '60'
    }

class Dragonite(Pokemon):

    def __init__(self, name):
        super(Dragonite, self).__init__(name)

    hp = 700
    healing_rate = 6

    moves = {
        'Hyper Beam': '110',
        'Inferno' : '90',
        'Slash' : '50',
        'Dragon Rush': '50'
    }
