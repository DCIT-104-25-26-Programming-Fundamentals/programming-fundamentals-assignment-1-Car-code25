number = int(input("Enter number: "))

print("===========================")

print("MULTIPLICATION TIME TABLE") 

print("===========================")


nums = [1,2,3,4,5,6,7,8,9,10,11,12]

if number<0:
    print("Error")
else:
    for i in nums:
        print(f"{number}*{i} = {i*number}")