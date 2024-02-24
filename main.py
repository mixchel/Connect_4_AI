from game import *
from alphaBeta import *
#from aStar import *
import os #poder usar função clear

clear = lambda: os.system('cls') #limpar o terminal do Windows; os.system('clear') para o Linux
new_game = 1 #inicializa um novo jogo, e permite resetar (1) ou quitar (0)


while new_game == 1:
    #iniciando o game loop
    novo_game = game() #inicia um novo objeto game
    turn = 0
    start = novo_game.start() #decide quem começa
    novo_game.drawBoard()
    
    alpha_beta = alphaBeta() #inicia a alphaBeta AI
    #a_star = aStar() #inicia a aStar AI
    

    """Enquanto não houver ganhador ou der empate o jogo continua.
    O ciclo avalia quem começa e progride de acordo.
    Só é necessário imprimir a board para os jogos da AI, pois ela joga logo depois do player."""
    while novo_game.game_winner == EMPTY:
        if start == 0:
        #jogador começa
            if turn % 2 == 0:
                novo_game.playOneTurn()
            else:
                novo_game.putGamePiece(alpha_beta.a_star(), AI_PIECE)
                clear()
                novo_game.drawBoard()

        #a_star começa
        else:
            if turn % 2 == 0:
                novo_game.putGamePiece(alpha_beta.a_star(), AI_PIECE)
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