import pytest
import random
import math
from lol import *



def test_add_basic():
    assert add(2,3) == 5
    assert add(99, 1) == 100
    assert add(15,15) == add(20,10)
    assert add(10000, 20000) == 30000
    
    
def test_add_inf():
    assert add(5,float('inf')) == float('inf')
    assert add(float('inf'),float('inf')) == float('inf')
    assert math.isnan(add(float('-inf'), float('inf')))


def test_add_zero():
    assert add(121, 0) == 121
    assert add(0,19) == 19
    assert add(0,0) == 0
    assert add(0,8) == add(8,0)

def test_add_errors():
    with pytest.raises(TypeError):
        add(8, 'a')
        add('a', 8)
        add('a', 'a')
