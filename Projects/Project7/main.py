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


def printBoard(board):
    for i in board:
        for j in i:
            print(j,end="\t")
        print("\n")

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

def checkRow(row):
    a = row[0]
    for i in row:
        if i != a:
            return False
    else:
        return True

def checkCol(board, rownum):
    a = board[0][rownum]
    for i in range(len(board)):
        if board[i][rownum] != a:
            return False
    else:
        return True

def checkCross(board):
    a = [0][0]
    for i in range(len(board)):
        if a != board[i][i]:
            return False
    else:
        return True

# check if someone has won the game
def checkWinner(board):
    winner = False
    usr = ""
    # check each row
    for i in range(len(board)):
        if checkRow(board[0]) == True:
            winner = True
            return True

    for i in range(len(board)):
        if checkCol(board, i) == True:
            winner = True
            return True
    

    a = [0][0]
    for i in range(len(board)):
        if a != board[i][i]:
            return False
    else:
        return True

    lrcross = True
    rlcross = True
    a = board[0][0]
    b = board[-1][-1]
    for i in range(len(board)):
        if board[i][i] != a:
            lrcross = False
    for i in range(len(board),0,-1):
        if board[i][i] != b:
            rlcross = False
    if rlcross or lrcross:
        winner = True

    return winner




def main():
    '''Your main function.  Do NOT change the given code.'''
    dim = int(input("Input dimension of the board: "))
    board = init_board(dim)
    printBoard(board)
    for i in range(1,(dim)+1):
        pass
        #board = addPos("O", i, board)
    addPos("O", 3, board)
    printBoard(board)
    print(checkWinner(board))
    
    

if __name__ == "__main__":
    main()