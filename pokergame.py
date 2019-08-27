
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

            elif ( value == 1]):
                return "You have a straight: ", 20

            else:
                return "Sorry, Your hand has not won you anything: ", 0

class PokerGame:
    def __init__(self, Interface):
        self.Dice = Dice()
        self.money = 100
        self.Interface = Interface
           
    def Game_Termination(self):
        while self.money >= 10 and self.Interface.ContinuePlay():
            self.Play_Poker()            
        self.Interface.Terminate()

    def Play_Poker(self):
        self.money -= 10
        self.Interface.CurrentMoneyValue(self.money)
        self.Rolls()
        result, score = self.Dice.Score()
        self.Interface.ShowResults(result, Score())
        self.money = self.money + score
        self.Interface.CurrentMoneyValue(self.money)        

    def Rolls(self):
        self.Dice.Roll([0,0,0,0,0])
        roll = 1
        self.Interface.DiceSetValues(self.Dice.Values())
        Dice_To_Be_Rolled = self.Interface.ChooseDice()
        while roll < 3 and Dice_To_Be_Rolled != []:
            self.Dice.Roll(Dice_To_Be_Rolled)
            roll = roll + 1
            self.Interface.DiceSetValues(self.Dice.Values())
            if roll < 3:
                Dice_To_Be_Rolled = self.Interface.ChooseDice()

class Interface:

    def __init__(self):
        print("please play")

    def CurrentMoneyValue(self, amount):
        print("you currently have: ", amount)

    def DiceSetValues(self, Values):
        print("your hand is valued at: ", Values)

    def ContinuePlay(self):
        response = input("Do you want to Play? " )
        return response[0] in 'yY'
    
    def Terminate(self):
        print("Good Bye")

    def ShowResults(self, message, score):
        print(f"{message}. you win {score}")

    def ChooseDice(self):
        return input("enter list index of which dice to roll in square brackets[]")



if __name__ == "__main__":
    # player1 = Dice()
    # print(player1.Values())
    # print(player1.Score())
    # print(player1.Roll([1,3]))
    # print(player1.Values())
    # print(player1.Score())
    user = Interface()
    app = PokerGame(user)
    app.Game_Termination()

         

    



    



   

    


