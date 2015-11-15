# Rock-paper-scissors-lizard-Spock template
## Credit for this exercise goes to Rice University 
## Fundamentals of Computing Specialization Authors
## Joe Warren and Scott Rixner
## for this exercise and more see www.coursera.org/fundamentalscomputing2

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
import math

def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    # Also if you wrote a doc string to say what this does then that'd be cool...
    pass


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    pass
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print "\n"
    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()

    # print out the message for computer's choice


    # use if/elif/else to determine winner, print winner message


    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


