from game import *
import numpy as np
import copy

class alphaBeta:
    def __init__(self):
      pass
      
    def get_move(self, state, depth=5, alpha=-np.infty, beta=np.infty):
        pl = state.player()
        if depth == 0:
            s = sum(state.segment_heuristics)
            
            if pl == "X":
                s += 16
            elif pl == "O":
                s -= 16
            return s, None

        if state.terminal():
            return state.utility(), None

        if pl == "X":
            v = -np.infty
            move = None
            for action in state.availableCollumns():
                new_state = copy.deepcopy(state)  # Assume que a classe game tem o método copy() para criar uma cópia do estado
                new_state.putGamePiece(action, "X")
                test = self.get_move(new_state, depth - 1, alpha, beta)[0]
                if test > v:
                    v = test
                    move = action
                if v > beta:
                    break
                alpha = max(alpha, v)
            return v, move
        else:
            v = np.infty
            move = None
            for action in state.availableCollumns():
                new_state =  copy.deepcopy(state)  # Assume que a classe game tem o método copy() para criar uma cópia do estado
                new_state.putGamePiece(action, "O")
                test = self.get_move(new_state, depth - 1, alpha, beta)[0]
                if test < v:
                    v = test
                    move = action
                if v < alpha:
                    break
                beta = min(beta, v)
            return v, move
