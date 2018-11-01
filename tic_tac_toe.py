import random

# game board for players to assign their game pieces too
board = [[1], [2], [3],
            [4], [5], [6],
            [7], [8], [9]
            ]

game = True

# randomly choose who goes first and assign player board piece
rand_num = random.randrange(1, 11)
# have both players guess a number, whoever is closet (abs value) is player one
get_guess = input("Please guess a number between 1 and 10 inclusive:👉 ")

guess1 = int(get_guess)
guess2 = int(get_guess)

first_guess = f"\n The number was {rand_num}\n The first guess entered is correct!\n You are Player One and will take a turn first turn."
second_guess = f"\n The number was {rand_num}\n The second guess entered is correct!\n You are Player One and will take a turn first turn."
# evaluates for correct guess of rand int
if guess1 == rand_num:
    print(first_guess)
elif guess2 == rand_num:
    print(second_guess)
elif (abs(guess1) - rand_num) < (abs(guess2) - rand_num):
    print(first_guess)
else:
    print(second_guess)

playerOne = 'X'
playerTwo = 'O'
# chosen player takes the first turn
# turn increments
turn = 0
# board updates
# repeat process with second player
# check for win state after turn increments >= 3


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
board[place] = playerOne # this value will be stored in a variable later in game development

# this will display the game board
print(f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]} \n{board[6]}|{board[7]}|{board[8]} \n")








