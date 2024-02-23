import numpy as np

NUM_ROW = 6
NUM_COL = 7

#cria a board 6 por 7
def reset_board():
    board =np.zeros((NUM_ROW,NUM_COL))
    return board

#retorna se o movimento é valido
def valid_move(board, move):
    pass

#retorna a proxima row valida dentro da coluna
def get_row(board, move):
    pass

#verificar se o jogo acabou, e quem ganhou, ou se for empate
def check_win():
    pass

#movimento do jogador
def player_move():
    #tem que alterar a variavel board
    pass

#criar a A* ai e fazer o movimento dela
def a_star():
    #tem que alterar a variavel board
    pass


board = reset_board()

#um loop que é basicamente o jogo lol

print(board)