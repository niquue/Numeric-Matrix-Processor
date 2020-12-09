import numpy as np
# ---=== Based on the users input, call the correct arithmetic to apply to matrix ---===
def determine_process(choice):
    if choice == 1:
        add_matrices()
    elif choice == 2:
        multiply_constant()
    elif choice == 3:
        multiply_matrix()
    elif choice == 4:
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        user_in = int(input("Your choice: "))
        transpose(user_in)
    elif choice == 5:
        row, col = input("Enter matrix size: ").split()
        print("Enter matrix: ")
        matrix = get_nums(int(row), int(col))
        det = determinant(matrix)
        print("The result is: ")
        print(det)
    elif choice == 6:
        row, col = input("Enter matrix size: ").split()
        print("Enter matrix: ")
        matrix = get_nums(int(row), int(col))
        A = np.array(matrix)
        print("The result is: ")
        print_matrix(np.linalg.inv(A))
        print()
        # inv = inverse(matrix)
        # print(inv)
        # if inv == -1:
        #     print("This matrix doesn't have an inverse")
        #     print()
        # else:
        #     print_matrix(inv)
        #     print()


# ---=== Matrix method that adds two matrices together, and prints the result ---===
def add_matrices():
    # Get information of matrix one / row, col, and numerical info inside matrix.
    row_m_one, col_m_one = input("Enter size of first matrix: ").split()
    print("Enter first matrix:")
    m_one = get_nums(int(row_m_one), int(col_m_one))
    # Get information of matrix two / row, col, and numerical info inside matrix.
    row_m_two, col_m_two = input("Enter size of second matrix: ").split()
    print("Enter second matrix:")
    m_two = get_nums(int(row_m_two), int(col_m_two))

    matrix = []
    if len(m_one) != len(m_two):
        print("The operation cannot be performed.")
        print()
    else:
        for x in range(len(m_one)):
            m_add = []
            for y in range(len(m_one[x])):
                m_add.append(m_one[x][y] + m_two[x][y])
            matrix.append(m_add)
        print_matrix(matrix)
        print()


# ---=== Matrix method that multiplies a matrix by a constant (chosen by user) ---===
def multiply_constant():
    # Get information of the matrix / row, col, and numerical info inside matrix.
    row_m_one, col_m_one = input("Enter size of matrix: ").split()
    print("Enter matrix: ")
    matrix_one = get_nums(int(row_m_one), int(col_m_one))
    constant = input("Enter constant: ")
    # Check if the constant is an integer or a float for proper multiplication.
    if constant.isdigit():
        constant = int(constant)
    else:
        constant = float(constant)

    matrix = []
    for i in range(len(matrix_one)):
        m_mult = []
        for j in range(len(matrix_one[i])):
            m_mult.append(matrix_one[i][j] * constant)
        matrix.append(m_mult)
    print_matrix(matrix)
    print()


def multiply_matrix():
    # Get information of matrix one / row, col, and numerical info inside matrix.
    row_m_one, col_m_one = input("Enter size of first matrix: ").split()
    print("Enter first matrix:")
    m_one = get_nums(int(row_m_one), int(col_m_one))
    # Get information of matrix two / row, col, and numerical info inside matrix.
    row_m_two, col_m_two = input("Enter size of second matrix: ").split()
    print("Enter second matrix: ")
    m_two = get_nums(int(row_m_two), int(col_m_two))

    # Create matrix of [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ] or other dimension
    # Ex: (n x m) * (m x k) = n x k matrix
    result = [[0 for x in range(int(col_m_two))] for y in range(int(row_m_one))]

    if col_m_one != row_m_two:
        print("The operation cannot be performed.")
    else:
        for x in range(len(m_one)):
            for y in range(len(m_two[0])):
                for k in range(len(m_two)):
                    result[x][y] += m_one[x][k] * m_two[k][y]
    print_matrix(result)
    print()


def transpose(choice):
    row, col = input("Enter matrix size: ").split()
    print("Enter matrix: ")
    matrix = get_nums(int(row), int(col))
    result = [[0 for x in range(int(row))] for y in range(int(col))]
    # -- Main diagonal
    if choice == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]
    # -- Side diagonal
    elif choice == 2:
        a = 0
        b = 0
        for i in reversed(range(len(matrix))):
            for j in reversed(range(len(matrix[0]))):
                result[a][b] = matrix[j][i]
                b += 1
            a += 1
            b = 0
    # -- Vertical line
    elif choice == 3:
        a = 0
        for i in range(len(matrix)):
            for j in reversed(range(len(matrix[0]))):
                result[i][a] = matrix[i][j]
                a += 1
            a = 0
    # -- Horizontal line
    elif choice == 4:
        a = 0
        for i in reversed(range(len(matrix))):
            for j in range(len(matrix[0])):
                result[a][j] = matrix[i][j]
            a += 1
    print_matrix(result)
    print()


def determinant(p_matrix):

    if len(p_matrix) == len(p_matrix[0]):
        pass
    else:
        print("Invalid matrix input for determinant.")

    det = 0
    if len(p_matrix) < 2:
        return p_matrix[0][0]
    if len(p_matrix) == 2:
        return p_matrix[0][0] * p_matrix[1][1] - p_matrix[0][1] * p_matrix[1][0]
    for i in range(len(p_matrix)):
        det += ((-1) ** i) * p_matrix[0][i] * determinant(matrix_minor(p_matrix, 0, i))
    return det


def matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


def transpose_matrix(m):
    return list(map(list, zip(*m)))


def inverse(m):
    det = determinant(m)
    if det == 0:
        return -1
    if len(m) == 2:
        return [[m[1][1] / det, (-1 * m[0][1] / det)],
                [(-1 * m[1][0] / det), m[0][0] / det]]

    cofactors = []
    for row in range(len(m)):
        cofactor_row = []
        for col in range(len(m)):
            minor = matrix_minor(m, row, col)
            cofactor_row.append(((-1)**(row + col)) * determinant(minor))
        cofactors.append(cofactor_row)
    for row in range(len(cofactors)):
        for col in range(len(cofactors)):
            cofactors[row][col] = cofactors[row][col] / det
    return cofactors


def get_nums(row, col):
    matrix = []
    while True:
        for x in range(row):
            user_mat = input().split()
            # print(user_mat)
            for i in range(len(user_mat)):
                if user_mat[i].isdigit():
                    user_mat[i] = int(user_mat[i])
                else:
                    user_mat[i] = float(user_mat[i])
            #if user_mat[0].isdigit():
            #    user_mat = [int(n) for n in user_mat]
            #else:
            #    user_mat = [float(n) for n in user_mat]
            # user_mat = [int(nums) for nums in input().split()]
            if len(user_mat) > col:
                print("User entries did not match dimensions")
                break
            else:
                matrix.append(user_mat)
        break
    return matrix


# ---=== Basic procedure method that takes a matrix as an arg and outputs it to the screen ---===
def print_matrix(matrix):
    print("The result is: ")
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(matrix[x][y], end=' ')
        print()


# ---=== Start of the program that routes to matrix arithmetic based on choice ---===
print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
user_choice = int(input("Your choice: "))
while user_choice != 0:
    determine_process(user_choice)
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")
    user_choice = int(input("Your choice: "))






