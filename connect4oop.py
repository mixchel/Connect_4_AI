import numpy as np

NUM_ROW = 6
NUM_COL = 7
EMPTY = '-'
PLAYER_PIECE = 'X'

class game:
    def __init__(self):
        self.board = np.full([NUM_ROW,NUM_COL],EMPTY)

    def drawBoard(self):
        print(np.flip(self.board, 0))
        return
    
    def playOneTurn(self):
        self.drawBoard()
        available = game.availableRows()
        collumn = int(input("Choose in which collumn do you wanna play"))
        while collumn not in available:
            collumn = int(input("The collumn you selected is either full or invalid, choose another one"))
            print(collumn)
        game.putGamePiece(collumn, PLAYER_PIECE)
        return
    
    def putGamePiece(self, collumn, piece):
        self.board[self.nextEmptyRowinCollumn(collumn)][collumn] = piece
        return
    
    def availableRows(self):
        available = []
        for i,value in enumerate(self.board[5]):
            if value == EMPTY: available.append(i) 
        return available
    
    def nextEmptyRowinCollumn(self, collumn):
        for i,value in enumerate(self.board[:,collumn]):
            if value == EMPTY: return i
    def checkWin(self):
        pass
        