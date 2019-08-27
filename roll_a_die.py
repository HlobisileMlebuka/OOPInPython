


class MsDie:

    """ class function that allows one to roll a die with a preselected number of sides.
    From the Roll Method, the die outputs a random number.
    From the SetValue Method, the die output is a preselected number.
    the GetValue method returns the current value of the die, depending on the instance made."""

    def __init__(self, value, number_of_sides):
        
        self.value = value
        self.number_of_sides = number_of_sides

    def roll(self):                                                     #returns a random number
        import random
        self.value = random.randrange(1,(self.number_of_sides+1))
        return self.value

    def SetValue(self):                                                 #returns a set number
        
        if self.value not in range(1,7):
            raise Exception('please select a value in range (1:6), inclusive')
        else:
            return self.value

    def GetValue(self):                                                 #returns the current value of the die
        return self.value

    

if __name__ == '__main__':
    pass
  
