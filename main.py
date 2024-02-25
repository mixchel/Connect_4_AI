from game import *
from aStar import *
from minimax import *
from alphaBeta import *
import os #poder usar função clear

clear = lambda: os.system('cls') #limpar o terminal do Windows; os.system('clear') para o Linux
new_game = 1 #inicializa um novo jogo, e permite resetar (1) ou quitar (0)


while new_game == 1:
    #iniciando o game loop
    novo_game = game() #inicia um novo objeto game
    novo_game.turn = 0
    clear()
    start = novo_game.start()#começa o jogo
    clear()
    novo_game.drawBoard()
    
    #a_star = aStar() #inicia a aStar AI
    mini = minimax() #inicia a minimax AI
    #alpha = alphaBeta() #inicia a alphaBeta AI
    
    while novo_game.game_winner == EMPTY:
        
        if novo_game.turn % 2 == 0:
            novo_game.playOneTurn()
        else:
            #ai_move = a_star.get_move(novo_game)[1] #a_star AI
            ai_move = mini.get_move(novo_game)[1] #minimax AI
            #ai_move = alpha.get_move(novo_game)[1] #alphabeta AI
            if ai_move != None:
                novo_game.putGamePiece(ai_move,AI_PIECE)
            clear()
            novo_game.drawBoard()

        novo_game.turn += 1 #incrementar o turno

    clear() #não importa quem jogou por último, o output é limpo e redesenhado
    novo_game.drawBoard()

    if novo_game.game_winner == "It's a tie!": #empate
        print(f"\n{novo_game.game_winner}")
    else:
        print(f"\n{novo_game.game_winner} Won!") #vitória
    
    new_game = int(input("\nType 0 to quit or 1 to play again: ")) #escolher se vai haver novo jogo

quit()