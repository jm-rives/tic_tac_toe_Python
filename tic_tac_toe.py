import random
# import time

# game board for players to assign their game pieces too
board = [[1], [2], [3],
            [4], [5], [6],
            [7], [8], [9]
            ]

game = True

# coin_flip
print("Time for a coin toss players. Choose heads or tails.")

# allow players time to choose heads or tails
# time.sleep(5)
coin_toss = random.randint(0, 1) % 2

if coin_toss == 0:
    result = "Heads"
else:
    result = "Tails"
# chosen player takes the first turn
print(f"The {result} wins! The winner is Player One and will play 'X' and move first")
playing_X = True

player_one = 'X'
player_two = 'O'


# game engine here
turn = 0
while game == True:


    if  playing_X == True:

        print(f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]} \n{board[6]}|{board[7]}|{board[8]} \n")
        move = int(input("Please enter the number where you want your mark:  "))
        # test to see if desired space taken
        try:
            # find board coordinates
            place = board.index([move])
            board[place] = player_one
        except:
            print("Sorry, that is not a valid move. Check the board and try again.")
            # function call to move later in game development
        playing_X = False
    else:
        print(
            f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]} \n{board[6]}|{board[7]}|{board[8]} \n")
        move = int(input("Please enter the number where you want your mark:  "))
        # test to see if desired space taken
        try:
            # find board coordinates
            place = board.index([move])
            board[place] = player_two
        except:
            print("Sorry, that is not a valid move. Check the board and try again.")
            # function call to move later in game development
        playing_X = True








