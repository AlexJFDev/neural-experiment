import numpy as np

class Field:
    def __init__(self, rows, cols, filler='#'):
        self.__field = np.full((rows, cols), filler)
        self.__rows = rows
        self.__cols = cols

    def __str__(self):
        gap = 3
        string = ' ' * gap
        for i in range(self.__cols):
            string += f'{chr(ord("A") + i)} '
        string += '\n'
        for i in range(self.__rows):
            string += f'{i + 1:<3}'
            for j in range(self.__cols):
                string += f'{self.__field[i, j]} '
            string += '\n'
        return string[:-1]
    
    def set_coord(self, x, y, value):
        self.__field[x, y] = value
