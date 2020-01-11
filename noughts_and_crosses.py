import numpy as np 

# create an empty board using a 2D array
board = np.array(
[["0", "1", "2"],
["3", "4", "5"],
["6", "7", "8"]])

# Test that the initial board is displayed correctly.
# print(board)

# reset a square's value to X. This is the long way round. 
def set_square(player_choice):
    if player_choice == "0": 
        board[0, 0] = "X"
    elif player_choice == "1": 
        board[0, 1] = "X"
    elif player_choice == "2": 
        board[0, 2] = "X"
    elif player_choice == "3": 
        board[1, 0] = "X"
    elif player_choice == "4": 
        board[1, 1] = "X"
    elif player_choice == "5": 
        board[1, 2] = "X"
    elif player_choice == "6": 
        board[2, 0] = "X"
    elif player_choice == "7": 
        board[2, 1] = "X"
    elif player_choice == "8": 
        board[2, 2] = "X"
    else:
        print("You've entered an invalid choice.")

# check if a square has been used
def check_if_square_has_been_used():
    if board.size > 0:
     if np.any(board == "X"):
        return "That's already been used"

#get the user to add a square to the board
def add_a_square():
    print("We're going to play noughts and crosses.")
    square = input("Pick a square: ")
    check_if_square_has_been_used()
    set_square(square)
    print(board)

# test the add square function
# add_a_square()

# get the user to keep adding squares.
def play():
    while np.any(board != "X"):
        add_a_square()

# run the game
play()