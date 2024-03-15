from game import *
import copy
import numpy as np


class ai_aStar:
    def __init__(self, is_FST_player) -> None:
        if is_FST_player:
            self.ai_piece = FST_PIECE
            self.oponent_piece = SND_PIECE
            self.heuristics_signal = -1 # As funções que calculam heuristica esperam que a peça da AI seja SND_PIECE, portanto pra alterar o valor, caso a AI jogue primeiro, multiplicamos por -1
        else:
            self.ai_piece = SND_PIECE
            self.oponent_piece = FST_PIECE
            self.heuristics_signal = 1
    def get_move(self, state):

        actions = []
        heuristic = []
        for action in state.availableCollumns():
            new_state = copy.deepcopy(state)
            new_state.putGamePiece(action, self.oponent_piece)
            if new_state.game_winner != EMPTY:
                return heuristic, action
            
        for action in state.availableCollumns():
            new_state = copy.deepcopy(state)
            new_state.putGamePiece(action, self.ai_piece)
            actions.append(action)
            heuristic.append(self.heuristics_signal * sum(new_state.segment_heuristics))
        index_min = np.argmin(heuristic)
        print(heuristic, actions)
        return heuristic, actions[index_min]
