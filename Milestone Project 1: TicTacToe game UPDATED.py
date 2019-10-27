from random import randint
global board, players, position
position = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
userchoise = 0
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
players = []

def clear_outputs():
    print('\n' * 100)  # clear outputs in console, pretty easy to make 100 enters instead of longer code

def choose_mark():  # Choose mark for player 1. player to will be opposite
    global mark_1, mark_2  # make it global for work through all code
    while True:
        mark_1 = input('Now, Player 1 please choose "X" or "O": ').upper()
        clear_outputs()  # using it for make display clear
        if mark_1 == 'X' or mark_1 == 'O':  # if players make mistake and input something else not excepted keywords
            print(f'Player 1 choose: {mark_1}')
            if mark_1 == 'X':
                mark_2 = 'O'
            else:
                mark_2 = 'X'
            print(f'Then Player 2 will be: {mark_2}')
            break
        else:
            print('Oooops! Please choose correct.')



def choose_first_gamer():
    print('And now we will find out who will be the first!')
    global rand  # again make it global for easy access in further
    rand = randint(1, 2)
    if rand == 1:
        print('Player 1 go first!')
        players.append('Player 1')
        players.append(mark_1)
        players.append('Player 2')
        players.append(mark_2)
    else:
        print('Player 2 go first!')
        players.append('Player 2')
        players.append(mark_2)
        players.append('Player 1')
        players.append(mark_1)

def print_field():
    global pole
    pole = ['   |   |   \n',
            ' ', board[7], ' | ', board[8], ' | ', board[9], ' \n',
            '   |   |   \n-----------\n   |   |   \n',
            ' ', board[4], ' | ', board[5], ' | ', board[6], ' \n',
            '   |   |   \n-----------\n   |   |   \n',
            ' ', board[1], ' | ', board[2], ' | ', board[3], ' \n',
            '   |   |   \n']
    print(''.join(pole))

def user_choice():
    i = 1
    while len(position) > 1:
        i += 1
        if i % 2 == 0:
            a = players[3]
            while find_winner(a)== False:
                userchoise = int(input(f'{players[0]} "{players[1]}" please choose position (1-9) on the desk: '))
                if userchoise not in position:
                    print(f'Dear {players[0]} "{players[1]}" please take care choose position from 1 to 9.')
                    continue
                else:
                    clear_outputs()
                    board.pop(userchoise)
                    board.insert(userchoise, players[1])
                    position.remove(userchoise)
                    print_field()
                    break
            else:
                print(f'{players[2]} WIN this game!!!')
                break
        else:
            a = players[1]
            while find_winner(a) == False:
                userchoise = int(input(f'{players[2]} "{players[3]}" please choose position (1-9) on the desk: '))
                if userchoise not in position:
                    print(f'Dear {players[2]} "{players[3]}" please take care choose position from 1 to 9.')
                    continue
                else:
                    clear_outputs()
                    board.pop(userchoise)
                    board.insert(userchoise, players[3])
                    position.remove(userchoise)
                    print_field()
                    break
            else:
                print(f'{players[0]} WIN this game!!!')
                break
    else:
        return





def find_winner(a):
    if (board[1] == board[2] == board[3] == a) or \
        (board[4] == board[5] == board[6] == a) or \
        (board[7] == board[8] == board[9] == a) or \
        (board[7] == board[4] == board[1] == a) or \
        (board[8] == board[5] == board[2] == a) or \
        (board[7] == board[4] == board[1] == a) or \
        (board[9] == board[6] == board[3] == a) or \
        (board[7] == board[5] == board[3] == a) or \
        (board[9] == board[5] == board[1] == a):
        return True
    else:
        return False




game = input(print('Dear Players! Are you want to play this game? Please answer Y on N:')).lower()
if game == 'y':
    clear_outputs()
    choose_mark()
    clear_outputs()
    choose_first_gamer()
    clear_outputs()
    user_choice()
elif game == 'n':
    print('You dont want play now.')
else:
    print('Be carefull, y or n!')
