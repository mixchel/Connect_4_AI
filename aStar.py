#Temos que implementar na aula prática, só estou fazendo testes
#classes em Java era mais fácil....

from game import *
class aStar:
    def __init__(self) -> None:
        pass
    
    """testando como fazer o input atraves de classes
    nesse caso, se a primeira coluna não tiver vazia ele retorna 6,
    o que quer dizer "por um x na ultima coluna"
    """
    def test_move(self,board_state):
        if board_state[0][1] != EMPTY:
            return 6