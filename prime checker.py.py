def prime_checker (number:int):
    for nums in range (2,number):
        if number%nums ==0:
            print("The number is not prime number")
            break

    else:
        print("The number is  prime")




print(prime_checker(8))


