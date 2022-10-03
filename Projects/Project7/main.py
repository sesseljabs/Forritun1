def init_board(dim):
    '''Returns an initialized board for the given dimension.'''
    board = []
    pos = 1

    for i in range(dim):
        sublist = []
        for j in range(dim):
            sublist.append(str(pos))
            pos += 1
        board.append(sublist)
    return board

# prints entire board
def printBoard(board):
    for i in board:
        for j in i:
            print(f"{j : >5}", end="")
        print()


# adds a value to a section of a board
def addPos(val,pos,board):
    # x = pos//dim
    # position divided by width gives what row the number is in
    # y = pos%dim
    # the leftovers give where in that row the number is
    pos -= 1
    dim = len(board)
    x = pos//dim
    y = pos % dim
    board[x][y] = val
    return board


# check if the board has been filled
def isFull(board):
    for i in board:
        for j in i:
            if j != "X" and j != "O":
                return False
    else:
        return True

# check if a row is all the same
def checkRow(row):
    a = row[0]
    for i in row:
        if i != a:
            return False
    else:
        return True

# check if a column is all the same
def checkCol(board, rownum):
    a = board[0][rownum]
    for i in range(len(board)):
        if board[i][rownum] != a:
            return False
    else:
        return True


# checks for win across the board
def checkCross(board):
    lrcross = True
    rlcross = True
    a = board[0][0]
    b = board[0][-1]

    # top left to bottom right diagonal
    for i in range(len(board)):
        if board[i][i] != a:
            lrcross = False

    # bottom left to top right diagonal line
    for i in range(len(board)):
        if board[i][len(board)-1-i] != b:
            rlcross = False
    
    return lrcross or rlcross
        

# check if someone has won the game
def checkWinner(board):
    winner = False
    usr = ""
    # check each row
    for i in range(len(board)):
        if checkRow(board[i]) == True:
            winner = True
            return True
    # check each column
    for i in range(len(board)):
        if checkCol(board, i) == True:
            winner = True
            return True
    

    if checkCross(board) == True:
        winner = True

    return winner

# function that checks if input is allowed
def canInput(pos,board):
    # first checks if it's an integer
    if pos.isdigit() == False:
        return False

    pos = int(pos)
    pos -= 1
    dim = len(board)
    x = pos//dim
    y = pos % dim
    if pos+1>dim*dim: # check if out of bounds
        return False
    return not (board[x][y] == "X" or board[x][y] == "O") # checks if chosen position has already been selected


def main():
    '''Your main function.  Do NOT change the given code.'''
    dim = int(input("Input dimension of the board: "))
    board = init_board(dim)

    printBoard(board)
    
    game = True
    turn = "X"

    while game:
        game = not (checkWinner(board) or isFull(board))

        # this is X's turn
        if turn == "X":
            xpos = input("X position: ")
            while canInput(xpos, board) == False:
                print("Illegal move!")
                xpos = input("X position: ")

            board = addPos("X", int(xpos), board)

            turn = "O"

        # this is O's turn
        elif turn == "O":
            opos = input("O position: ")
            while canInput(opos, board) == False:
                print("Illegal move!")
                opos = input("O position: ")

            board = addPos("O", int(opos), board)

            turn = "X"

        printBoard(board)
        
        game = not (checkWinner(board) or isFull(board))

    if isFull(board):
        print("Draw!")
    elif turn == "O":
        print("Winner is: X")
    elif turn == "X":
        print("Winner is: O")
        
    
    

if __name__ == "__main__":
    main()