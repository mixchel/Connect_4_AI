from game import *
import numpy as np
import copy

class ai_miniMax:
    def __init__(self, is_FST_player):
        if is_FST_player:
            self.ai_piece = FST_PIECE
            self.oponent_piece = SND_PIECE
            self.heuristics_signal = -1
        else:
            self.ai_piece = SND_PIECE
            self.oponent_piece = FST_PIECE
            self.heuristics_signal = 1


    def get_move(self, i_state, depth=5):
        state = copy.deepcopy(i_state)
        if depth == 0:
            return self.heuristics_signal * sum(state.segment_heuristics), None
        
        if state.terminal():
            return state.utility(), None

        if state.player() == self.oponent_piece:
            v = -np.infty
            move = None
            for action in state.availableCollumns():
                new_state = copy.deepcopy(state)  
                new_state.putGamePiece(action, self.oponent_piece) 
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
                new_state.putGamePiece(action, self.ai_piece) 
                test = self.get_move(new_state, depth - 1)[0]
                if test < v:
                    v = test 
                    move = action
            return v, move
