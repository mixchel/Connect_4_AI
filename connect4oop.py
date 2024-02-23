import numpy as np
import os #poder usar função clear

clear = lambda: os.system('cls') #limpar o terminal do Windows; os.system('clear') para o Linux

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
    game = game() #inicia um novo objeto game
    turn = 0
    start = game.start() #decide quem começa
    game.drawBoard()

    """Enquanto não houver ganhador ou der empate o jogo continua.
    O ciclo avalia quem começa e progride de acordo.
    Só é necessário imprimir a board para os jogos da AI, pois ela joga logo depois do player."""
    while game.game_winner == EMPTY: 
        if start == 0:
        #jogador começa
            if turn % 2 == 0:
                game.playOneTurn()
            else:
                game.a_star()
                clear()
                game.drawBoard()

        #a_star começa
        else:
            if turn % 2 == 0:
                game.a_star()
                clear()
                game.drawBoard()
            else:
                game.playOneTurn()

        turn += 1 #incrementar o turno

    #não importa quem jogou por último, o output é limpo e redesenhado
    clear()
    game.drawBoard()

    if game.game_winner == "It's a tie!": #empate
        print(f"\n{game.game_winner}")
    else:
        print(f"\n{game.game_winner} Won!") #vitória
    
    new_game = int(input("\nType 0 to quit or 1 to play again: ")) #escolher se vai haver novo jogo

quit()