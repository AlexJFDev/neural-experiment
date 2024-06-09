from minefield import Minefield
from os import system

if __name__ == "__main__":
    rows = int(input('Rows: '))
    cols = int(input('Columns: '))
    mines = int(input('Mines: '))
    field = Minefield(rows, cols, mines)

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
    