import pytest
from .roll_a_die import *

import random
def test_innit_():
    
    MsDieInstance = MsDie(3,6)

    assert MsDieInstance.value == 3
    assert MsDieInstance.number_of_sides == 6

def test_Set_ValueRaisesException():
    
    with pytest.raises(Exception):
        assert MsDieInstance.SetValue() == MsDie(12,6)
        assert MsDieInstance.SetValue() == MsDie(0,6)
        
def test_Set_Value():
    MsDieInstance = MsDie(1,6)
    assert MsDieInstance.SetValue() == 1

def test_GetValue():

    MsDieInstance = MsDie(1,6)
    assert MsDieInstance.SetValue() == MsDieInstance.GetValue()
    assert MsDieInstance.roll() == MsDieInstance.GetValue()


    


    