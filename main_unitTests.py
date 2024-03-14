from game import *
from ai_aStar import *
from ai_miniMax import *
from ai_alphaBeta import *
import os #poder usar função clear
from sys import platform

clear = lambda: None
new_game = 1 #inicializa um novo jogo, e permite resetar (1) ou quitar (0)

ai = ai_aStar()
ai = ai_miniMax()
ai = ai_alphaBeta()

def show_heuristics(dgame):
    old = [dgame.evaluate(segment) for segment in dgame.get_segments()]
    print(old)
    print(dgame.segment_heuristics)

def aiMove():
    novo_game.drawBoard()
    print("Next to play: AI Name\n")
    ai_move = ai.get_move(novo_game)[1]
    if ai_move != None:
        novo_game.putGamePiece(ai_move,AI_PIECE)
    #show_heuristics(novo_game)
    #clear()
    
def start_ai():
        starts = int(input("\nChoose which AI to play against: 0 = A*; 1 = mini-max; 2 = AlphaBeta: "))
        if starts not in range(3):
            start_ai()
        return starts
    

    


while new_game == 1: #Jogo contra A*
    #iniciando o game loop
    novo_game = game() #inicia um novo objeto game
    #novo_game.turn = 0
    clear()
    start = novo_game.start_ai()#começa o jogo
    
    if start == 0:
        aStar = ai_aStar() #inicia a aStar AI
        
        clear()
        print("vs A*")
        novo_game.drawBoard()
        
        while novo_game.game_winner == EMPTY:
            if novo_game.player() == PLAYER_PIECE:
            #if novo_game.turn % 2 == 0:
                novo_game.playOneTurn()
            else:
                ai_move = aStar.get_move(novo_game)[1] #a_star AI
                if ai_move != None:
                    novo_game.putGamePiece(ai_move,AI_PIECE)
                clear()
                print("vs A*")
                novo_game.drawBoard()
                show_heuristics(novo_game)
            #novo_game.turn += 1 #incrementar o turno

    elif (start == 1):
        mini = ai_miniMax() #inicia a minimax AI
        
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

    else: #jogo contra alphaBeta
        alpha = ai_alphaBeta() #inicia a alphaBeta AI
        
        #clear()
        
        while novo_game.game_winner == EMPTY:      
            if novo_game.player() == PLAYER_PIECE:
                novo_game.drawBoard()
                print("Next to play: Player\n")
                novo_game.playOneTurn()
            else:
                aiMove()

    #clear() #não importa quem jogou por último, o output é limpo e redesenhado
    novo_game.drawBoard()

    if start == 0 and novo_game.game_winner == 'O':
        print("\nA* Won!")
    elif start == 1 and novo_game.game_winner == 'O':
        print("\nMini-Max Won!")
    elif start == 2 and novo_game.game_winner == 'O':
        print("\nAlphaBeta Won!") #vitória
    elif novo_game.game_winner == 'X':
            print("\nX Won!")
    else:
        print("\nIt's a tie!")
    new_game = int(input("\nType 0 to quit or 1 to play again: ")) #escolher se vai haver novo jogo

quit()


