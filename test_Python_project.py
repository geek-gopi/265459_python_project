import pytest
from Python_project import add,subtract,divide,multiply

'''def calculate():
    a = '+'
    assert Python_project.calculate(a) == '+' '''

def test_add():
   a=2
   b=9
   assert add(a,b) == 6


def test_add2():
   a=3
   b=2
   assert add(a,b) == 5

def test_add3():
   a=5
   b=2
   assert add(a,b) == 7

'''def testsquare():
   num = 7
   assert 7*7 == 40   '''