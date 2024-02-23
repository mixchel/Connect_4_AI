import numpy as np

NUM_ROW = 6
NUM_COL = 7
EMPTY = '-'
PLAYER_PIECE = 'X'

class game:
    game_winner = EMPTY
    def __init__(self):
        self.board = np.full([NUM_ROW,NUM_COL],EMPTY)

    def drawBoard(self):
        print(np.flip(self.board, 0))
        return
    
    def playOneTurn(self):
        available = self.availableRows()
        collumn = int(input("Choose in which collumn do you wanna play"))
        while collumn not in available:
            collumn = int(input("The collumn you selected is either full or invalid, choose another one"))
        self.putGamePiece(collumn, PLAYER_PIECE)
        return
    
    def putGamePiece(self, collumn, piece):
        piece_placement = self.nextEmptyRowinCollumn(collumn)
        self.board[piece_placement][collumn] = piece
        if self.check_win_after_move(piece_placement, collumn, piece): game_winner = piece
             
        

    
    def availableRows(self):
        available = []
        for i,value in enumerate(self.board[5]):
            if value == EMPTY: available.append(i) 
        return available
    
    def nextEmptyRowinCollumn(self, collumn):
        for i,value in enumerate(self.board[:,collumn]):
            if value == EMPTY: return i

    # def segments(self):
    #     segmentsList = []
    #     for row in self.board:
    #         segmentsList.append(row)
    #     # Coloca as linhas da matriz na lista
    #     for row in np.transpose(self.board):
    #         segmentsList.append(row)
    #     # Coloca as linhas da transposta da matriz na lista, equivalente as colunas da matriz original
    def check_win_after_move(self, moverow, movecollumn, piece):
        for i in range(moverow - 3,moverow + 4):
            if i in range(0,6) and self.board[i][movecollumn] == piece: count += 1
            else: count = 0
        if count >= 4: return True
        count = 0
        for j in range(movecollumn - 3, movecollumn + 4):
            if j in range(0,7) and self.board[moverow][j] == piece: count += 1
            else: count = 0  
        if count >= 4: return True
        for k in range(-3, 4):
            i = moverow + k
            j = movecollumn + k 
            if i in range(0,6) and j in range(0,6) and self.board[i][j] == piece: count += 1
            else: count = 0
        if count >= 4: return True
        for k in range(-3, 4):
            i = moverow - k
            j = movecollumn + k 
            if i in range(0,6) and j in range(0,6) and self.board[i][j] == piece: count += 1
            else: count = 0
        if count >= 4: return True
        return False
    