import pytest
from Python_project import add,subtract,divide,multiply,hypo,sine,tan,cos,radian



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

def test_mul2():
   a=3
   b=20
   assert multiply(a,b)==60

def test_div():
   a=4
   b=2
   assert divide(a,b)==2

def test_div1():
   a=10
   b=2
   assert divide(a,b)==5

def test_div3():
   a=10
   b=2
   assert divide(a,b)==5
   
def test_div4():
   a=10
   b=2
   assert divide(a,b)==7 

def test_hypo():
   a=3
   b=4
   assert hypo(a,b)==5.0 

def test_hypo1():
   a=3
   b=4
   assert hypo(a,b)==10


def test_hypo2():
   a=10
   b=2
   assert hypo(a,b)==4

def test_sin():
   assert sine()==34

def test_tan():
   assert tan()==0.9999999999999999

def test_cos():
   assert cos()== 0.8660254037844387

def test_cos1():
   assert cos()== 1

def test_rad():
   d=30
   assert radian(d)==0.5235987755982988

def test_rad1():
   d=30
   assert radian(d)==12






