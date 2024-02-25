from game import *
import numpy as np
import copy

"""
Está com um "problema". Quando a IA sabe que já vai ganhar ela empata a vitoria. Acho que é comum, mas convem ver forma de alterar (?)

"""

class minimax:
    def __init__(self):
        pass


    def get_move(self, i_state, depth=3):
        state = copy.deepcopy(i_state)
        if depth == 0:
            return state.evaluate_all(), None
        if state.terminal():
            return state.utility(), None

        if state.player() == PLAYER_PIECE:
            v = -np.infty
            move = None
            for action in state.availableCollumns():
                new_state = copy.deepcopy(state)  
                new_state.putGamePiece(action, PLAYER_PIECE) 
                test = self.get_move(new_state, depth - 1)[0]
                if test > v:
                    v = test 
                    move = action
            return v, move
        
        else:
            v = np.infty
            move = None
            for action in state.availableCollumns():
                new_state = copy.deepcopy(state)  
                new_state.putGamePiece(action, AI_PIECE) 
                test = self.get_move(new_state, depth - 1)[0]
                if test < v:
                    v = test 
                    move = action
            return v, move
