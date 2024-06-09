import numpy as np

def reduce_matrix(matrix: np.ndarray, starting_row: int, column_index: int):
    column = (matrix[:, column_index])
    row_index = starting_row
    while row_index < column.shape[0] and column[row_index] == 0: # Find the first non-zero row in the column
        row_index += 1
        if row_index == column.shape[0]:
            reduce_matrix(matrix, starting_row, column_index + 1) # No reduction is possible in this column
            return

    matrix[[row_index, starting_row]] = matrix[[starting_row, row_index]] # Swap the non-zero row with the starting row

    row = matrix[starting_row]
    if row[column_index] != 1:
        row //= row[column_index] # If the column's value in the row is not 1 make it 1

    for row_i in matrix[starting_row + 1:]: # Reduce the rest of the rows
        if (row_i[column_index] != 0):
            coefficient = row_i[column_index]
            row_i -= coefficient * row

    for row_i in matrix[:starting_row]:
        if (row_i[column_index] != 0):
            coefficient = row_i[column_index]
            row_i -= coefficient * row

    if (starting_row == matrix.shape[0] - 1):
        return
    reduce_matrix(matrix, starting_row + 1, column_index + 1)

if __name__ == "__main__":
    input_matrix = np.array(
        [
            #A  B  C  D  E  F  G  H  I  J  K  constants
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], # 1
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], # 2
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1], # 3
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], # 4
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1], # 5
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], # 6
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], # 7
        ]
    )
    output_matrix = np.array(
        [
            #A  B  C  D  E  F  G  H  I  J  K  constants
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0], # 1
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], # 2
            [0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0], # 3
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 4
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], # 5
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # 6
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], # 7
        ]
    )
    reduce_matrix(input_matrix, 0, 0)
    print(input_matrix)
    print()
    print(output_matrix)