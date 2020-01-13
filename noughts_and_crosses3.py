# import numpy as np

# create an empty board using a 2D array
board = [["0", "1", "2"],
["3", "4", "5"],
["6", "7", "8"]]

# Test that the initial board is displayed correctly.
print(board)

#get the user to add a square to the board
def choose_square():
    board = [["0", "1", "2"],
["3", "4", "5"],
["6", "7", "8"]]
    print("We're going to play noughts and crosses.")
    for square in board:
        print(square)
        # while square != "X":
        #     x = int(input("Pick the x coordinate: "))
        #     y = int(input("Pick the y coordinate: "))
        #     board[x][y] = "X"
        #     print("You chose {}, {}.".format(x, y))
        #     print(board)
#     set_square(square)
#     print(board)
choose_square()
