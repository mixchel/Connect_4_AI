#
from game import *
from aStar import *
from minimax import *
from alphaBeta import *
from aStar_rules import *
from aStar_depth import *
from mcts_new import *

import os #poder usar função clear
from sys import platform
import numpy as np
import csv

NUM_GAMES = 10

mini = minimax()
mcts =MonteCarloTreeSearch()
alpha = alphaBeta()

mc =0
mm =0
sav_list=[]


lol = int(input("0 -> mini vs monte; 1 -> monte vs mini; 2-> alpha vs monte; 3 -> monte vs alpha:     "))

def saveResults(res, lol):
    if lol ==0:
        file_name = "mini_v_monte.csv"
    if lol ==1:
        file_name = "monte_v_mini.csv"
    if lol ==2:
        file_name = "alpha_v_monte.csv"
    if lol ==3:
        file_name = "monte_v_alpha.csv"

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(res)
    

if lol==0:

    #Mini v Monte 
    for gg in range(NUM_GAMES):
        novo_game = game()
        #novo_game.start_ai()
        q_t = 0
        act = ""
        while novo_game.terminal() == False:
            q_t = q_t+1
            mini_move = mini.get_move(novo_game)[1]
            novo_game.putGamePiece(mini_move, "X")
            act+=str(mini_move)+"-"
            #novo_game.drawBoard()
            if novo_game.terminal():
                break
            mc_move = mcts.get_move(novo_game)
            if mc_move!= None:
                novo_game.putGamePiece(mc_move, "O")
                act=act+str(mc_move)+"-"
            #novo_game.drawBoard()
        if novo_game.game_winner == "X":
            mm += 1
        if novo_game.game_winner=="O":
            mc +=1
        print("Jogo: ", gg, " Vencedor: ",novo_game.game_winner, " em ", q_t, " jogadas")
        sav_list.append((novo_game.game_winner, q_t, act))

        q_t = 0
        act=""

elif lol==2:

    #Alpha v Monte 
    for gg in range(NUM_GAMES):
        novo_game = game()
        #novo_game.start_ai()
        q_t = 0
        act=""
        while novo_game.terminal() == False:
            q_t = q_t+1
            alpha_move = alpha.get_move(novo_game)[1]
            novo_game.putGamePiece(alpha_move, "X")
            #novo_game.drawBoard()
            act=act+str(alpha_move)+"-"
            if novo_game.terminal():
                break
            mc_move = mcts.get_move(novo_game)
            if mc_move!= None:
                novo_game.putGamePiece(mc_move, "O")
                act= act+str(mc_move)+"-"
            #novo_game.drawBoard()
        if novo_game.game_winner == "X":
            mm += 1
        if novo_game.game_winner=="O":
            mc +=1
        print("Jogo: ", gg, " Vencedor: ",novo_game.game_winner, " em ", q_t, " jogadas")
        sav_list.append((novo_game.game_winner, q_t, act))

        q_t = 0
        act=""

elif lol==3:

    #Monte vs Alpha 
    for gg in range(NUM_GAMES):
        novo_game = game()
        #novo_game.start_ai()
        q_t = 0
        act=""
        while novo_game.terminal() == False:
            q_t = q_t+1
            mc_move = mcts.get_move(novo_game)
            if mc_move!= None:
                novo_game.putGamePiece(mc_move, "X")
                act+=str(mc_move)+"-"
                        #novo_game.drawBoard()
            if novo_game.terminal():
                break
            alpha_move = alpha.get_move(novo_game)[1]
            act+=str(alpha_move)+"-"
            novo_game.putGamePiece(alpha_move, "O")
            #print(mc_move, alpha_move)
            #novo_game.drawBoard()



            #novo_game.drawBoard()
        if novo_game.game_winner == "X":
            mc += 1
        if novo_game.game_winner=="O":
            mm +=1
        print("Jogo: ", gg, " Vencedor: ",novo_game.game_winner, " em ", q_t, " jogadas")
        saveResults([(novo_game.game_winner, q_t,act)], lol=3)
        #sav_list.append((novo_game.game_winner, q_t,act))
        q_t = 0
        act=""
        novo_game.drawBoard()


else:
    #Monte v Mini 
    for gg in range(NUM_GAMES):
        novo_game = game()
        #novo_game.start_ai()
        q_t = 0
        act=""
        while novo_game.terminal() == False:
            q_t = q_t+1
            mc_move = mcts.get_move(novo_game)
            if mc_move!= None:
                novo_game.putGamePiece(mc_move, "X")
                act=str(mc_move)+"-"
            mini_move = mini.get_move(novo_game)[1]
            novo_game.putGamePiece(mini_move, "O")
            act=act+str(mini_move)+"-"
            #novo_game.drawBoard()
            if novo_game.terminal():
                break

            #novo_game.drawBoard()
        if novo_game.game_winner == "O":
            mm += 1
        if novo_game.game_winner=="X":
            mc +=1
        print("Jogo: ", gg, " Vencedor: ",novo_game.game_winner, " em ", q_t, " jogadas")
        sav_list.append((novo_game.game_winner, q_t, act))

        q_t = 0
        act=""
print("Mini/Alpha: ", mm, " Monte: ", mc)

#TODO: GAURDAR OS VENCEDORES E AS JOGADAS NUMA LISTA E SALVAR ESSA LISTA COMO APPEND NUM FICHEIRO PARA FUTUROS TESTES.

