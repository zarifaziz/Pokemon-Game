# Author Zarif Aziz

# Importing my Pokemon from the PO_Box in another file
from pokemon_battle import Combat
from pokemon_world import Pokemon
from PO_Box import Charizard
from PO_Box import Dragonite
from random import randint
from random import choice
import time
import math



# The Engine that runs the game. Starts with the opening scene and goes to the
# next scene
# I commented out a lot of code because I foound it unnecessary from Zeds code
# but stll keeping it there in case I need it later
class Engine(object):

    #def  __init__(self, scene_map):
        # what does this mean exactly
        # Maybe its so that the variables from the Engine and Map class are connecting
        # or are talking about the same instances ??

        #self.scene_map = scene_map

    def play(self):
        # Initialize the start scene
        #current_scene = self.scene_map.opening_scene()
        current_scene = a_map.opening_scene()
        # The game is constantly running here
        while True:
            print "\n       -------------------     \n"
            # Playing the current scene and storing the return
            # value into the next_scene variable
            next_scene_name = current_scene.enter()
            # updating the current_scene variable so that the next scene plays
            #current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene = a_map.next_scene(next_scene_name)

# The parent class for all the scenes
class Scene(object):

    def enter(self):
        print "This class is not needed for this program but just keeping it here anyway"
        exit(1)

# The intro scene where the game is introduced and you enter your details
class Player(object):

    def __init__(self, name, town):
        # Assigning these variables later
        self.name = name
        self.town = town

    def enter(self):

        time.sleep(0.5)
        print "Loading...."
        time.sleep(1)
        print """\n\n
        You, %s from %s, have
        finally made it to the Pokemon League and are about to challenge the
        Elite Four, a supergroup of the most powerful pokemon trainers! Each trainer has
        a specific fighting style and you have to choose your pokemon carefully
        to beat them! You MUST choose ONE pokemon by their number to beat your opponent.
        """ % (self.name, self.town)

        time.sleep(1)

        print """
        Throughout your journey you have trained some really powerful pokemon and your
        choices are: \n"""

        for no, name in my_pokemon.arsenal.items():
            print "%s : %s" % (no, name)

        print "\nAre you ready?\n"
        ready = raw_input("(y/n)? ")
        if ready == 'y':
            return 'room_1'
        elif ready == 'n':
            exit(1)
        else:
            print "DOES NOT COMPUTE"
            return 'player'

def make_player():
    user = {}

    print """ \n
    Welcome to the world of Pokemon! Please enter your details to get started.
    """
    user['name'] = raw_input('Name: ')
    user['town'] = raw_input('Town: ')

    return user

# Creating Myself
player_object = Player(**make_player())

# Class for the first room
class Room1(object):

    def enter(self):
        print"""
        \n
        You entered the first room and a rush of icy wind hits your face. Waves of
        water splash against the wall on all sides and in the middle is a stage
        made of smooth ice. You meet Lorelei, the water and ice type master.
        She chooses Dewgong! Who do you choose?\n\n
        """

        for no, name in my_pokemon.arsenal.items():
            print "%s : %s" % (no, name)

        ans = raw_input('I choose number: ')

        if not ans.isdigit():
            print" Please enter a number!"
            return 'room_1'
        elif int(ans) is 1:
            print "you chose %s - you win! You go onto the second room." % my_pokemon.choose(ans)
            return 'room_2'
        elif int(ans) > 4:
            print "\nDOES NOT COMPUTE"
            return 'room_2'
        else:
            print "You chose %s but it wasn't strong enough. You got defeated" % my_pokemon.choose(ans)
            return 'pokemon_centre'

# Class for the second room
class Room2(object):

    def enter(self):
        print """
        \n
        You enter the second room which looks like the inside of a cave. The floor
        and walls are all rocky and there are massive brown boulders scattered across
        the room. In the middle stands a tall and bulky figure - the elite trainer
        Bruno who is a rock and fighting type master. You guys go into battle straight
        away and he chooses Machamp, beating its chest loudly with its four massive
        arms. Choose your Pokemon wisely!
\n
        """

        for no, name in my_pokemon.arsenal.items():
            print "%s : %s" % (no, name)

        ans = raw_input('\nI choose number: ')

        if not ans.isdigit():
            print" Please enter a number!"
            return 'room_2'
        elif int(ans) is 3:
            print "you chose %s - you win! You go onto the third room." % my_pokemon.choose(ans)
            return 'room_3'
        elif int(ans) > 4:
            print "\nDOES NOT COMPUTE"
            return 'room_2'
        else:
            print "You chose %s but it wasn't strong enough. You got defeated" % my_pokemon.choose(ans)
            return 'pokemon_centre'

