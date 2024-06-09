from minefield import Minefield
from os import system
import helper_functions

def play_game():
    height = int(input('Height: '))
    width = int(input('Width: '))
    mines = int(input('Mines: '))
    field = Minefield(height, width, mines)

    print('Give input in the form of a command followed by a coordinate.')
    print('Commands: flag, unflag, reveal, check')
    print('The first tile you reveal will always be safe.')

    field.print_field()
    while(True):
        inputs = input().split(' ')
        command = inputs[0]
        try:
            if (command == 'check'): 
                if (field.check_clear()):
                    print('You won!')
                    break
                else:
                    print('Keep trying!')
                    continue
            row = int(inputs[1]) - 1
            col = ord(inputs[2].upper()) - ord('A')
        except:
            print('Invalid input')
            continue
        #system('clear')
        if (command == 'flag'): field.flag(row, col)
        if (command == 'unflag'): field.unflag(row, col)
        if (command == 'reveal'): field.reveal(row, col)
        field.print_field()

if __name__ == "__main__":
    field = Minefield(5, 5, 5)
    field._set_mines([(3, 4), (4, 4), (3, 0), (0, 0), (0, 3)])
    field.reveal(2, 2)
    field.print_field()
    field.reveal(2, 0)
    field.reveal(2, 4)
    field.flag(3, 4)
    field.flag(4, 4)
    field.print_field()
    field_matrix, column_dictionary = helper_functions.create_field_matrix(field)
    print(column_dictionary)
    print(field_matrix)
    helper_functions.reduce_matrix(field_matrix, 0, 0)
    print(field_matrix)