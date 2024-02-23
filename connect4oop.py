import numpy as np
import os #poder usar função clear

clear = lambda: os.system('cls') #limpar o terminal do Windows; os.system('clear') para o Linux
# def clear():
#    pass

NUM_ROW = 6
NUM_COL = 7
EMPTY = '-'
PLAYER_PIECE = 'X'
AI_PIECE = 'O'

class game:
    game_winner = EMPTY
    
    def __init__(self):
        self.board = np.full([NUM_ROW,NUM_COL],EMPTY)

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
        for i,value in enumerate(self.board[:,collumn]):
            if value == EMPTY: return i
        return


    # def segments(self):
    #     segmentsList = []
    #     for row in self.board:
    #         segmentsList.append(row)
    #     # Coloca as linhas da matriz na lista
    #     for row in np.transpose(self.board):
    #         segmentsList.append(row)
    #     # Coloca as linhas da transposta da matriz na lista, equivalente as colunas da matriz original
    def check_win_after_move(self, move_row, move_col, piece):
        row_count = 0
        for i in range(move_row - 3,move_row + 4):
            if i in range(0,6) and self.board[i][move_col] == piece: row_count += 1
            else: row_count = 0
            if row_count >= 4: return True
        collumn_count = 0
        for j in range(move_col - 3, move_col + 4):
            if j in range(0,7) and self.board[move_row][j] == piece:
                collumn_count += 1
                print("im, here")
            else: collumn_count = 0 
            if collumn_count >= 4: return True
        downrightdiag_count = 0
        for k in range(-3, 4):
            i = move_row + k
            j = move_col + k 
            if i in range(0,6) and j in range(0,7) and self.board[i][j] == piece: downrightdiag_count += 1
            else: downrightdiag_count = 0
            if downrightdiag_count >= 4: return True
        upleftdiag_count = 0
        for k in range(-3, 4):
            i = move_row - k
            j = move_col + k 
            if i in range(0,6) and j in range(0,7) and self.board[i][j] == piece: upleftdiag_count += 1
            else: upleftdiag_count = 0
            if upleftdiag_count >= 4: return True
        return False
    
    """Função que checa se houve vitória após cada movimento."""
    # def check_win_after_move_2(self, move_row, move_col, piece):
        
    #     #verificar se houve vitória na row
    #     row_count = 0 #conta quantas vezes seguidas a peça aparece na row
    #     for i in range(NUM_COL):
    #         if self.board[move_row][i] == piece: 
    #             row_count += 1
    #             if row_count >= 4: 
    #                 return True
    #         else: 
    #             row_count = 0
        
        
    #     #verificar se houve vitória na coluna
    #     col_count = 0 #conta quantas vezes seguidas a peça aparece na coluna
    #     for i in range(NUM_ROW):
    #         if self.board[i][move_col] == piece: 
    #             col_count += 1
    #             if col_count >= 4: 
    #                 return True
    #         else: 
    #             col_count = 0
        
    #     #verificar se houve vitória na diagonal principal e adjacentes
    #     r_diag_count = 0
    #     r_diag_array = []
    #     for k in range(-2,4): #gerar os r_array a partir da diagonal principal
    #         r_diag_array = np.diag(self.board, k) #transforma uma diagonal num array uni-dimensional
    #         for i in range(r_diag_array.size): #verifica cada array pra ver se houve vitória
    #             if r_diag_array[i] == piece:
    #                 r_diag_count += 1
    #                 if r_diag_count >= 4: 
    #                     return True
    #             else: 
    #                 r_diag_count = 0
                    
    #     #verificar se houve vitória na diagonal secundária e adjacentes
    #     l_diag_count = 0
    #     l_diag_array = []
    #     for k in range(-2,4): #gerar os r_array a partir da diagonal principal
    #         l_diag_array = np.diag(np.fliplr(self.board), k) #dá flip no array e verifica as diagonais principais do array flipado
    #         for i in range(l_diag_array.size): #verifica cada array pra ver se houve vitória
    #             if l_diag_array[i] == piece:
    #                 l_diag_count += 1
    #                 if l_diag_count >= 4: 
    #                     return True
    #             else: 
    #                 l_diag_count = 0
                    
    #     return False
    
    #função que decide quem começa o jogo
    def start(self):
        who_starts = int(input("\nType 0 to begin or 1 to go second:"))
        if (who_starts != 0) and (who_starts != 1):
            self.start()
        return who_starts
    
    #Granda AI
    def a_star(self):
        self.putGamePiece(0, AI_PIECE) #granda ai
        return
    
#inicializa um novo jogo, e permite resetar (1) ou quitar (0)
new_game = 1

while new_game == 1:
    #iniciando o game loop
    novo_game = game() #inicia um novo objeto game
    turn = 0
    start = novo_game.start() #decide quem começa
    novo_game.drawBoard()

    """Enquanto não houver ganhador ou der empate o jogo continua.
    O ciclo avalia quem começa e progride de acordo.
    Só é necessário imprimir a board para os jogos da AI, pois ela joga logo depois do player."""
    while novo_game.game_winner == EMPTY:
        if start == 0:
        #jogador começa
            if turn % 2 == 0:
                novo_game.playOneTurn()
            else:
                novo_game.a_star()
                clear()
                novo_game.drawBoard()

        #a_star começa
        else:
            if turn % 2 == 0:
                novo_game.a_star()
                clear()
                novo_game.drawBoard()
            else:
                novo_game.playOneTurn()

        turn += 1 #incrementar o turno

    #não importa quem jogou por último, o output é limpo e redesenhado
    clear()
    novo_game.drawBoard()

    if novo_game.game_winner == "It's a tie!": #empate
        print(f"\n{novo_game.game_winner}")
    else:
        print(f"\n{novo_game.game_winner} Won!") #vitória
    
    new_game = int(input("\nType 0 to quit or 1 to play again: ")) #escolher se vai haver novo jogo

quit()