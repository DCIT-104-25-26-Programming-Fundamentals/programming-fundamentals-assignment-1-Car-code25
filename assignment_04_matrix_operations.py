# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
 ============================================================================= 
def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} numbers.")

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        transpose.append(new_row)

    return transpose


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = []

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            total = 0

            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


def main():
    while True:
        print("\n==============================")
        print("MATRIX OPERATIONS")
        print("==============================")
        print("1. Transpose Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            print("Enter the matrix:")
            matrix = read_matrix(rows, cols)

            print("\nOriginal Matrix:")
            print_matrix(matrix)

            print("\nTransposed Matrix:")
            print_matrix(transpose_matrix(matrix))

        elif choice == "2":
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            print("Enter Matrix A:")
            matrix1 = read_matrix(rows, cols)

            print("Enter Matrix B:")
            matrix2 = read_matrix(rows, cols)

            print("\nSum of Matrices:")
            print_matrix(add_matrices(matrix1, matrix2))

        elif choice == "3":
            rows_a = int(input("Enter rows for Matrix A: "))
            cols_a = int(input("Enter columns for Matrix A: "))

            print("Enter Matrix A:")
            matrix1 = read_matrix(rows_a, cols_a)

            rows_b = int(input("Enter rows for Matrix B: "))
            cols_b = int(input("Enter columns for Matrix B: "))

            if cols_a != rows_b:
                print("Matrix multiplication is not possible.")
                continue

            print("Enter Matrix B:")
            matrix2 = read_matrix(rows_b, cols_b)

            print("\nProduct of Matrices:")
            print_matrix(multiply_matrices(matrix1, matrix2))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose between 1 and 4.")


main()
