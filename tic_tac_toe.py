board = [[[1], [2], [3]],
            [[4], [5], [6]],
            [[7], [8], [9]]
            ]

def display_board(board):
    bar = "." * 13
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}\n{board[1][0]}|{board[1][1]}|{board[1][2]} \n{board[2][0]}|{board[2][1]}|{board[2][2]} \n")


def update_board(board, piece, x, y):
    """the game board is a 2d list that holds the game logic
        accepts as arguments the game piece
        and coordinates ( x == index in list 1, y == index in nested list)
        on game board"""


    board[x][y] = piece
    # the board needs to retain it's updated state while game is in play
    # need a separate function to update?
    # Break off display code into it's own function
    return board




# WILO get logic board state to persist through plays
# building game engine
board = update_board(board, 'X', 1, 1)
board = update_board(board, 'O', 0, 1)
display_board(board)
def main():
    pass

if __name__ == "__main__":
    main()