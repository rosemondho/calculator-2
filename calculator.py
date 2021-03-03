"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("Enter your equation: ")
    tokens = user_input.split(" ")

    if tokens[0] is "q":
        print("You will exit.")
        break

    elif len(tokens) < 2:
        print("More input is needed")
        continue

    operator = tokens[0]
    num1 = tokens[1]        
        
    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("Enter real numbers")
        continue

    elif operator == "+":
        result = add(float(num1), float(num2))
    
    elif operator == "-":
        result = subtract(float(num1), float(num2))
    
    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), result(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))
    
    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))


    print(result)
# takes user input --> puts user input into list
# verify that user is inputting 
# if they enter < 2, let them know that it's not enough inputs
# check to see that num1 and num2 are digits 
# check to make sure that it is not a q

# Rosemond: navigate the section that takes in user input
# Kioshi: navigate the section that completes operation