print("================")
print("GRADE CHECKER")
print("================")




def get_grade(score):
    if 80<=score<=100:
     return"Grade: A"

    elif 70<=score<=79:
        return "Grade: B"

    elif 60<=score<=69:
        return "Grade: C"

    elif 50<=score<=59:
        return "Grade: D"

    elif 0<=score<50: 
        return "Grade: F"

    elif score<0 or score>100:
        print("Enter a valid score.")

def main():
    score = float(input("Enter student score(0-100):  "))
    result = get_grade(score)
    if result is None:
        print("Enter a valid score.")
    else:
        print(result)


    main()
