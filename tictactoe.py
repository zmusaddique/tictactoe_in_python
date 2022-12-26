theSpaces = list('123456789')
X,O,blank = 'X','O',' '

def main():
    '''Running the game'''
    print('Welcome to the game!')
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))

        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input()
        updateBoard(gameBoard, move, currentPlayer)

        if isWinner(gameBoard, currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')
    print('\n\nCopied with full heart from Automate the boring stuff with Python')
    print('coded by Zmusaddique')


def getBlankBoard():
    board = {}
    for space in theSpaces:
        board[space] = blank
    return board

def getBoardStr(board):
    b = board
    '''For the text representation'''
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(b['1'], b['2'], b['3'],
                                b['4'], b['5'], b['6'],
                                b['7'], b['8'], b['9'])

def isValidSpace(board, space):
    return space in theSpaces and board[space] == blank


def isWinner(board, player):
    b, p = board, player

    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['1'] == b['5'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p))

def isBoardFull(board):
    for space in theSpaces:
        if board[space] == blank:
            return False
    return True

def updateBoard(board, space, mark):
    board[space] = mark

if __name__ == '__main__':
    main()
