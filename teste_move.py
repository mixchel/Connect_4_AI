from game import *
from aStar import *
from minimax import *
from alphaBeta import *
from aStar_rules import *
from aStar_depth import *
from mctsNextCheck import *
import os #poder usar função clear
from sys import platform
import numpy as np

mc = MonteCarloTreeSearch()

jogo = game()

while not jogo.terminal():
    mc_move = mc.get_move(jogo)
    jogo.putGamePiece(mc_move, "X")
    jogo.drawBoard()
    if jogo.terminal():
        print(jogo.game_winner)
    gg = int(input())
    jogo.putGamePiece(gg, "O")
    #jogo.drawBoard()


jogo.drawBoard()
print(jogo.game_winner)