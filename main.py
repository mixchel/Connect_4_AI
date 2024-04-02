from game import *
from ai_aStar import *
from ai_miniMax import *
from ai_alphaBeta import *
from ai_mcts import *
import time #calcular tempo de execução
import os #poder usar função clear
from sys import platform #identificar plataforma

NEW_GAME = 1 #inicializa um novo jogo, e permite resetar (1) ou quitar (0)
CLEAR_TERMINAL = False #define se o terminal sera limpo ou não

if platform == "win32":
    clear = lambda: os.system('cls') #limpar o terminal do Windows; os.system('clear') para o Linux
else:
    clear = lambda: os.system('clear')

def clearTerminal():
    if CLEAR_TERMINAL:
        clear()

def show_heuristics(dgame):
    old = [dgame.evaluate(segment) for segment in dgame.get_segments()]
    print(old)
    print(dgame.segment_heuristics)

def playerMove(): #movimento do jogador
    novo_game.drawBoard()
    print("Next to play: Player\n")
    novo_game.playOneTurn()
    #show_heuristics(novo_game)
    clearTerminal()
    
def aiMove(): #movimento da ai
    novo_game.drawBoard()
    print(f"Next to play: {aiName}\n")
    ai_move = ai.get_move(novo_game)[1]
    if ai_move != None:
        novo_game.putGamePiece(ai_move,AI_PIECE)
    #show_heuristics(novo_game)
    clearTerminal()
    
def start_ai(): #inicializa a AI escolhida
    start = -1 # error handling
    while start not in range(4):
        try:  
            start = int(input("\nChoose which AI to play against: 0 = A*, 1 = Mini Max, 2 = Alpha Beta, 3 = MTC: "))
        except:
            continue
    match start:
        case 0:
            ai = ai_aStar()
            aiName = "A*"
        case 1:
            ai = ai_miniMax()
            aiName = "Mini Max"
        case 2:
            ai = ai_alphaBeta()
            aiName = "Alpha Beta"
        case 3:
            ai = MonteCarloTreeSearch()
            #ai = ai_MTC()
            aiName = "MTC"
    return ai,aiName

def first_player(): #decide quem vai primeiro
    try:  # error handling
        first = int(input("\nChoose 0 to go first or 1 to go second: "))
    except:
        first = -1
    if first not in range(2):
        first_player()
    return first

while NEW_GAME == 1: #Iniciando o game loop
     #inicia um novo objeto game
    clearTerminal()
    print("\nNew Game\n")
    
    start = start_ai()
    ai = start[0]
    aiName = start[1]
    if aiName == "MTC":
        novo_game = game(calculate_heuristics=False)
    else:
        novo_game = game()
    
    if first_player() == 0:
        novo_game.first = PLAYER_PIECE
    else:
        novo_game.first = AI_PIECE
        
    clearTerminal()
    while novo_game.game_winner == EMPTY:
        if novo_game.player() == PLAYER_PIECE:
            playerMove()
        else:
            ti = time.time()
            aiMove()
            print(time.time()-ti)

    clearTerminal()
    novo_game.drawBoard()

    if novo_game.game_winner == AI_PIECE:
        print(f"\n{aiName} Won!")
    elif novo_game.game_winner == PLAYER_PIECE:
            print("\nPlayer Won!")
    else:
        print("\nIt's a tie!")
    NEW_GAME = int(input("\nType 0 to quit or 1 to play again: ")) #escolher se vai haver novo jogo

quit()


