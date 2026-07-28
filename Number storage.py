nums = int(input("How many numbers: "))

arr = []

for i in range(nums):
    value = input(f"Enter number {i+1}: ")
    arr.append(int(value))


print("Sum:" + str(sum(arr)))
print("Average:" + str(sum(arr)/len(arr)))
print("Maximum:" + str(max(arr)))
print("Minimum:" + str(min(arr)))














