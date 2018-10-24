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

    return logic_board

print(game_board('X', 2, 2))