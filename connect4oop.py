import numpy as np

NUM_ROW = 6
NUM_COL = 7
EMPTY = "-"

class game:
    turn = 0
    def __init__(self):
        self.board = np.full([NUM_ROW,NUM_COL],EMPTY)
    def printBoard(self):
        print(self.board)
    def playOneTurn(self):
        self.printBoard()
        available = game.availableRows()
        row = int(input("Choose in which collumn do you wanna play"))
        while row not in available:
            row = input("The collumn you selected is either full or invalid, choose another one")
    def putGamePiece(self, collumn):
        pass
    def availableRows(self):
        available = []
        for i,value in enumerate(self.board[0]):
            if value == EMPTY: available.append(i) 
        return available