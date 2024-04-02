from game import *
from aStar import *
from minimax import *
from alphaBeta import *
from aStar_rules import *
from aStar_depth import *
from mcts_new import *
import time
import os #poder usar função clear
from sys import platform
import cProfile

def main():
    if platform == "win32":
        clear = lambda: None
    else:
        clear = lambda: os.system('clear')

    new_game = 1 #inicializa um novo jogo, e permite resetar (1) ou quitar (0)


    while new_game == 1: #Jogo contra A*
        #iniciando o game loop
        novo_game = game() #inicia um novo objeto game
        #novo_game.turn = 0
        clear()
        start = novo_game.start_ai()#começa o jogo
        
        if start == 0:
            #a_star = aStar() #inicia a aStar AI
            #a_star_rules = aStar_rules() #inicia aStar_Rules AI
            a_star_depth = aStar_depth()
            
            clear()
            print("vs A*")
            novo_game.drawBoard()
            
            while novo_game.game_winner == EMPTY:
                if novo_game.player() == PLAYER_PIECE:
                #if novo_game.turn % 2 == 0:
                    novo_game.playOneTurn()
                else:
                    #ai_move = a_star.get_move(novo_game)[1] #a_star AI
                    #ai_move = a_star_rules.get_move(novo_game)[1] #a_star_rules AI
                    ti = time.time()
                    ai_move = a_star_depth.get_move(novo_game, 3)
                    if ai_move != None:
                        novo_game.putGamePiece(ai_move,AI_PIECE)
                    clear()
                    print("vs A*")
                    novo_game.drawBoard()
                    print(time.time()-ti)
                #novo_game.turn += 1 #incrementar o turno

        elif (start == 1):
            mini = minimax() #inicia a minimax AI
            
            clear()
            print("vs MiniMax")
            novo_game.drawBoard()
            
            while novo_game.game_winner == EMPTY:
                if novo_game.player() == PLAYER_PIECE:   
                #if novo_game.turn % 2 == 0:
                    novo_game.playOneTurn()
                else:
                    ai_move = mini.get_move(novo_game)[1] #minimax AI
                    if ai_move != None:
                        novo_game.putGamePiece(ai_move,AI_PIECE)
                    clear()
                    print("vs MiniMax")
                    novo_game.drawBoard()
                #novo_game.turn += 1 #incrementar o turno
                    
        elif (start == 3):
            print("Starting game against MCTS")
            mct = MonteCarloTreeSearch() #inicia a Monte Carlo Tree Search AI
            
            clear()
            print("vs MCTS")
            novo_game.drawBoard()
            
            while novo_game.game_winner == EMPTY:
                if novo_game.player() == PLAYER_PIECE:   
                    novo_game.playOneTurn()
                else:
                    ti = time.time()
                    ai_move = mct.get_move(novo_game) #minimax AI
                    if ai_move != None:
                        novo_game.putGamePiece(ai_move,AI_PIECE)
                    print("MCTS played")
                    novo_game.drawBoard()
                    print(time.time()-ti)


        else: #jogo contra alphaBeta
            alpha = alphaBeta() #inicia a alphaBeta AI
            
            clear()
            print("vs AlphaBeta")
            novo_game.drawBoard()
            
            while novo_game.game_winner == EMPTY:      
                if novo_game.player() == PLAYER_PIECE:
                #if novo_game.turn % 2 == 0:
                    novo_game.playOneTurn()
                else:
                    ti = time.time()
                    ai_move = alpha.get_move(novo_game, depth=7)[1] #alphabeta AI
                    if ai_move != None:
                        novo_game.putGamePiece(ai_move,AI_PIECE)
                    clear()
                    print("vs AlphaBeta")
                    novo_game.drawBoard()
                    print(time.time()-ti)
                #novo_game.turn += 1 #incrementar o turno


        #clear() #não importa quem jogou por último, o output é limpo e redesenhado
        novo_game.drawBoard()

        if start == 0 and novo_game.game_winner == 'O':
            print("\nA* Won!")
        elif start == 1 and novo_game.game_winner == 'O':
            print("\nMini-Max Won!")
        elif start == 2 and novo_game.game_winner == 'O':
            print("\nAlphaBeta Won!") #vitória
        elif start==3 and novo_game.game_winner == "O":
            print("\n MCTS Won!")
        elif novo_game.game_winner == 'X':
                print("\nX Won!")
        else:
            print("\nIt's a tie!")
        new_game = int(input("\nType 0 to quit or 1 to play again: ")) #escolher se vai haver novo jogo

    return

cProfile.run("main()")