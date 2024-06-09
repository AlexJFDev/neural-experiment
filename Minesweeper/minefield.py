import numpy as np
import random
from field import Field

class Minefield:
    def stringify_field(field: np.ndarray, flag_filler: str = 'F', unknown_filler: str = '#') -> str:
        height, width = field.shape
        gap = 3
        string = ' ' * gap
        for i in range(height):
            string += f'{chr(ord("A") + i)} '
        string += '\n'
        for i in range(height):
            string += f'{i + 1:<3}'
            for j in range(width):
                num = field[i, j]
                if (num == -1):
                    string += f'{flag_filler} '
                elif (num == -2):
                    string += f'{unknown_filler} '
                else:
                    string += f'{num} '
            string += '\n'
        return string[:-1]

    def __init__(self, height, width, num_mines):
        if height * width < num_mines + 9: raise ValueError('More mines than valid spaces')
        self.__field = np.full((height, width), -2, dtype=int)
        self.__rows = height
        self.__width = width
        self.__num_mines = num_mines
        self.__revealed_cords = set()
        self.__flaged_cords = set()
        self.__mined_cords = set()
        self.__mines_placed = False

    def __place_mines(self, x, y):
        row_values = np.arange(self.__rows)
        col_values = np.arange(self.__width)
        all_coords = {(row, col) for row in row_values for col in col_values}
        invalid_coords = self.__get_neighboring_coords(x, y)
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
        for coord in self.__get_neighboring_coords(x, y):
            if (self.__is_mined(*coord)): 
                surrounding_mines += 1
        return surrounding_mines

    def __get_neighboring_rows(self, x):
        if (x <= 0): return {x, x + 1}
        if (x >= self.__rows - 1): return {x - 1, x}
        return {x - 1, x, x + 1}

    def __get_neighboring_cols(self, y):
        if (y <= 0): return {y, y + 1}
        if (y >= self.__width - 1): return {y - 1, y}
        return {y - 1, y, y + 1}
    
    def __get_neighboring_coords(self, x, y):
        return {
            (row, col) 
            for row in self.__get_neighboring_rows(x) 
            for col in self.__get_neighboring_cols(y)
        }
    
    def __is_valid_coord(self, x, y):
        if (x < 0 or x >= self.__rows): return False
        if (y < 0 or y >= self.__width): return False
        return True
    
    def _get_field(self):
        return self.__field
    
    def print_field(self):
        print(Minefield.stringify_field(self.__field))

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
        self.__field[x, y] = surrounding_mines
        if (surrounding_mines == 0):
            for coord in self.__get_neighboring_coords(x, y):
                if (coord not in self.__revealed_cords):
                    self.reveal(*coord)

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
        self.__field[x, y] = -1

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
        self.__field [x, y] = -1

    def check_clear(self):
        if (self.__mines_placed == False): return False
        difference = self.__mined_cords.symmetric_difference(self.__flaged_cords)
        if (len(difference) == 0):
            return True
        return False