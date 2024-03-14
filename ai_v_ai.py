from game import *
from aStar import *
from minimax import *
from alphaBeta import *
from aStar_rules import *
from aStar_depth import *
from mtcs2 import *
import os #poder usar função clear
from sys import platform


mini = minimax()
mcts =MonteCarloTreeSearch()
alpha = alphaBeta()

mc =0
mm =0

lol = int(input("0 -> mini first; 1 -> monte first; 2-> monte vs alpha:     "))

if lol==0:

    #Mini v Monte 
    for gg in range(10):
        novo_game = game()
        #novo_game.start_ai()
        q_t = 0
        while novo_game.terminal() == False:
            q_t = q_t+1
            mini_move = mini.get_move(novo_game)[1]
            novo_game.putGamePiece(mini_move, "X")
            #novo_game.drawBoard()
            if novo_game.terminal():
                break
            mc_move = mcts.get_move(novo_game)
            if mc_move!= None:
                novo_game.putGamePiece(mc_move, "O")
            #novo_game.drawBoard()
        if novo_game.game_winner == "X":
            mm += 1
        if novo_game.game_winner=="O":
            mc +=1
        print("Jogo: ", gg, " Vencedor: ",novo_game.game_winner, " em ", q_t, " jogadas")
        q_t = 0

elif lol==2:

    #Alpha v Monte 
    for gg in range(10):
        novo_game = game()
        #novo_game.start_ai()
        q_t = 0
        while novo_game.terminal() == False:
            q_t = q_t+1
            alpha_move = alpha.get_move(novo_game)[1]
            novo_game.putGamePiece(alpha_move, "X")
            #novo_game.drawBoard()
            if novo_game.terminal():
                break
            mc_move = mcts.get_move(novo_game)
            if mc_move!= None:
                novo_game.putGamePiece(mc_move, "O")
            #novo_game.drawBoard()
        if novo_game.game_winner == "X":
            mm += 1
        if novo_game.game_winner=="O":
            mc +=1
        print("Jogo: ", gg, " Vencedor: ",novo_game.game_winner, " em ", q_t, " jogadas")
        q_t = 0

else:
    #Monte v Mini 
    for gg in range(4):
        novo_game = game()
        #novo_game.start_ai()
        q_t = 0
        while novo_game.terminal() == False:
            q_t = q_t+1
            mc_move = mcts.get_move(novo_game)
            if mc_move!= None:
                novo_game.putGamePiece(mc_move, "X")
            mini_move = mini.get_move(novo_game)[1]
            novo_game.putGamePiece(mini_move, "O")
            #novo_game.drawBoard()
            if novo_game.terminal():
                break

            #novo_game.drawBoard()
        if novo_game.game_winner == "O":
            mm += 1
        if novo_game.game_winner=="X":
            mc +=1
        print("Jogo: ", gg, " Vencedor: ",novo_game.game_winner, " em ", q_t, " jogadas")
        q_t = 0
print("Mini: ", mm, " Monte: ", mc)
