from random import randint
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # creat bord for collect cells from numlock which will use
position = []
print('Welcome to TIC TAC TOE game!!!')
game = input("Input 'Yes' to start game or 'No' if you don't want play: ")
if game[0].lower() == 'y':
    player_1 = input('Player 1: Do you want to be X or O ? ').upper()
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    players = (0, player_1, player_2)
    first_gamer = players[randint(1, 2)]
    if first_gamer == 'O':
        second_gamer = 'X'
    else:
        second_gamer = 'O'
    print(f'The first player will be Player {players.index(first_gamer)}')
    i = 1
    while range(1,11,1) not in position:
        i += 1
        if i % 2 == 0:
            curent_position = int(input(f'Player {first_gamer} Choose you next position from (1-9): '))
            position.append(curent_position)
            board.pop(curent_position)
            board.insert(curent_position, first_gamer)
            pole = {'line01': [' ', ' ', ' | ', ' ', ' | ', ' ', ' \n'], 'line': ['-----------\n'],
                    'line_3': [' ', board[7], ' | ', board[8], ' | ', board[9], ' \n'],
                    'line_2': [' ', board[4], ' | ', board[5], ' | ', board[6], ' \n'],
                    'line_1': [' ', board[1], ' | ', board[2], ' | ', board[3], ' \n']}
            print(''.join(pole['line01'] + pole['line_3'] + pole['line01'] + pole['line'] +
                          pole['line01'] + pole['line_2'] + pole['line01'] + pole['line'] +
                          pole['line01'] + pole['line_1'] + pole['line01']))

        else:
            curent_position = int(input(f'Player {second_gamer} Choose you next position from (1-9): '))
            position.append(curent_position)
            board.pop(curent_position)
            board.insert(curent_position, second_gamer)
            pole = {'line01': [' ', ' ', ' | ', ' ', ' | ', ' ', ' \n'], 'line': ['-----------\n'],
                    'line_3': [' ', board[7], ' | ', board[8], ' | ', board[9], ' \n'],
                    'line_2': [' ', board[4], ' | ', board[5], ' | ', board[6], ' \n'],
                    'line_1': [' ', board[1], ' | ', board[2], ' | ', board[3], ' \n']}
            print(''.join(pole['line01'] + pole['line_3'] + pole['line01'] + pole['line'] +
                          pole['line01'] + pole['line_2'] + pole['line01'] + pole['line'] +
                          pole['line01'] + pole['line_1'] + pole['line01']))
        if board[7] == board[4] == board[1] == 'X' or board[8] == board[5] == board[2] == 'X' \
                or board[9] == board[6] == board[3] == 'X' or board[7] == board[8] == board[9] == 'X'\
                or board[4] == board[5] == board[6] == 'X' or board[1] == board[2] == board[3] == 'X'\
                or board[7] == board[5] == board[3] == 'X' or board[9] == board[5] == board[1] == 'X':
            print("Player 'X' WIN!!!")
            break
        elif board[7] == board[4] == board[1] == 'O' or board[8] == board[5] == board[2] == 'O' \
                or board[9] == board[6] == board[3] == 'O' or board[7] == board[8] == board[9] == 'O' \
                or board[9] == board[6] == board[3] == 'O' or board[7] == board[8] == board[9] == 'O' \
                or board[4] == board[5] == board[6] == 'O' or board[1] == board[2] == board[3] == 'O' \
                or board[7] == board[5] == board[3] == 'O' or board[9] == board[5] == board[1] == 'O':
            print("Player 'O' WIN!!!")
            break
        else:
            continue
    else:
        print('Game is finished. Have no winner!')
else:
    pass





