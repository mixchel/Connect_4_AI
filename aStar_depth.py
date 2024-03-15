"""Ainda não está usando as mudanças no dicionário
feitas pelo Michel."""


import copy
import numpy as np

class aStar_depth:
    def __init__(self) -> None:
        pass
    
    def get_move(self, state, depth_limit):
        _, action = self.dfs_with_heuristic(state, 0, depth_limit)
        return action

    def dfs_with_heuristic(self, state, depth, depth_limit):
        
        if depth == depth_limit:
            return self.evaluate_depth(state)

        actions = state.availableCollumns()
        best_heuristic = float('inf')
        best_action = None

        for action in actions:
            new_state = copy.deepcopy(state)
            pl = new_state.player()
            new_state.putGamePiece(action, pl)
            heuristic, _ = self.dfs_with_heuristic(new_state, depth + 1, depth_limit)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_action = action

        return best_heuristic, best_action

    def evaluate_depth(self, state):
        actions = state.availableCollumns()
        heuristic = []
        for action in actions:
            new_state = copy.deepcopy(state)
            new_state.putGamePiece(action, "O")
            heuristic.append(new_state.evaluate_all())
        index_min = np.argmin(heuristic)
        return heuristic[index_min], actions[index_min]


