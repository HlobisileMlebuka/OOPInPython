import random
from random import randint
from collections import Counter

from Dice import Dice
from pokergame import Interface

class PokerGame:

    """The player starts with \$100.
    Each round costs \$10 to play. This amount is subtracted from the player’s money at the start of the round.
    The player initially rolls a completely random hand (i.e. all the five dice are rolled).
    The player gets two chances to enhance the hand by re-rolling some or all of the dice."""

    def __init__(self, Interface):
        self.Dice = Dice()
        self.money = 100
        self.Interface = Interface

    def game_termination(self):
        
    # game terminates if player chooses to terminate or has more than $10
        while (
            self.money >= 10 and self.Interface.continue_play()
        ):  
            self.play_poker()
        self.Interface.terminate()

    def play_poker(self):

    # each round costs $10 dollars    
        self.money = self.money - 10  
        self.Interface.current_money_value(self.money)
        self.rolls()
        result, score = self.Dice.Score()
        self.Interface.show_results(result, score)
        self.money = self.money + score
        self.Interface.current_money_value(self.money)

    def rolls(self):
        
        self.Dice.roll(range(5))
        roll = 1
        self.Interface.dice_set_values(self.Dice.values())
        dice_to_be_rolled = self.Interface.choose_dice()
        while roll < 3 and dice_to_be_rolled != []:
            self.Dice.roll(dice_to_be_rolled)
            roll = roll + 1
            self.Interface.dice_set_values(self.Dice.values())
            if roll < 3:
                dice_to_be_rolled = self.Interface.choose_dice()

