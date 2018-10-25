def game_board(piece, x, y):
    """the game board is a 2d list that holds the game logic
        accepts as arguments the game piece
        and coordinates ( x == index in list 1, y == index in nested list)
        on game board"""
    logic_board = [[[], [], []],
                   [[], [], []],
                   [[], [], []]
                   ]

    logic_board[x][y] = piece
    # the board needs to retain it's updated state while game is in play
    # need a separate function to update?
    return f"{logic_board[0][0]}|{logic_board[0][1]}|{logic_board[0][2]} \n{logic_board[1][0]}|{logic_board[1][1]}|{logic_board[1][2]} \n{logic_board[2][0]}|{logic_board[2][1]}|{logic_board[2][2]} \n"


print(game_board('X', 1, 1))
