# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
def add(first_number:int , second_number:int):
    return  first_number + second_number

def subtract(first_number:int , second_number:int):
    return   first_number-second_number

def multiply(first_number:int , second_number:int):
    return  first_number*second_number

def divide(first_number:int , second_number:int):
    return  round(first_number/second_number, 2)


def mod(first_number:int , second_number:int):
    return  first_number%second_number


def exponent(first_number:int , second_number:int):
    return   first_number**second_number




while True:
    print("=======================")

    print("SIMPLE CALCULATOR")

    print("=======================")

    print("1." + "Addition")
    print("2." + "Subtraction")
    print("3." + "Multiplication")
    print("4." + "Division")
    print("5." + "Modulus")
    print("6." + "Exponentiation")
    print("7." + "Quit")


    operation_of_user = input("Select an operation from (1-7): ")

    if operation_of_user == 7:
        print("Calculation halted")
        break
    else:
        first_number = int(input("Enter first number: "))

        second_number = int(input("Enter second number: "))
    

    if operation_of_user == str(1):
        print(add(first_number, second_number))

    elif operation_of_user == str(2):
        print(subtract(first_number, second_number))

    elif operation_of_user == str(3):
        print(multiply(first_number,second_number))

    elif operation_of_user == str(4):
        if second_number == 0:
            print("Math error")
        else:
            print(divide(first_number,second_number))

    elif operation_of_user == str(5):
        print(mod(first_number,second_number))

    elif operation_of_user == str(6):
        print(exponent(first_number, second_number))

