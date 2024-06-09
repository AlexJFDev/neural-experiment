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
    field = Minefield(6, 6, 8)
    field.reveal(2, 2)
    field.print_field()
    field_matrix = helper_functions.create_field_matrix(field)