import addition
import subtraction
import division
import multiplication

print("What would you like to do?")
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")

userNum = input("Enter Choice : ")
if userNum in ('1', '2', '3', '4'):
    numOne = input("Select first number: ")
    numTwo = input("Select second number: ")
    if userNum == '1':
        print(addition.add(numOne, numTwo))
    elif userNum == '2':
        print(subtraction.minus(numOne, numTwo))
    elif userNum == '3':
        print(multiplication.multiply(numOne, numTwo))
    elif userNum == '4':
        print(division.divide(numOne, numTwo))
    else:
        print("Error invalid input")