# Christiana Huss
# CIS 129
# Module 7 Assignment
# 06/30/2024

# Lab 7-3 The Dice Game
# add libraries needed
import random
import re

#this function gets the players names
def input_names(one, two):
    one = input("Please enter player 1s name: ") # first player to input their name 
    two = input("Please enter player 2's name: ") # second player to input their name 
    print(f"Great! Welcome, {one} and {two}!") # welcome message to players 
    return one, two # return both names 

#this function will get the random values
def roll_dice(num1, num2, p1, p2, winner):
    num1 = random.randint(1, 6) # generate random number between 1 and 6 inclusive for player 1
    num2 = random.randint(1, 6) # generate random number between 1 and 6 inclusive for player 2 

    print(f"{p1} rolled a {num1}!") # display what player 1 rolled 
    print(f"{p2} rolled a {num2}!") # display what player 2 rolled 

    if num1 > num2:
        winner = p1 # assign p1 is winner if their roll is greater than p2's roll
    elif num2 > num1:
        winner = p2 # assign p2 to winner if their roll is greater than p1's roll
    else:
        winner = "TIE!" # otherwise it is a tie 
    return winner
        

#this function displays the winner
def display_info(winner):
    if winner == "TIE!":
        print("It's a Tie!") # message to users if it's a tie 
    else:
        print(f"{winner} won!") # message to users if there is a winner 

# the main function
def main():
    print()

    # initialize variables
    end_program = 'no' # variable for while loop 
    player_one = 'NO NAME' # initialize player_one name as a string 
    player_two = 'NO NAME' # initialize player_two name as a string 

    # call to inputNames
    player_one, player_two = input_names(player_one, player_two)

    # while loop to run program again
    while end_program == 'no':

        # populate variables
        winner_name = 'NO NAME'
        p1number = 0 # initialize p1number 
        p2number = 0 # initialize p2number 

        # call to rollDice
        winner_name = roll_dice(p1number, p2number, player_one, player_two, winner_name) # generate winner with roll_dice function 

        # call to displayInfo
        display_info(winner_name) 

        end_program = input('Do you want to end the program? (yes/no): ') # prompt user to continue or end the program 
        end_program = re.sub(r'[^a-zA-Z0-9]','', end_program) # remove special characters from input
        end_program = end_program.lower() # convert elements of phrase to lowercase 
        end_program = end_program.replace(" ", "") # remove white spaces from user input 

# calls main
main()
