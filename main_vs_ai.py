from game import *
from ai_aStar import *
from ai_miniMax import *
from ai_alphaBeta import *
from ai_mcts_test import *
import time #calcular tempo de execução
import os #poder usar função clear
from sys import platform #identificar plataforma

CLEAR_TERMINAL = False #define se o terminal sera limpo ou não
NUM_GAMES = 5 #define o numero de jogos a serem jogados

if platform == "win32":
    clear = lambda: os.system('cls') #limpar o terminal do Windows; os.system('clear') para o Linux
else:
    clear = lambda: os.system('clear')

def clearTerminal():
    if CLEAR_TERMINAL:
        clear()
    
def aiMove_1(): #movimento da ai 1
    ai_move = ai_1.get_move(novo_game)[1]
    if ai_move != None:
        novo_game.putGamePiece(ai_move,PLAYER_PIECE)
        print("||"*10)

def aiMove_2(): #movimento da ai 2
    ai_move = ai_2.get_move(novo_game)[1]
    if ai_move != None:
        novo_game.putGamePiece(ai_move,AI_PIECE)
        print(ai_move)
        print("||"*10)
def start_ai(): #inicializa a AI 1
    start = -1 # error handling
    while start not in range(4):
        try:  
            start = int(input("\nChoose the AI => 0 = A*, 1 = Mini Max, 2 = Alpha Beta, 3 = MTC: "))
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
            aiName = "MTC"
    return ai,aiName

#-------- Game Loop --------

start = start_ai() #primeira ai
ai_1 = start[0]
ai_1_Name = start[1]
ai_1_wins = 0

start = start_ai() #segunda ai
ai_2 = start[0]
ai_2_Name = start[1]
ai_2_wins = 0

for i in range(1, NUM_GAMES + 1):
    clearTerminal()
    novo_game = game() #inicia um novo objeto game
    print(f"\nGame {i}\n")
        
    count_moves = 0
    while novo_game.game_winner == EMPTY:
        if novo_game.player() == PLAYER_PIECE:
            count_moves += 1
            aiMove_1()
            #novo_game.drawBoard()
        else:
            count_moves += 1
            aiMove_2()
            #novo_game.drawBoard()

    novo_game.drawBoard()

    if novo_game.game_winner == PLAYER_PIECE:
        ai_1_wins += 1
        print(f"\n{ai_1_Name} Won in {count_moves} moves!")
    elif novo_game.game_winner == AI_PIECE:
        ai_2_wins += 1
        print(f"\n{ai_2_Name} Won in {count_moves} moves!")
    else:
        print(f"\nIt's a tie in {count_moves} moves!")
        
print(f"\nResult:\n{ai_1_Name}: {ai_1_wins} vs {ai_2_Name}: {ai_2_wins}")
    
quit()


