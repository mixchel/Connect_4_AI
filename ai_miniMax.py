from game import *
import numpy as np
import copy

class ai_miniMax:
    def __init__(self):
        pass


    def get_move(self, i_state, depth=5):
        state = copy.deepcopy(i_state)
        if depth == 0:
            return sum(state.segment_heuristics), None
        
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
