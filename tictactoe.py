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
                print("The game is a tie!")
            else:
                turn = "p2"
    
    else: #Player two
        
        print_board(board)
        print("Player two's move: ")
        move = player_move(board)
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
                print("The game is a tie!")
            else:
                turn = "p1"