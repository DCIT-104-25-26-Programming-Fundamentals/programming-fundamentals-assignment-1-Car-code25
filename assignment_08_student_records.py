# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# =============================================================================

students = []


def add_student():
    name = input("Student name: ")
    student_id = int(input("Student ID: "))

    number_of_scores = int(input("How many scores? "))

    scores = []

    for i in range(number_of_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)

    print(f'Student "{name}" added successfully.')


def display_all_students():
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("-" * 60)
    print(f"{'Name':<20}{'ID':<12}{'Scores':<20}{'Average':<10}")
    print("-" * 60)

    for student in students:
        average = sum(student["scores"]) / len(student["scores"])

        scores = ", ".join(str(score) for score in student["scores"])

        print(
            f"{student['name']:<20}"
            f"{student['id']:<12}"
            f"{scores:<20}"
            f"{average:.2f}"
        )

    print("-" * 60)


def calculate_average():
    student_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == student_id:

            average = sum(student["scores"]) / len(student["scores"])

            print(
                f"{student['name']}'s average score: "
                f"{average:.2f}"
            )

            return

    print("Student ID not found.")


def main():
    while True:
        print()
        print("==============================")
        print("   STUDENT RECORD SYSTEM MENU")
        print("==============================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_all_students()

        elif choice == "3":
            calculate_average()

        elif choice == "4":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")


main()
