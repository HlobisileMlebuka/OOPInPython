import random
from random import randint
from collections import Counter

class Dice:
    def __init__(self):

        """assign random values to a list of five zeros"""

        self.dice = [0, 0, 0, 0, 0]
        self.roll(range(5))


    def roll(self, dice_roll_position):

        """ roll takes in a list that has an index of Dice one
        would like to roll. the zeros represents Dice that have not been rolled.
        A random number is generated for the chosen Dice """

        for index in dice_roll_position:
            self.dice[index] = randint(1, 6)
        

    def values(self):
        return self.dice[:]

    def Score(self):

        """ Score makes a count oprint(second.Score())f the occurances of each value in self.Dice and returns a dictionary
        it then loops over the values of the dictionary and makes conditional statements according to 
        the scoring system"""

        dice_count = Counter(self.dice)
        nonzero_dice_count = {k: dice_count[k] for k in dice_count.keys() - {0}}    

        list_of_counts = list(nonzero_dice_count.values())
        print(list_of_counts)

        if 3 in list_of_counts and 2 in list_of_counts:
            return "you have a full house: ", 12

        elif 3 in list_of_counts:
            return "You have a three of a kind: ", 8

        elif 4 in list_of_counts:
            return "You have a four of a kind: ", 15

        elif 5 in list_of_counts:
            return "You have a five of a kind: ", 30

        elif all(i == 1 for i in list_of_counts):
            return "You have a straight: ", 20

        else:
            return "Sorry, Your hand has not won you anything: ", 0


