import numpy as np
import field
from minefield import Minefield

def create_field_matrix(minefield: Minefield) -> np.ndarray:
    coord_to_col = {} # Each coordinate (that we care about) gets assigned a column in the matrix
    col_to_coord = {} # Convert back easily
    matrix_width = 0 # Width not including constant column (width - 1)
    constants = [] # will become last column of matrix
    rows = [] # Each row in this list says which columns should be 1's
    field = minefield._get_field()
    height, width = field.shape
    for i in range(height):
        for j in range(width): # Iterate over the coordinates
            constant = field[i, j] # The constant IF a matrix row is made
            if constant > 0: # If it's an edge tile
                coords = get_2d_neighbors(i, j, height, width)
                cols = [] # The columns of the matrix that will be 1's
                for coord in coords: # Iterate through neighbors
                    x, y = coord
                    value = field[x, y] # Get the neighbor's value
                    if (value == -1): # -1 is flag
                        constant -= 1 # If there is a flag, the tile has one fewer unknown mines
                    elif (value == -2): # -2 is an unknown title
                        col = coord_to_col.get(coord) # Get the column the coord is equivalent to
                        if col is None: # Add coord to dicts if it's not there
                            col = matrix_width
                            matrix_width += 1
                            coord_to_col[coord] = col
                            col_to_coord[col] = coord
                        cols.append(col) # Add the column to cols
                    # if constant == 0: break # If the tile has enough flagged mines we can ignore it
                # if constant == 0: continue # Except I don't think that's actually true
                constants.append([constant])
                rows.append(cols)
    field_matrix = np.zeros((len(constants), matrix_width), dtype=int) # Create a matrix of 0's
    for row_index in range(len(rows)): # Fill the matrix in
        row = rows[row_index] # Each row in rows is a list of numbers. 
        field_matrix[row_index][row] = 1 # These numbers determine which columns in the row should be 1
    field_matrix = np.concatenate([field_matrix, constants], axis=1) # Add the constants column
    return field_matrix, col_to_coord

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

def reduce_matrix(matrix: np.ndarray, starting_row = 0, column_index = 0, recursive=True):
    """
    matrix:
        A 2D numpy array.
    starting_row:
        Which row to start looking for a leading coefficient in.
    column_index:
        Which column to reduce.
    recursive:
        Toggle recursion on and off. Mostly for testing purposes.
    Recursively performs row reduction (gaussian elimination) on an augmented matrix.
    Each iteration reduces one column at a time.
    """
    # If there are no more rows
    if (starting_row == matrix.shape[0]): return
    # If there are no more columns except the augmented column
    if (column_index == matrix.shape[1] - 1): return

    column = (matrix[:, column_index])
    row_index = starting_row
    while row_index < column.shape[0] and column[row_index] == 0: # Find the first non-zero row in the column
        row_index += 1
        if row_index == column.shape[0]:
            if recursive: 
                reduce_matrix(matrix, starting_row=starting_row, column_index=column_index + 1) # No reduction is possible in this column
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

    if recursive: 
        reduce_matrix(matrix, starting_row=starting_row + 1, column_index=column_index + 1)

def solve_field_matrix(field_matrix: np.ndarray, column_dictionary: dict):
    """
    Solves a field matrix by finding the safe and mined columns.

    Args:
        field_matrix (np.ndarray): The field matrix to be solved.
        column_dictionary (dict): A dictionary mapping column indices to coordinates.

    Returns:
        None
    Note:
        The function assumes that the field matrix is a 2D numpy array and the column dictionary maps column indices to coordinates.

    """
    mined_cols = set()
    for row in field_matrix:
        if (np.count_nonzero(row) == 0):
            continue
        constant = row[-1]
        lower_bound = 0
        upper_bound = 0
        positives = set()
        negatives = set()
        for col_index in range(row.shape[0] - 1):
            col_val = row[col_index]
            if col_val < 0:
                lower_bound += col_val
                negatives.add(col_index)
            elif col_val > 0:
                upper_bound += col_val
                positives.add(col_index)
        if lower_bound == constant:
            mined_cols = mined_cols.union(negatives)
            safe_cols = safe_cols.union(positives)
        elif upper_bound == constant:
            mined_cols = mined_cols.union(positives)
            safe_cols = safe_cols.union(negatives)
    for col in mined_cols:
        coord = column_dictionary[col]
        print('Flag', coord, col)
    for col in safe_cols:
        coord = column_dictionary[col]
        print('Reveal', coord, col)



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