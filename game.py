import numpy as np

NUM_ROW = 6
NUM_COL = 7
EMPTY = '-'
PLAYER_PIECE = 'X'
AI_PIECE = 'O'

class game:
    game_winner = EMPTY
    
    def __init__(self):
        self.board = np.full([NUM_ROW,NUM_COL],EMPTY)

    def get_state(self):
        return self.board
        
    def drawBoard(self):
        print(np.flip(self.board, 0))
        return
    
    """Dado um input, verifica a função availableRows para saber se é válido.
    Se não for pede novamente o input, do contrário usa a função putGamePiece para alterar a board."""
    def playOneTurn(self):
        available = self.availableRows()
        collumn = int(input("Choose in which collumn do you wanna play: "))
        while collumn not in available:
            collumn = int(input("The collumn you selected is either full or invalid, choose another one: "))
        self.putGamePiece(collumn, PLAYER_PIECE)
        return
    
    """Verifica a função nextEmptyRowinCollumn para saber qual a próxima row vazia.
    Alterar a board dado a coluna e a qual das peças (AI ou Player) será usada e põe na row vazia."""
    def putGamePiece(self, collumn, piece):
        piece_placement = self.nextEmptyRowinCollumn(collumn)
        self.board[piece_placement][collumn] = piece
        if self.check_win_after_move(piece_placement, collumn, piece): self.game_winner = piece
        return
    
    """Checa a última row para saber quais colunas não estão cheias. Retorna a lista de colunas."""
    def availableRows(self):
        available = []
        for i,value in enumerate(self.board[NUM_ROW - 1]):
            if value == EMPTY: available.append(i) 
        return available
    
    """Dado uma coluna, verifica qual a próxima row vazia. Retorna o número da row."""
    def nextEmptyRowinCollumn(self, collumn):
        #for i in range(NUM_ROW):
        #    if self.board[i][collumn] == EMPTY:
        #        return i
        for i,value in enumerate(self.board[:,collumn]):
            if value == EMPTY: return i
        return

    # sla o que o michel queria fazer aqui
    # def segments(self):
    #     segmentsList = []
    #     for row in self.board:
    #         segmentsList.append(row)
    #     # Coloca as linhas da matriz na lista
    #     for row in np.transpose(self.board):
    #         segmentsList.append(row)
    #     # Coloca as linhas da transposta da matriz na lista, equivalente as colunas da matriz original
    
    """Função que checa se houve vitória após cada movimento. 
    Verifica somente os arrays que contém o a peça em [move_row, move_col]."""
    def check_win_after_move(self, move_row, move_col, piece):
        #verificar se houve vitória na row
        row_count = 0
        for i in range(move_row - 3,move_row + 4):
            if i in range(0,NUM_ROW) and self.board[i][move_col] == piece: row_count += 1
            else: row_count = 0
            if row_count >= 4: return True
        
        #verificar se houve vitória na coluna
        collumn_count = 0
        for j in range(move_col - 3, move_col + 4):
            if j in range(NUM_COL) and self.board[move_row][j] == piece:
                collumn_count += 1
            else: collumn_count = 0 
            if collumn_count >= 4: return True
            
        #verificar se houve vitória na diagonal principal e adjacentes
        downrightdiag_count = 0
        for k in range(-3, 4):
            i = move_row + k
            j = move_col + k 
            if i in range(NUM_ROW) and j in range(NUM_COL) and self.board[i][j] == piece: downrightdiag_count += 1
            else: downrightdiag_count = 0
            if downrightdiag_count >= 4: return True
            
        #verificar se houve vitória na diagonal secundária e adjacentes
        upleftdiag_count = 0
        for k in range(-3, 4):
            i = move_row - k
            j = move_col + k 
            if i in range(NUM_ROW) and j in range(NUM_COL) and self.board[i][j] == piece: upleftdiag_count += 1
            else: upleftdiag_count = 0
            if upleftdiag_count >= 4: return True
        return False
    
    #função que decide quem começa o jogo
    def start(self):
        who_starts = int(input("\nType 0 to begin or 1 to go second:"))
        if (who_starts != 0) and (who_starts != 1):
            self.start()
        return who_starts
