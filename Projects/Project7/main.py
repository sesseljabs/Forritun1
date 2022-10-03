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

# check if someone has won the game
def checkWinner(board):
    winner = True
    usr = ""
    # check each row
    for i in range(len(board)):
        if board[i][0]=="X" or board[i][0]=="O":
            s = board[i][0]
            for j in range(1,len(board)):
                if not s == board[i][j]:
                    winner = False
            if winner:
                usr = s
                    
    
    # check each column
    if False == True:
        for i in range(len(board)):
            if board[0][i]=="X" or board[0][i]=="O":
                s = board[0][i]

                for j in range(1,len(board)):
                    if not s == board[j][i]:
                        winner = False


    return winner




def main():
    '''Your main function.  Do NOT change the given code.'''
    dim = int(input("Input dimension of the board: "))
    board = init_board(dim)
    printBoard(board)
    for i in range(1,(dim*dim)+1):
        pass
        #board = addPos("O", i, board)
    #addPos("O", 3, board)
    printBoard(board)
    print(checkWinner(board))
    
    

if __name__ == "__main__":
    main()