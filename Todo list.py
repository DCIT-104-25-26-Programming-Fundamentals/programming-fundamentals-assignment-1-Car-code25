Tasks = []

number_of_tasks = int(input("How many tasks: "))

for task in range(number_of_tasks):
     value = input(f" add {task+1}: ")
Tasks.append((value))


print(Tasks) and print("Your task has been added")


