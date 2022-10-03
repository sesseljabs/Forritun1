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
            if j != "X" or j != "O":
                return False
    else:
        return True

# check if someone has won the game
def checkWinner(board):
    pass



def main():
    '''Your main function.  Do NOT change the given code.'''
    dim = int(input("Input dimension of the board: "))
    board = init_board(dim)
    printBoard(board)
    
    

if __name__ == "__main__":
    main()