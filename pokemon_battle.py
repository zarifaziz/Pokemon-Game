# Author: Zarif Aziz


from random import *
import time
import math

class Combat(object):

    def combat(self, user, opp):

        # Keep fighting until someone is victorious
        while True:
            # Print out the status of the battle
            print "\n", "-" * 20, "\n"
            print "%s's HP : %d" % (user.name, user.hp)
            print "%s's HP : %d" % (opp.name, opp.hp)
            print "\nWhat will %s do?\n" % (user.name)
            print '1) attack - Attack the enemy'
            print '2) defend - Defend from being attacked'

            user_choice = raw_input("\n\nattack/defend? > ")

            # opponent's choice is random
            opp_choice = randint(2,3)

            if user_choice == 'attack':

                time.sleep(0.5)
                # Display all the moves available to attack with
                print "Choose your move from the following:\n"
                for movez, no in user.moves.items():
                    print "%s \n" % movez

                final_choice = raw_input("> ")

                # Check whether our entry is valid
                if final_choice in user.moves.keys():

                    # opponent has a 1/2 chance of attacking
                    if opp_choice is not 3:
                        # Attack the oponent with the chosen move
                        user.attack(opp, final_choice)
                        # opponent attacks user with a random attack
                        opp.attack(user, choice(['Hyper Beam', 'Inferno', 'Slash', 'Dragon Rush']))
                    else:
                        opp.defend()
                        # Attack the oponent with the chosen move
                        user.attack(opp, final_choice)
                # User input should be valid before a valid attack sequence takes place
                else:
                    time.sleep(0.5)
                    print "\nError, that attack does not exist! Check the spelling"


            elif user_choice == 'defend':

                # User defends
                user.defend()

                # opponent has a 2/3 chance of attacking
                if opp_choice is not 3:
                    # opponent attacks user with a random attack
                    opp.attack(user, choice(['Hyper Beam', 'Inferno', 'Slash', 'Dragon Rush']))
                else:
                    opp.defend()

            else:
                print "DOES NOT COMPUTE"

            # Checking if anyone has died
            if user.hp <= 0:
                time.sleep(0.5)
                print "Oh no! You're %s has fainted !" % user.name
                return 'pokemon_centre'
            if opp.hp <= 0:
                time.sleep(0.5)
                print "%s has fainted !" % opp.name
                return 'finished'
