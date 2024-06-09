import numpy as np

def reduce_matrix(matrix):
    print(matrix[:, 0])

def reduce_column(matrix, starting_row, column_index):
    column = (matrix[:, column_index])
    pass

if __name__ == "__main__":
    input_matrix = np.array(
        [
            #A  B  C  D  E  F  G  H  I  J  K  coefficient
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
            #A  B  C  D  E  F  G  H  I  J  K  coefficient
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0], # 1
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], # 2
            [0, 0, 1, 0, 0,-1, 1, 0, 0, 0, 0, 0], # 3
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], # 4
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], # 5
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # 6
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], # 7
        ]
    )
    reduce_matrix(input_matrix)