#1. build the board 9 spaces 3 columns of 3
board = [" " for i in range(9)]#9 blank strings

def print_board():
    row1 = "|{} |{} |{} |".format(board[0], board[1], board[2])
    row2 = "|{} |{} |{} |".format(board[3], board[4], board[5])
    row3 = "|{} |{} |{} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

while True: #game loop
    print_board()
    choice = int(input("enter your move 1-9").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = "X"
    else:
        print()
        print("that space is taken")

