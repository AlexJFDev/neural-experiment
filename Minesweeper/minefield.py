import numpy as np
import random
from field import Field

class Minefield:
    def __init__(self, rows, cols, num_mines):
        if rows * cols < num_mines + 9: raise ValueError('More mines than valid spaces')
        self.__field = Field(rows, cols)
        self.__rows = rows
        self.__cols = cols
        self.__num_mines = num_mines
        self.__revealed_cords = set()
        self.__flaged_cords = set()
        self.__mined_cords = set()
        self.__mines_placed = False

    def __place_mines(self, x, y):
        row_values = np.arange(self.__rows)
        col_values = np.arange(self.__cols)
        all_coords = {(row, col) for row in row_values for col in col_values}
        invalid_coords = {
            (row, col) 
            for row in self.__get_neighboring_rows(x) 
            for col in self.__get_neighboring_cols(y)
        }
        valid_coords = all_coords.difference(invalid_coords)
        for i in range(self.__num_mines):
            coord = random.sample(valid_coords, 1)[0]
            valid_coords.remove(coord)
            self.__mined_cords.add(coord)
    
    def __is_mined(self, x, y):
        if ((x, y) in self.__mined_cords): return True
        return False
    
    def __count_surrounding_mines(self, x, y):
        surrounding_mines = 0
        for i in self.__get_neighboring_rows(x):
            for j in self.__get_neighboring_cols(y):
                if (self.__is_mined(i, j)):
                    surrounding_mines += 1
        return surrounding_mines

    def __get_neighboring_rows(self, x):
        if (x <= 0): return [x, x + 1]
        if (x >= self.__rows - 1): return [x - 1, x]
        return [x - 1, x, x + 1]
    
    def __get_neighboring_cols(self, y):
        if (y <= 0): return [y, y + 1]
        if (y >= self.__cols - 1): return [y - 1, y]
        return [y - 1, y, y + 1]
    
    def __is_valid_coord(self, x, y):
        if (x < 0 or x >= self.__rows): return False
        if (y < 0 or y >= self.__cols): return False
        return True
    
    def print_field(self):
        print(self.__field)

    def reveal(self, x, y):
        if (not self.__is_valid_coord(x, y)): 
            print(f'{x}, {y} is out of bounds.')
            return
        if (not self.__mines_placed):
            self.__place_mines(x, y)
            self.__mines_placed = True
        if ((x, y) in self.__flaged_cords): 
            print(f'{x}, {y} is flaged, unflag it first.')
            return
        if (self.__is_mined(x, y)): raise ValueError('You lose!')
        if ((x, y) in self.__revealed_cords): 
            print(f'{x}, {y} is already revealed.')
            return
        
        self.__revealed_cords.add((x, y))
        surrounding_mines = self.__count_surrounding_mines(x, y)
        self.__field.set_coord(x, y, surrounding_mines)
        if (surrounding_mines == 0):
            for i in self.__get_neighboring_rows(x):
                for j in self.__get_neighboring_cols(y):
                    if ((i, j) not in self.__revealed_cords):
                        self.reveal(i, j)

    def flag(self, x, y):
        if (not self.__is_valid_coord(x, y)): 
            print(f'{x}, {y} is out of bounds')
            return
        if ((x, y) in self.__revealed_cords): 
            print(f'{x}, {y} is already revealed')
            return
        if ((x, y) in self.__flaged_cords): 
            print(f'{x}, {y} is already flaged')
            return
        self.__flaged_cords.add((x, y))
        self.__field.set_coord(x, y, 'F')

    def unflag(self, x, y):
        if (not self.__is_valid_coord(x, y)): 
            print(f'{x}, {y} is out of bounds')
            return
        if ((x, y) in self.__revealed_cords): 
            print(f'{x}, {y} is already revealed')
            return
        if ((x, y) not in self.__flaged_cords): 
            print(f'{x}, {y} is not flaged')
            return
        self.__flaged_cords.remove((x, y))
        self.__field.set_coord(x, y, '#')

    def check_clear(self):
        if (self.__mines_placed == False): return False
        difference = self.__mined_cords.symmetric_difference(self.__flaged_cords)
        if (len(difference) == 0):
            return True
        return False