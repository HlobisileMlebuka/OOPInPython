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

        """ Score makes a count of the occurances of each value in self.Dice and returns a dictionary
        it then loops over the values of the dictionary and makes conditional statements according to 
        the scoring system"""

        dice_count = Counter(self.Dice)
        nonzero_dice_count = {k: dice_count[k] for k in dice_count.keys() - {0}}

        for value in list(nonzero_dice_count.values()):

            if value == 2 and value == 3:
                return "you have a full house: ", 12

            elif value == 3:
                return "You have a three of a kind: ", 8

            elif value == 4:
                return "You have a four of a kind: ", 15

            elif value == 5:
                return "You have a five of a kind: ", 30

            elif value == 1:
                return "You have a straight: ", 20

            else:
                return "Sorry, Your hand has not won you anything: ", 0


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

        while (
            self.money >= 10 and self.Interface.continue_play()
        ):  # game terminates if player chooses to terminate or has more than $10
            self.play_poker()
        self.Interface.terminate()

    def play_poker(self):
        self.money = self.money - 10  # each round costs $10 dollars
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
        print(f"{message}. you win {score}")

    def choose_dice(self):
        numbers = input("enter list index of which dice to roll.")
        number_list = [int(x) for x in input()]
        return number_list


if __name__ == "__main__":
    # player1 = Dice()
    # print(player1.values())
    # print(player1.Score())
    # print(player1.roll([1,3]))
    # print(player1.values())
    # print(player1.Score())
    user = Interface()
    app = PokerGame(user)
    app.game_termination()

