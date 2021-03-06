import random

player_1 = "X" #Player one is X
player_2 = "O" #Player two is O
game = True

#Show the numbers that correspond with each space
def instructions():
    print("Board and number layout:")
    print("")
    print(" %s | %s | %s " %(1,2,3))
    print("---+---+---")
    print(" %s | %s | %s " %(4,5,6))
    print("---+---+---")
    print(" %s | %s | %s " %(7,8,9))
    print("")
    
    while True:
        choice = raw_input("Press 'Y' to continue: ")
        print("")
        if choice.lower() == "y":
            break
        
#Print board with move choices
def print_board(board):
    print(" %s | %s | %s " %(board[1], board[2], board[3]))
    print("---+---+---")
    print(" %s | %s | %s " %(board[4], board[5], board[6]))
    print("---+---+---")
    print(" %s | %s | %s " %(board[7], board[8], board[9]))
    print("")
    
#Duplicate board for the computer to use
def copy_board(board):
    dup_board = []
    
    for position in board:
        dup_board.append(position)
    return dup_board

board = [" "] * 10 #Fill board with blanks

#Check if anyone has won yet
def check_win(board, move):
    
    return ((board[1] == move and board[2] == move and board[3] == move) or
    (board[4] == move and board[5] == move and board[6] == move) or
    (board[7] == move and board[8] == move and board[9] == move) or
    (board[1] == move and board[4] == move and board[7] == move) or
    (board[1] == move and board[5] == move and board[9] == move) or
    (board[2] == move and board[5] == move and board[8] == move) or
    (board[3] == move and board[6] == move and board[9] == move) or
    (board[3] == move and board[5] == move and board[7] == move))

#Place move on the board
def place_move(board, move, position):
    board[position] = move

#Make sure the space isn't taken    
def check_space(board, position):
    return board[position] == " "

#Check if the board is full in cases of a tie    
def board_check(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True

#Choose a position on the board, check if it's taken, then place the move
def player_move(board):
    move = " "
    while move not in range(1,10) or not check_space(board, int(move)):
        move = int(input("Choose a space: (1-9) "))
        print("")
    return move
    
#Chooses a move for the computer based on board position availability
def random_move(board, moves):
    open_positions = []
    for move in moves:
        if check_space(board, move):
            open_positions.append(move)
            
    #Check if there are actual moves to make
    if len(open_positions) != 0:
        return random.choice(open_positions)
    else:
        return None
        
#Computer's move
def comp_move(board):
    
    #See if the computer can win in the next move
    for move in range(1,10):
        copy = copy_board(board)
        if check_space(copy, move):
            place_move(copy, player_2, move)
            if check_win(copy, player_2):
                return move
                
    #See if player 1 could win in the next move. Block them if necessary
    for move in range(1,10):
        copy = copy_board(board)
        if check_space(copy, move):
            place_move(copy, player_1, move)
            if check_win(copy, player_1):
                return move
    #Move to the middle if it's free
    if check_space(board, 5):
        return 5
        
    #Choose a corner if it's free
    move = random_move(board, [1,3,7,9])
    if move != None:
        return move
        
    #Choose a side
    return random_move(board, [2,4,6,8])
    
    
#Reset board
def reset_board():
    board = [" "] * 10

instructions()

turn = "p1"

while game:
    
    if turn == "p1": #Player one
        
        print_board(board)
        print("Player one's move: ")
        move = player_move(board)
        place_move(board, player_1, move)
        
        if check_win(board, player_1):
            print_board(board)
            print("-----------------------")
            print("| Player one has won! |")
            print("-----------------------")
            game = False
        else:
            if board_check(board):
                print_board(board)
                print("----------------------")
                print("| The game is a tie! |")
                print("----------------------")
                break
            else:
                turn = "p2"
    
    else: #Player two
        
        print_board(board)
        print("The Computer's turn: ")
        move = comp_move(board)
        place_move(board, player_2, move)
        
        if check_win(board, player_2):
            print_board(board)
            print("-----------------------")
            print("| Player two has won! |")
            print("-----------------------")
            game = False
        else:
            if board_check(board):
                print_board(board)
                print("----------------------")
                print("| The game is a tie! |")
                print("----------------------")
                break
            else:
                turn = "p1"