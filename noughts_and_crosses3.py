# import numpy as np

# create an empty board using a 2D array
board = [["0", "1", "2"],
["3", "4", "5"],
["6", "7", "8"]]

# Test that the initial board is displayed correctly.
# print(board)

# get the user to add a square to the board
def choose_square(board):
    print("We're going to play noughts and crosses. Here's the board.")
    for row in board:
        print(row)
    x = input("Pick the row coordinate: ")
    while not x.isnumeric():
        print("This is not a valid number.")
        x = int(input("Try again: "))
    y = input("Pick the column coordinate: ")
    while not y.isnumeric():
        print("This is not a valid number.")
        y = int(input("Try again: "))

    # if x in range(0, 9) and y in range(0, 9):
    board[x][y] = "X"
    print("You chose {}, {}.".format(x, y))
    for row in board:
        print(row)
    

choose_square(board)
# print(board)

# Identifies all the winning lines (for "X") and plays until one of them is reached. It's very long using an elif - investigate other possibilities (maybe a switch?)
def play_until_winning_line(board):
    for i in range(len(board)):
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            print("winner")
            return 
        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            print("winner")
            return 
        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            print("winner")
            return 
        elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            print("winner")
            return 
        elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            print("winner")
            return 

        elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            print("winner")
            return 
        elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
            print("winner")
            return 
        elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("winner")
            return 
        else: 
            choose_square(board)

play_until_winning_line(board)