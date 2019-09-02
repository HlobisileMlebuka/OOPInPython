import random
from random import randint
from collections import Counter

from Dice import *
from poker_game_methods import *

class Interface:
    """ this class has methods that prompt the user to act on the option of playing more rounds or 
    terminating and also gives feedback on what the game's status is, regarding scores and winnings"""

    def __init__(self):
        print("please play")

    def current_money_value(self, amount):
        print("you currently have: ", amount)

    def dice_set_values(self, values):
        print("your hand is: ", values)

    def continue_play(self):
        response = input("Do you want to Play? ")
        return response[0] in "yY"

    def terminate(self):
        print("Good Bye")

    def show_results(self, message, score):
        print(f"{message} you win {score}")

    def choose_dice(self):
        numbers = input("enter list index of which dice to roll.")
        number_list = [int(x) for x in input()]
        return number_list






if __name__ == "__main__":
    
    user = Interface()
    app = PokerGame(user)
    app.game_termination()

