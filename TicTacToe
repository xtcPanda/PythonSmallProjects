def print_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")
 
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")
 
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")

def check_win(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def tictactoe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        print("It's {}'s turn. Please enter a valid move (1-9):".format(player))
        move = input()

        while move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(move) - 1] != " ":
            print("Invalid move. Please enter a valid move (1-9):")
            move = input()

        board[int(move) - 1] = player

        if check_win(board, player):
            print_board(board)
            print("Congratulations! {} has won the game.".format(player))
            game_over = True
        elif " " not in board:
            print_board(board)
            print("The game is a tie.")
            game_over = True
        else:
            player = "O" if player == "X" else "X"

    print("Game over. Thanks for playing!")

tictactoe()
