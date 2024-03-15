""" 
Falta ainda implementar os testes sequenciais e poder escolher a board.
Agora a AI pode começar mas ainda está com problemas.
Falta adicionar o arquivo do MTC e deletar o comentário em start_ai quando fizer.
Se quiser que o terminal seja limpo durante o jogo é só mudar o valor da variável
    CLEAR_TERMINAL para True.
"""

from game import *
from ai_aStar import *
from ai_miniMax import *
from ai_alphaBeta import *
import os #poder usar função clear
from sys import platform #identificar plataforma

#FST_PIECE = "X"
#SND_PIECE = "O"
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
    
def aiMove(ai_piece): #movimento da ai
    novo_game.drawBoard()
    print(f"Next to play: {aiName}\n")
    ai_move = ai.get_move(novo_game)[1]
    if ai_move != None:
        novo_game.putGamePiece(ai_move,ai_piece)
    #show_heuristics(novo_game)
    clearTerminal()
    
def start_ai(is_FST_player): #inicializa a AI escolhida
    start = -1 # error handling
    while start not in range(4):
        try:  
            start = int(input("\nChoose which AI to play against: 0 = A*, 1 = Mini Max, 2 = Alpha Beta, 3 = MTC: "))
        except:
            continue
    match start:
        case 0:
            ai = ai_aStar(is_FST_player)
            aiName = "A*"
        case 1:
            ai = ai_miniMax(is_FST_player)
            aiName = "Mini Max"
        case 2:
            ai = ai_alphaBeta(is_FST_player)
            aiName = "Alpha Beta"
        case 3:
        #    ai = ai_MTC()
        #    aiName = "MTC"
            print("not implemented")
            quit()
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
    novo_game = game() #inicia um novo objeto game
    clearTerminal()
    print("\nNew Game\n")
    
    if first_player() == 0:
        start = start_ai(False)
        ai_piece = SND_PIECE
        player_piece = FST_PIECE
    else:
        start = start_ai(True)
        ai_piece = FST_PIECE
        player_piece = SND_PIECE
    ai = start[0]
    aiName = start[1]
    
    
        
    clearTerminal()
    while novo_game.game_winner == EMPTY:
        if novo_game.player() == player_piece:
            playerMove()
        else:
            aiMove(ai_piece)

    clearTerminal()
    novo_game.drawBoard()

    if novo_game.game_winner == ai_piece:
        print(f"\n{aiName} Won!")
    elif novo_game.game_winner == player_piece:
            print("\nPlayer Won!")
    else:
        print("\nIt's a tie!")
    NEW_GAME = int(input("\nType 0 to quit or 1 to play again: ")) #escolher se vai haver novo jogo

quit()


