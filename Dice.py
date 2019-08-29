import random
from random import randint

class Dice:

    def __init__(self):

        """assign random Values to a list of five zeros"""

        self.Dice = [0,0,0,0,0]
        self.Roll(range(5))
   
    def Roll(self, Dice_Roll_Position):
        """ Roll takes in a list that has an index of Dice one
        would like to roll. the zeros represents Dice that have not been rolled.
        A random number is generated for the chosen Dice """
        import random 
        from random import randint 
        self.Dice = [0,0,0,0,0]
        for index in Dice_Roll_Position:
            
            self.Dice = randint(1,6)
        return self.Dice
    
    def Values(self):
        return self.Dice[:]
    
    def Score(self):
        from collections import Counter

        """ Score makes a count of the occurances of each value in self.Dice and returns a dictionary
        it then loops over the values of the dictionary and makes conditional statements according to 
        the scoring system"""

        Dice_Count = Counter(self.Dice)
        NonZero_Dice_Count = {k: Dice_Count[k] for k in Dice_Count.keys() - {0}}
        
        for value in list(NonZero_Dice_Count.values()):
            
            if value == 2 and value == 3:
                return "you have a full house: ", 12
            
            elif value==3:
                return "You have a three of a kind: ", 8
                    
            elif value == 4:
                return "You have a four of a kind: ", 15
            
            elif  value == 5:
                return "You have a five of a kind: ", 30

            elif value == 1:
                return "You have a straight: ", 20

            else:
                return "Sorry, Your hand has not won you anything: ", 0