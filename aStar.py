#Temos que implementar na aula prática, só estou fazendo testes
#classes em Java era mais fácil....

from game import *
import copy
import numpy as np
class aStar:
    def __init__(self) -> None:
        pass
    
    """testando como fazer o input atraves de classes
    nesse caso, se a primeira coluna não tiver vazia ele retorna 6,
    o que quer dizer "por um x na ultima coluna"
    """
    def get_move(self, state):
        actions = []
        heuristic = []
        for action in state.availableCollumns():
            new_state = copy.deepcopy(state)
            new_state.putGamePiece(action, "X")
            actions.append(action)
            heuristic.append(new_state.evaluate_all())
        index_min = np.argmin(heuristic)
        print(heuristic, actions)
        return actions[index_min]


