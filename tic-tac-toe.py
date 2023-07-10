turn = 0
board = [[' '] * 3 for i in range(3)]
def BOARD(board):

    print(f"  0   1   2")
    for i in range(3):
        print(f'{i} {board[i][0]} | {board[i][1]} | {board[i][2]}')
        if i<2:
            print(f'  ---------')

def Input(board):
    while True:
        coords = input('Ход: ').split()
        if len(coords) != 2:
            print('Введите ДВЕ координаты')
        else:
            x, y = map(int, coords)
            if 0 <= x <= 2 and 0 <= y <= 2:
                if board[y][x] != ' ':
                    print('Клетка занята')
                else:
                    return x, y
            else:
                print('Координаты вне диапазона')

def win(board):
    for i  in range(3):
        caracter = []
        for j in range(3):
            caracter.append(board[i][j])

        if caracter == ['X','X','X']:
            return 'X'
        elif caracter == ['0', '0', '0']:
            return '0'

    for j in range(3):
        caracter = []
        for i in range(3):
            caracter.append(board[i][j])
        if caracter == ['X','X','X']:
            return 'X'
        elif caracter == ['0', '0', '0']:
            return '0'

    caracter = []
    for i in range(3):
        caracter.append(board[i][i])
    if caracter == ['X','X','X']:
        return 'X'
    elif caracter == ['0', '0', '0']:
        return '0'

    caracter = []
    for i in range(3):
        caracter.append(board[i][2-i])
    if caracter == ['X','X','X']:
        return 'X'
    elif caracter == ['0', '0', '0']:
        return '0'



###################################################################

print('Давайте начнем')
BOARD(board)

while True:
    turn +=1
    if turn % 2 == 0:
        print('Ход крестика')
        x,y = map(int, Input(board))
        board[y][x] = 'X'
    else:
        print('Ход нолика')
        x, y = map(int, Input(board))
        board[y][x] = '0'
    BOARD(board)

    if win(board) == 'X':
        print('Выйграл крестик')
        break
    elif win(board) == '0':
        print('Выйграл нолик')
        break
    if turn >= 9:
        print('Игра закончена')
        break


