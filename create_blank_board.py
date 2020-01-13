# this file is just an idea. I don't think I'll use it in the game.

# function to display an ASCII version of a noughts and crosses board, but the user can define the size.
def get_board_size():
    size = int(input("How many rows will your board have?: "))
    horizontals = "___" * (size + 1)
    verticals = "|   " * (size + 1)
    for i in range(size):
        print(horizontals + "_")
        print(verticals)
    print(horizontals + "_")


get_board_size()
    