#  Class for the third room
class Room3(object):

    def enter(self):
        print """
        \n
        You enter a dark and eery room which has a stange smell of incense in it.
        On the smooth purple stage you meet Agatha - the expert on Poison and Ghost-
        type Pokemon. She lets out her mighty Gengar, floating up and staring down at
        you with its sinister smile. Which Pokemon do you choose?
                \n\n
        """

        for no, name in my_pokemon.arsenal.items():
            print "%s : %s" % (no, name)

        ans = raw_input('\nI choose number: ')

        if not ans.isdigit():
            print" Please enter a number!"
            return 'room_3'
        elif int(ans) is 2:
            print "you chose %s - you win! You go onto the fourth room." % my_pokemon.choose(ans)
            return 'room_4'
        elif int(ans) > 4:
            print "\nDOES NOT COMPUTE"
            return 'room_3'
        else:
            print "You chose %s but it wasn't strong enough. You got defeated" % my_pokemon.choose(ans)
            return 'pokemon_centre'

# Class for the last room where a special combat takes place
class Room4(object):

    # special enter function because it initiates combat
    def enter(self):
        print """
        \n
        You have one Elite Four left to beat so you did great so far! Now you enter the
        final room which is the throne of the king of the Elite Four - Lance. He has the
        baddest team of elite dragon type Pokemon. He whips out the legenary Dragonite.
        You need your strongest Pokemon to beat him! Who do you choose?
                \n\n
        """

        for no, name in my_pokemon.arsenal.items():
            print "%s : %s" % (no, name)

        ans = raw_input('\nI choose number: ')

        if not ans.isdigit():
            print" Please enter a number!"
            return 'room_4'
        elif int(ans) is 4:
            print "you chose %s - the strongest Pokemon you have!." % my_pokemon.choose(ans)
            print "\n Your oponent Lance choose Dragonye, let the battle begin!!"
            # STARTING THE FINAL COMBAT
            final_combat = Combat()
            return final_combat.combat(my_pokemon, opp_pokemon)

        elif int(ans) > 4:
            print "\nDOES NOT COMPUTE"
            return 'room_4'
        else:
            print "You chose %s but it wasn't strong enough to beat Dragonite. You got defeated" % my_pokemon.choose(ans)
            return 'pokemon_centre'


# You come here if your Pokemon faints and the PokemonCentre will heal them
# But if you come here more than twice, the PokemonCentre won't heal you anymore
class PokemonCentre(object):

    def __init__(self):
        # creating an instance variable which will be created when creating
        # an object of this class
        self.trip_counter = 1

    def enter(self):


        print "You are at the Pokemon Centre...\n"
        # Pause for one second
        time.sleep(1)
        # Only allow 2 trips to the Pokemon Centre, 3 times means GAME OVER

        print "Nurse: Welcome to the Pokemon Centre, %s" % (player_object.name)
        print "We heal your Pokemon back to Perfect health"
        print "Shall we heal your Pokemon?\n"

        # Receive input from user
        ans = raw_input('(y/n)? ')

        time.sleep(2)

        if ans is 'y' and self.trip_counter < 3:
            # Remebering the number of trips to the pokemon centre
            self.trip_counter += 1

            # Rehealing the pokemon
            my_pokemon.hp = 500
            opp_pokemon.hp = 700

            print "\nNurse: Thank you %s! Your Pokemon are fighting fit!" % (player_object.name)
            print "We hope to see you again!\n\n"
            return 'room_1'
        elif ans is 'y' and not self.trip_counter < 3:
            print "\nNurse: %s! this seems to be your third time here." % (player_object.name)
            print "Your Pokemon look exhausted! They will take a few days to heal now..\n\n"
            print "Tip: Go back to watching Pokemon on TV and knowing more about them"
            print "before coming back...\n\n "
            time.sleep(2)
            print "GAME OVER\n\n"
            # You lost the game
            exit(1)
        elif ans is 'n':
            print "Your Pokemon must be healed before you want to go battle again"
            time.sleep(1)
            print "GAME OVER\n\n"
            exit(1)
        else:
            print "\nDOES NOT COMPUTE, please enter (y/n)"
            return 'pokemon_centre'

# Winning dialogue
class Finished(object):

    def enter(self):
        print "Congratulations %s! You have defeated the Elite four and have" % (player_object.name)
        print "become the Pokemon Master!!\n\n\n"
        exit(1)


# Contains all the different scenes and returns the classes based on the scene name
# The Engine then calls the method enter() in the particular class
class Map(object):

    scenes = {
        'player' : Player(player_object.name, player_object.town),
        'room_1' : Room1(),
        'room_2' : Room2(),
        'room_3' : Room3(),
        'room_4' : Room4(),
        'pokemon_centre' : PokemonCentre(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def opening_scene(self):
        return Map.scenes.get(self.start_scene)

    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)


# -------------------------------------------

# creating the Pokemon for battle
my_pokemon = Charizard('Charizard')
opp_pokemon = Dragonite('Dragonite')

# creating a pokemon centre
Restart = PokemonCentre()

# Running the engine

a_map = Map('player')
a_game = Engine()
a_game.play()
