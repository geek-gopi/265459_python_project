import pytest
from Python_project import add,subtract,divide,multiply



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

def test_sub():
   a=5
   b=2
   assert subtract(a,b) == 3
def test_sub1():
   a=5
   b=2
   assert subtract(a,b) == 1

def test_mul():
   a=3
   b=2
   assert multiply(a,b)==6

def test_mul1():
   a=3
   b=3
   assert multiply(a,b)==10

def test_div():
   a=4
   b=2
   assert divide(a,b)==2

def test_div1():
   a=4
   a=2
   assert divide(a,b)=1

def test_div3():
   a=10
   a=2
   assert divide(a,b)=5
   
def test_div4():
   a=10
   a=2
   assert divide(a,b)=7  
