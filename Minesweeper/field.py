import numpy as np

class Field:
    def __init__(self, rows, cols, filler='#'):
        self.__field = np.full((rows, cols), -1)
        self.__rows = rows
        self.__cols = cols
        self.__filler = filler

    def __str__(self):
        gap = 3
        string = ' ' * gap
        for i in range(self.__cols):
            string += f'{chr(ord("A") + i)} '
        string += '\n'
        for i in range(self.__rows):
            string += f'{i + 1:<3}'
            for j in range(self.__cols):
                num = self.__field[i, j]
                if (num == -1):
                    string += f'{self.__filler} '
                else:
                    string += f'{num} '
            string += '\n'
        return string[:-1]
    
    def get_neighboring_rows(self, x):
        if (x <= 0): return [x, x + 1]
        if (x >= self.__rows - 1): return [x - 1, x]
        return [x - 1, x, x + 1]
    
    def get_neighboring_cols(self, y):
        if (y <= 0): return [y, y + 1]
        if (y >= self.__width - 1): return [y - 1, y]
        return [y - 1, y, y + 1]
    
    def _get(self):
        return self.__field

    def set_coord(self, x, y, value):
        self.__field[x, y] = value
