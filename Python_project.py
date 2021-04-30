import pytest
import math

def add(x, y):
    return x + y
    

def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y    

def hypo(x,y):
    return math.hypot(x,y)

def sine():
    return math.sin(math.pi/6)  

def tan():
    return math.tan(math.pi/4) 

def cos():
    return math.cos(math.pi/6) 

def radian(d):
    return math.radians(d)



def calculate():
    operation = input('''
Choose Your Desired Operation by typing the symbol for it :
+ for addition
- for subtraction
* for multiplication
/ for division
hypo for hypothesis
sin for sin(pi/6)
tan for tan(pi/4)
cos for cos(pi/6)
rad to convert degree to radian
''')


    if operation == '+':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the Second number: '))
        print(num1, "+", num2, "=", add(num1, num2))
        output = str(add(num1,num2) )
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())

    elif operation == '-':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the Second number: '))
        print(num1, "-", num2, "=", subtract(num1, num2))
        
        output = str(subtract(num1,num2) )
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())





    elif operation == '*':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the Second number: '))
        print(num1, "*", num2, "=", multiply(num1, num2))
        
        output = str(multiply(num1,num2) )
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())




    elif operation == '/':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the Second number: '))
        print(num1, "/", num2, "=", divide(num1, num2))
        
        output = str(divide(num1,num2) )
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())
    

    elif operation == 'hypo':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the Second number: '))
        print("hypo",num1, num2, "=", hypo(num1, num2))
        
        output = str(hypo(num1,num2) )
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())
    

    
    elif operation == 'sin':
       # num1 = int(input('Enter the value in terms of pi: '))
       # print("sin",num1,"=", sine(num1))
        print ('The value of sin(pi/6): ', sine())
        
        output = str(sine())
       
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())
    
    elif operation == 'tan':
       # num1 = int(input('Enter the value in terms of pi: '))
       # print("sin",num1,"=", sine(num1))
        print ('The value of tan pi/4: ', tan())
        
        output = str(tan())
       
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())
    
    elif operation == 'cos':
       # num1 = int(input('Enter the value in terms of pi: '))
       # print("sin",num1,"=", sine(num1))
        print ('The value of cos pi/6: ', cos())
        
        output = str(cos())
       
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())

    elif operation == 'rad':
        num1 = int(input('Enter the value degree to be converted to radian: '))
       # print("sin",num1,"=", sine(num1))
        print("Degree",num1,"=", radian(num1),'radian')
        
        output = str(radian(num1))
       
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

        #open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())



    else:
        print('OOPS!!! INVALID user input, Please restart your program.')

    # Add again() function to calculate() function
      #  again()
        

     






calculate()