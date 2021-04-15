import pytest
import random
import math
from lol import *



def test_add_basic():
    assert add(2,3) == 5
    assert add(99, 1) == 100
    assert add(15,15) == add(20,10)
    assert add(10000, 20000) == 30000
    assert add(100000000, 1) == 100000001  

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

def test_add_negative():
    assert add(-1,0) == -1
    assert add(-1,-3) == -4
    assert add(1,-3) == -2
    assert add(-100,3) == 97




def test_sub_basic():
    assert sub(1,3) == -2
    assert sub(17,5) == 12
    assert sub(5,5) == 0
    assert sub(10000005,5) == 10000000

def test_sub_zero():
    assert sub(1,0) == 1
    assert sub(0,0) == 0
    assert sub(0,10) == -10
    
def test_sub_inf():
    assert sub(8,float('inf')) == float('-inf')

def test_sub_negative():
    assert sub(-1,-5) == 4
    assert sub(-1,5) == -6
    assert sub(1,-15) == 16

def test_sub_decimal():
    assert sub(1.22222,1) == 0.22222
    assert sub(-1.22222,1) == -2.22222
    assert sub(1.22222,-1.22222) == 2.44444
    assert sub(1.22222,1.22222) == 0
    assert sub(0,0.123456789) == -0.123456789
    assert sub(0,0.1234567894) == -0.123456789   #zaokruhlenie na dol na deviatom mieste
    assert sub(0,0.1234567815) == -0.123456782   #zaokruhlenie na hor na deviatom mieste



def test_mul_basic():
    assert mul(1,5) == 5
    assert mul(34,7) == 238
    assert mul(12345,1) == 12345
    assert mul(12345,45678) == 563894910
    assert mul(3,6) == mul(6,3)

def test_mul_zero():
    assert mul(0,9) == 0
    assert mul(71,0) == 0
    assert mul(0,0) == 0
    assert mul(0,-16) == 0
    assert mul(-97,0) == 0
    assert mul(-37.2332,0) == 0
    assert mul(0,-545) == 0

def test_mul_negative():
    assert mul(-17,-31) == 527
    assert mul(4,-19) == -76
    assert mul(-68,26) == -1768

def test_mul_decimal():
    assert mul(23.6556,456) == 10786.9536
    assert mul(739,456.23) == 337153.97
    assert mul(687.592,783.68) == 538852.09856
    assert mul(6.123456,3.68123) == 22.541849931    #zaokruhlene na hor 22,541849930 88
    assert mul(3.7526982, 8.462) == 31,755332168    #zaokruhlenie na dol 31,755332168 4



def test_div_basic():
    assert div(4,2) == 1
    assert div(3,9) == 0.333333333
    assert div (123135498,1) == 123135498
    assert div (123135498,10) == 12313549.8

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(45685,0)
        div(0,0)
        div(000.00,0000)

def test_div_negative():
    assert div(81,-9) == -9
    assert div(-125,25) == -5
    assert div(-10000,-10) == 1000

def test_div_decimal():
    assert div(125,0.5) == 250
    assert div(444.44,2) == 222,22
    assert div(259.568,9) == 28.840888889   # 8 zaokrulenie na hor
    assert div(3529456.45,128.175) == 27536.231324361 # 2 zaokruhlenie na dol



def test_fact_basic():
    assert fact(1) == 1
    assert fact(7) == 5040
    assert fact(13) == 6227020800
    

def test_fact_zero():
    assert fact(0) == 1

def test_fact_negative():
    with pytest.raises(TypeError):
        fact(-1)
        fact(-8)

def test_fact_decimal():
    with pytest.raises(TypeError):
        fact(1.7)
        fact(0.8)




def test_exponent_basic():
    assert exponent(1,7) == 1
    assert exponent(3,7) == 2187
    assert exponent(15,7) == 170859375

def test_exponent_zero():
    assert exponent(9,0) == 1
    assert exponent(98797,0) == 1
    assert math.isnan(exponent(0,0))