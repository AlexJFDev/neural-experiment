import numpy as np
import field
from minefield import Minefield

def create_field_matrix(minefield: Minefield) -> np.ndarray:
    coord_to_col = {}
    col_to_coord = {}
    matrix_width = 0 # Width not including constant column (width - 1)
    constants = [] # will become last column of matrix
    rows = []
    field = minefield._get_field()
    height, width = field.shape
    for i in range(height):
        for j in range(width):
            constant = field[i, j]
            if constant > 0:
                coords = get_2d_neighbors(i, j, height, width)
                cols = []
                for coord in coords:
                    x, y = coord
                    value = field[x, y] # -1 is flag, -2 is unknown
                    if (value == -1):
                        constant -= 1 # If there is a flag, the tile has one fewer unknown mines
                    elif (value == -2):
                        col = coord_to_col.get(coord)
                        if col is None:
                            col = matrix_width
                            matrix_width += 1
                            coord_to_col[coord] = col
                            col_to_coord[col] = coord
                        cols.append(col)
                    if constant == 0: break
                if constant == 0: continue
                constants.append([constant])
                rows.append(cols)
    field_matrix = np.zeros((len(constants), matrix_width), dtype=int)
    for row_index in range(len(rows)):
        row = rows[row_index]
        field_matrix[row_index][row] = 1
    field_matrix = np.concatenate([field_matrix, constants], axis=1)
    print(col_to_coord)
    return field_matrix

def get_neighbors(x, max):
    if (x == 0): return {x, x + 1}
    if (x == max - 1): return {x - 1, x}
    return {x - 1, x, x + 1}

def get_2d_neighbors(x, y, x_max, y_max):
    neighbors = {
        (row, col)
        for row in get_neighbors(x, x_max)
        for col in get_neighbors(y, y_max)
    }
    neighbors.remove((x, y))
    return neighbors

def reduce_matrix(matrix: np.ndarray, starting_row: int, column_index: int, recursive=True):
    column = (matrix[:, column_index])
    row_index = starting_row
    while row_index < column.shape[0] and column[row_index] == 0: # Find the first non-zero row in the column
        row_index += 1
        if row_index == column.shape[0]:
            if recursive: 
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
    if recursive: 
        reduce_matrix(matrix, starting_row + 1, column_index + 1)

if __name__ == "__main__":
    input_matrix = np.array([
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2]
        ]
    )
    copy = input_matrix.copy()
    reduce_matrix(copy, 0, 0, recursive=False)
    reduce_matrix(copy, 1, 1, recursive=False)
    reduce_matrix(copy, 2, 2, recursive=False)
    reduce_matrix(copy, 3, 3, recursive=False)
    reduce_matrix(copy, 4, 4, recursive=False)
    #reduce_matrix(copy, 5, 5, recursive=False)
    #print(copy)
    reduce_matrix(input_matrix, 0, 0)
    print(input_matrix)