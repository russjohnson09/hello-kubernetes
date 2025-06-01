

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


def test():

    test_array = [
        [1,1,0],
        [0,1,0]
    ]

    print(row_echelon_form(test_array))

    print("\n\n")

    print("hello")
    print("hello 2")