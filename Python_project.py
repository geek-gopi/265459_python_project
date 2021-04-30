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

    


def calculate():
    operation = input('''
Choose Your Desired Operation by typing the symbol for it :
+ for addition
- for subtraction
* for multiplication
/ for division
hypo for hypothesis
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


    else:
        print('OOPS!!! INVALID user input, Please restart your program.')

    # Add again() function to calculate() function
        again()
        
def again():
    calc_again = input('''
    For repeating.....
    Type Y for YES or N for NO.
    
    ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Come back later.')
    else:
        again()
  #  else():
   # print('ds')
     






calculate()