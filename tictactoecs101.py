from random import randint


board = []

for x in range(0, 3):
    board.append(["_"] * 3)


def print_board(board):
    print("###")
    for row in board:
        print(" ".join(row))

    print("###")


check = True
while check:
    print_board(board)
    #Players turn
    print("Pick a row and column")
    guess_row = int(input("Guess Row: ")) - 1
    guess_column = int(input("Guess Column: ")) - 1
    if guess_row not in range(0,3) or guess_column not in range(0,3):
        print("row or column entered not in range")
        continue
    elif board[guess_row][guess_column] == "_":
        board[guess_row][guess_column] = "X"
        
    
    #"AI"s turn:
    choice = True
    while choice:
        guess_row_bot = randint(0,2)
        guess_col_bot = randint(0,2)
        if board[guess_row_bot][guess_col_bot] == "_":
            board[guess_row_bot][guess_col_bot] = "O"
            choice = False


    #Find winner:

    choice = True

    

    