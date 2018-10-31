
# randomly choose who goes first and assign player board piece
playerOne = 'X'
playerTwo = 'O'
# chosen player gets to choose marker
# chosen player takes the first turn
# turn increments
# board updates
# repeat process with second player
# check for win state after turn increments >= 3

# game board for players to assign their game pieces too
board = [[1], [2], [3],
            [4], ['X'], [6],
            [7], [8], [9]
            ]

# get player input for next move
move = int(input("Please enter the number where you want your mark:  "))

# test to see if desired space taken
try:
# find board coordinates
    place = board.index([move])
except:
    print("Sorry, that is not a valid move. Check the board and try again.")
    # function call to move later in game development

# update board with valid players move
board[place] = playerTwo # this value will be stored in a variable later in game development

# this will display the game board
print(f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]} \n{board[6]}|{board[7]}|{board[8]} \n")








