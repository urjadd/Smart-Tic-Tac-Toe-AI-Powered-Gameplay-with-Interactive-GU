import sys
import copy

board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

initial_board = copy.deepcopy(board)

def check_winner(board):
    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            if row[0] == 'X':
                print('Player 1 wins')
                exit()
            else:
                print('Player 2 wins')
                exit()
            return

    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                print('Player 1 wins')
                exit()
            else:
                print('Player 2 wins')
                exit()
            return

    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            print('Player 1 wins')
            exit()
        else:
            print('Player 2 wins')
            exit()
        return

    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            print('Player 1 wins')
            exit()
        else:
            print('Player 2 wins')
            exit()
        return

    print('No winner yet')

def board_representation(a, player):
    if a == 0:
        print('You have choosen to exit the game! see you again!')
        exit()
    position = {1: [0, 0],
                2: [0, 1],
                3: [0, 2],
                4: [1, 0],
                5: [1, 1],
                6: [1, 2],
                7: [2, 0],
                8: [2, 1],
                9: [2, 2]}
    

    # Initialize the board first

    board[position[a][0]][position[a][1]] = player
    check_winner(board)
    return board


#board_representation()

def display_board(a,player):
    board = board_representation(a,player)

    print(f'{board[0][0]} | {board[0][1]} |  {board[0][2]}')
    print('---------------------')
    print(f'{board[1][0]} | {board[1][1]} |  {board[1][2]}')
    print('---------------------')
    print(f'{board[2][0]} | {board[2][1]} |  {board[2][2]}')

#display_board()
def exit_stratergy():
    ans = int(input('Do you want to restart?press 1 or to exit press 0: '))
    if ans == 0:
        print('You have choosen to exit the game! see you again!')
        sys.exit()

    else:
        global board
        board = copy.deepcopy(initial_board)
        print(board)
        player()


def player():
    player = 0
    ply_input = 1
    visited =[]
    while ply_input != 0:
        if player == 0:
            ply_input = int(input('Player 1:Enter the position you want to put your mark on, press 0 to exit:' ))
            if ply_input not in visited:
                player = display_board(ply_input, 'X')
                player = 1
                visited.append(ply_input)
            else:
                print('Position occupied, choose a different positon')
                player = 0
        
        else:
            ply_input = int(input('Player 2:Enter the position you want to put your mark on, press 0 to exit:' ))
            if ply_input not in visited:
                display_board(ply_input, 'O')
                player = 0
                visited.append(ply_input)
            else:
                print('Position occupied, choose a different positon')
                player = 1
        
exit = exit_stratergy
player()
