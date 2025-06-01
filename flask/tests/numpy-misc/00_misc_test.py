

import numpy as np




#convert row echelon form to reduced row echelon form
def convert_to_rref(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    current_row = 0

    for j in range(num_cols):
        if current_row >= num_rows:
            break

        pivot_element = matrix[current_row][j]

        if pivot_element != 0:
            # Normalize the row
            matrix[current_row] = [x / pivot_element for x in matrix[current_row]]

            # Make all elements below the pivot equal to zero
            for i in range(current_row + 1, num_rows):
                multiplier = matrix[i][j]
                matrix[i] = [matrix[i][k] - multiplier * matrix[current_row][k] for k in range(num_cols)]

            current_row += 1

    return matrix

# Example usage
# matrix = [[2, 1, -1], [-3, -1, 2], [1, 0.5, -0.5]]
# rref_matrix = convert_to_rref(matrix)
# print(rref_matrix)


#function that returns the row echelon form of a matrix
# init with continue qwen2.5-coder:1.5b-base
def row_echelon_form(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    current_row = 0

    for j in range(num_cols):
        if current_row >= num_rows:
            break

        pivot_row = current_row
        while pivot_row < num_rows and matrix[pivot_row][j] == 0:
            pivot_row += 1

        if pivot_row == num_rows:
            continue

        # Swap rows to get the leading entry as the first entry in the row.
        matrix[current_row], matrix[pivot_row] = matrix[pivot_row], matrix[current_row]

        # Use elementary row operations to make all other entries in this column 0.
        for i in range(num_rows):
            if i == current_row:
                continue
            factor = matrix[i][j] / matrix[current_row][j]
            for k in range(j, num_cols):
                matrix[i][k] -= factor * matrix[current_row][k]

        current_row += 1

    return matrix


#https://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u
#https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
def test_matrix():
    #PendingDeprecationWarning: the matrix subclass is not the recommended way to represent matrices or deal with linear algebra 
    # (see https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html). Please adjust your code to use regular ndarray.
    # a = np.asmatrix('4 3; 2 1')
    # b = np.asmatrix('1 2; 3 4')

    a = np.array([[4,3],
                  [2,1]])
    b = np.array([[1,2],
                  [3,4]])

    print(a)
    # [[4 3]
    #  [2 1]]
    print(b)
    # [[1 2]
    #  [3 4]]
    print(np.matmul(a,b))
    # [[13 20]
    #  [ 5  8]]


def test_rref():

    test_array = [
        [1,1,0],
        [0,1,0]
    ]

    test_array2 = [
        [.25,   1,  -1,  0],
        [1,     4   ,2,     12],
        [2,     -3,- 1,   3],
    ]

    print(row_echelon_form(test_array))
    print(row_echelon_form(test_array2))

    print(
        convert_to_rref(row_echelon_form(test_array2))
        )

    print("\n\n")

    print("hello")
    print("hello 2")