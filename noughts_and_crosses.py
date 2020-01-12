import numpy as np 

# create an empty board using a 2D array
board = np.array(
[["0", "1", "2"],
["3", "4", "5"],
["6", "7", "8"]])

# Test that the initial board is displayed correctly.
# print(board)

# set co-ordinates as variables
# coord0 = board[0, 0]
coord0 = np.argwhere(board == "0")
coord1 = np.argwhere(board == "1")
coord2 = np.argwhere(board == "2")
coord3 = np.argwhere(board == "3")
coord4 = np.argwhere(board == "4")
coord5 = np.argwhere(board == "5")
coord6 = np.argwhere(board == "6")
coord7 = np.argwhere(board == "7")
coord8 = np.argwhere(board == "8")



# coord1 = board[0, 1] 
# coord2 = board[0, 2] 
# coord3 = board[1, 0] 
# coord4 = board[1, 1] 
# coord5 = board[1, 2] 
# coord6 = board[2, 0] 
# coord7 = board[2, 1] 
# coord8 = board[2, 2] 

# create an array of co-ordinates. necessary?
coordinates = np.array([coord0, coord1, coord2, coord3, coord4, coord5, coord6, coord7, coord8])

# create an empty array or list 
# chosen_squares = np.empty(2)
chosen_squares = []
# squares = np.array([])
# chosen_squares.append(coord0)
# set chosen squares
# print(chosen_squares)

# reset a square's value to X. This is the long way round. 
def set_square(player_choice):
    if player_choice == "0": 
        board[0, 0] = "X"
        chosen_squares.append(coord0)
    elif player_choice == "1": 
        board[0, 1] = "X"
        chosen_squares.append(coord1)
    elif player_choice == "2": 
        board[0, 2] = "X"
        chosen_squares.append(coord2)
    elif player_choice == "3": 
        board[1, 0] = "X"
        chosen_squares.append(coord3)
    elif player_choice == "4": 
        board[1, 1] = "X"
        chosen_squares.append(coord4)
    elif player_choice == "5": 
        board[1, 2] = "X"
        chosen_squares.append(coord5)
    elif player_choice == "6": 
        board[2, 0] = "X"
        chosen_squares.append(coord6)
    elif player_choice == "7": 
        board[2, 1] = "X"
        chosen_squares.append(coord7)
    elif player_choice == "8": 
        board[2, 2] = "X"
        chosen_squares.append(coord8)
    else:
        print("You've entered an invalid choice.")

# check if a square has been used. If it was a list, I'd do a for loop, but maybe I can use a Numpy method
def check_if_square_has_been_used(square):
    # index = np.argwhere(board == square)
    # print("Index: {}".format(index))
    print("Square: {}".format(square))
    print(type(square))
    for row in board:
        for cell in row:
            # print("Position: {}".format(cell))
            print(type(cell))
            if cell == square:
                print("already taken")
                return True
        # if position == index:
        #     if position == "X":
        #         print("Already taken")


    # index = np.argwhere(board == square)
    # print(index)
    # if (len(chosen_squares) > 0):
    #     answer = index in chosen_squares
    #     print(answer)
            # if answer == True:
                # print("That's already been used")

#get the user to add a square to the board
def add_a_square():
    print("We're going to play noughts and crosses.")
    square = input("Pick a square: ")
    check_if_square_has_been_used(square)
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
print(chosen_squares)
# print(coord0)