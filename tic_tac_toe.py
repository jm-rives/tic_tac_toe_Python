import random

# game board for players to assign their game pieces too
board = [[1], [2], [3],
            [4], [5], [6],
            [7], [8], [9]
            ]

game = True

# coin_flip
print("Time for a coin toss players. Choose heads or tails.")

coin_toss = random.randint(0, 1) % 2
if coin_toss == 0:
    result = "Heads"
else:
    result = "Tails"
# chosen player takes the first turn
print(f"The {result} wins! The winner will play 'X' and move first")

playerOne = 'X'
playerTwo = 'O'

# # turn increments
# turn = 0
# # board updates
# # repeat process with second player
# # check for win state after turn increments >= 3
#
#
# # get player input for next move
# move = int(input("Please enter the number where you want your mark:  "))
#
# # test to see if desired space taken
# try:
# # find board coordinates
#     place = board.index([move])
# except:
#     print("Sorry, that is not a valid move. Check the board and try again.")
#     # function call to move later in game development
#
# # update board with valid players move
# board[place] = playerOne # this value will be stored in a variable later in game development
#
# # this will display the game board
# print(f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]} \n{board[6]}|{board[7]}|{board[8]} \n")








