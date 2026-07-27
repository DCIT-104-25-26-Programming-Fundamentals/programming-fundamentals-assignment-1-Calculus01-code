# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def input_matrix(rows, cols, matrix_name="Matrix"):
    print(f"\nEnter elements for {matrix_name} ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i+1}: ").split()
            if len(row_input) == cols:
                matrix.append([int(x) for x in row_input])
                break
            else:
                print(f"Error: Please enter exactly {cols} values.")
    return matrix
def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{val:>5}" for val in row))

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) 

    result=[[ 0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
      for j in range(cols):
        result[j][i] = matrix[i][j]
    return result
def add_matrices(matrix_a, matrix_b): 
    rows=len(matrix_a)
    cols=len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def main():
    print("=== Matrix Operations Program ===")
    print("\n--- Part A: Transpose a Matrix ---")
    m=int(input("Enter number of rows: "))
    n=int(input("Enter number of columns: "))
    matrix_a = input_matrix(m, n, "Original Matrix")

    print_matrix(matrix_a, "Original Matrix")
    transposed = transpose_matrix(matrix_a)
    print_matrix(transposed, "Transposed Matrix")

    print("\n--- Part B: Add Two Matrices ---")
    print(f"Creating two matrices of size {m} x {n} for addition.")
    mat_b1 = input_matrix(m, n, "Matrix 1")
    mat_b2 = input_matrix(m, n, "Matrix 2")

    sum_result = add_matrices(mat_b1, mat_b2)
    print_matrix(mat_b1, "Matrix 1:")
    print_matrix(mat_b2, "Matrix 2:")
    print_matrix(sum_result, "Sum of Matrices")

    print("\n--- Part C: Multiply Two Matrices ---")
    mat_c_A =input_matrix(m,n,"Matrix A")

    p=int(input(f"Enter number of columns for Matrix B: "))
    mat_c_B= input_matrix(n,p,"Matrix B")

    product_result = multiply_matrices(mat_c_A, mat_c_B)
    print_matrix(mat_c_A, "Matrix A:")
    print_matrix(mat_c_B, "Matrix B:")
    print_matrix(product_result, "Product of Matrices")

if __name__ == "__main__":
    main()