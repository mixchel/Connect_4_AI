from game import *
import copy
import numpy as np


class ai_aStar:
    def __init__(self) -> None:
        pass

    def get_move(self, state):

        actions = []
        heuristic = []
        for action in state.availableCollumns():
            new_state = copy.deepcopy(state)
            new_state.putGamePiece(action, "X")
            if new_state.game_winner != EMPTY:
                return heuristic, action
            
        for action in state.availableCollumns():
            new_state = copy.deepcopy(state)
            new_state.putGamePiece(action, "O")
            actions.append(action)
            heuristic.append(sum(new_state.segment_heuristics))
        index_min = np.argmin(heuristic)
        print(heuristic, actions)
        return heuristic, actions[index_min]
