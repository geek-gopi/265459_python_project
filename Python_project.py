import pytest

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

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    

    if operation == '+':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "+", num2, "=", add(num1, num2))
        output = str(add(num1,num2) )
        f = open("out1.txt", "w+")
        f.write(output)
        f.close()

#open and read the file after the appending:
        f = open("out1.txt", "r")
        print(f.read())

    elif operation == '-':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif operation == '*':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif operation == '/':
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Please type Y for YES or N for NO.
to continue
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()