import numpy as np

NUM_ROW = 6
NUM_COL = 7
EMPTY = '-'
PLAYER_PIECE = 'X'
AI_PIECE = 'O'
NUM_MOVES = NUM_ROW * NUM_COL - 1 #temporário até fazer funcionar usando as funçoes desta classe

class game:
    game_winner = EMPTY
    board_is_full = False
    
    def __init__(self):
        self.board = np.full([NUM_ROW,NUM_COL],EMPTY)

    def get_state(self):
        return self.board
        
    def drawBoard(self):
        print(np.flip(self.board, 0))
        return
    
    """Dado um input, verifica a função availableCollumns para saber se é válido.
    Se não for pede novamente o input, do contrário usa a função putGamePiece para alterar a board."""
    def playOneTurn(self):
        available = self.availableCollumns()
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
        elif not self.availableCollumns(): board_is_full = True # Isso muda board_is_full pra True se a lista de colunas com movimentos possiveis estiver vazia
        # not list aparentemente é um dos jeitos mais eficientes de checar se uma lista está vazia, python é estranho
        return
    
    """Checa a última row para saber quais colunas não estão cheias. Retorna a lista de colunas."""
    def availableCollumns(self):
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
            if row_count == 4: return True
        
        #verificar se houve vitória na coluna
        collumn_count = 0
        for j in range(move_col - 3, move_col + 4):
            if j in range(NUM_COL) and self.board[move_row][j] == piece:
                collumn_count += 1
            else: collumn_count = 0 
            if collumn_count == 4: return True
            
        #verificar se houve vitória na diagonal principal e adjacentes
        downrightdiag_count = 0
        for k in range(-3, 4):
            i = move_row + k
            j = move_col + k 
            if i in range(NUM_ROW) and j in range(NUM_COL) and self.board[i][j] == piece: downrightdiag_count += 1
            else: downrightdiag_count = 0
            if downrightdiag_count == 4: return True
            
        #verificar se houve vitória na diagonal secundária e adjacentes
        upleftdiag_count = 0
        for k in range(-3, 4):
            i = move_row - k
            j = move_col + k 
            if i in range(NUM_ROW) and j in range(NUM_COL) and self.board[i][j] == piece: upleftdiag_count += 1
            else: upleftdiag_count = 0
            if upleftdiag_count == 4: return True
        return False
    
    #função que decide quem começa o jogo
    def start(self):
        who_starts = int(input("\nType 0 to begin or 1 to go second:"))
        if (who_starts != 0) and (who_starts != 1):
            self.start()
        return who_starts
    
    def movelist_2_board(self, moves): # assumes game starts with playerPiece
        nextPiece = PLAYER_PIECE
        oldPiece = AI_PIECE
        for move in moves:
            if not self.board_is_full and move in self.availableCollumns():
                self.putGamePiece(move, nextPiece)
                nextPiece, oldPiece = oldPiece, nextPiece

    def get_segments(self):
        segments = []

        #Verifica linhas e colunas
        for i in range(NUM_ROW):
            line = self.board[i]
            for j in range(4):
                segments.append(line[j:j+4])
            col = self.board[:,i]
            for j in range(3):
                segments.append(col[j:j+4])
        
        #Verifica a ultima coluna
        col = self.board[:, NUM_COL-1]
        for j in range(3):
            segments.append(col[j:j+4])
        
        #Verifica as diagonais principais
        for i in range(-2,4):
            dia = np.diag(self.board,i)
            for j in range(len(dia)-3):
                segments.append(dia[j:j+4])
        #Dá flip no array e verifica as diagonais principais do array flipado (equivalentes às diagonais perpendiculares às principais do array original)
        state_tr = np.fliplr(self.board)
        for i in range(-2,4):
            dia = np.diag(state_tr,i)
            for j in range(len(dia)-3):
                segments.append(dia[j:j+4])
            
        
        return segments

    def evaluate(self, segment):
        cx = 0
        co = 0
        for i in segment:
            if i== PLAYER_PIECE:
                cx+=1
            elif i== AI_PIECE:
                co+=1

        # print(cx, co)
        if (cx==0 and co==0) or (cx>0 and co>0):
            return 0
        elif cx == 1:
            return 1
        elif cx == 2:
            return 10
        elif cx==3:
            return 50
        
        #   VERIFICAR ISTO
        elif cx == 4:
            return 512
        elif co ==4:
            return -512
        # ---

        elif co == 1:
            return -1
        elif co == 2:
            return -10
        elif co==3:
            return -50
        
    def evaluate_all(self):

        win = self.ganho()
        if win ==PLAYER_PIECE:
            return 512
        
        elif win ==AI_PIECE:
            return -512
        elif self.terminal():
            return 0
        s = 0
        if self.player()==PLAYER_PIECE:
            s= s+16
        elif self.player()==AI_PIECE:
            s=s-16
        for segment in self.get_segments():
            s=s+self.evaluate(segment)
        return s
    

    def terminal(self):
        """"
        Verifica se um determinado estado é um estado terminal/final 
        (estado em que um dos jogadores ganhou ou em que não há ações possíveis)
        
        """

        #Se houver vencedor o jogo acaba
        if self.ganho():
            return True
        
        #Se não houverem ações disponiveis o jogo acaba
        elif len(self.availableCollumns())==0:
            return True
        else:
            return False
    
    def ganho(self):
        """
        Recebe um estado e retorna o vencedor (no caso deste existir)
        
        """

        #Itera sobre todos os segmentos de tamanho 4 e verifica se há condição de vencedor
        for segment in self.get_segments():
            if np.array_equal(segment, ['X', 'X', 'X', 'X']):
                return "X"
            elif np.array_equal(segment, ['O', 'O', 'O', 'O']):
                return "O"
        return None
    
    def player(self):
        """
        Recebe um estado e retorna o jogador nesse turno.

        """


        cx = 0 #contador de X
        co = 0 #contador de O
        for i in range(6):
            a = self.board[i]
            for j in range(7):
                b = a[j]
                if b == PLAYER_PIECE:
                    cx +=1
                elif b == AI_PIECE:
                    co +=1
        #caso do tabuleiro estar completamente ocupado
        if cx+co == NUM_COL*NUM_ROW:
            return None
        
        #Se o número de X's for menor ou igual ao numéro de O's, então é a vez de X jogar.
        if cx <=co:
            return PLAYER_PIECE
        else:
            return AI_PIECE
        
    def utility(self):
        win = self.ganho()
        if win == PLAYER_PIECE:
            return 512
        elif win == AI_PIECE:
            return -512
        else:
            return 0