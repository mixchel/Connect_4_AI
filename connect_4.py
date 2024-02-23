import numpy as np

NUM_ROW = 6
NUM_COL = 7

#cria a board 6 por 7
def reset_board():
    board =np.zeros((NUM_ROW,NUM_COL))
    return board

def draw_board(board):
    print(np.flip(board, 0))

#movimento do jogador
def player_move():
    move = int(input("Insira numero de 0 a 6\n"))
    return move

#criar a A* ai e fazer o movimento dela
def a_star():
    #return move
    pass

#verificar se o jogo acabou, e quem ganhou, ou se for empate
def check_win(board):
    return False

#retorna se o movimento é valido
def valid_move(board, move):
    return board[NUM_ROW-1][move] == 0

#retorna a proxima row valida dentro da coluna
def get_row(board, move):
    for i in range (NUM_ROW):
        if board[i][move] == 0:
            return i
        
#função recursiva que só continua se o movimento do jogador for válido
def make_move(board, move):
    while valid_move(board,move) == False:
        print("movimento invalido")
        move = player_move()
        make_move(board, move)
    
    #caso seja valido, verificar prox coluna e alterar a board
    row = get_row(board,move)
    board[row][move] = 1
    return

#iniciando o game loop com uma nova board e turno 0
board = reset_board()
turn = 0
draw_board(board)

while check_win(board) != True: #enquanto não tiver vitória ou empate nao acaba
    #jogador começa
    if turn % 2 == 0:
        col_move = player_move()
        make_move(board, col_move)
    
    #na proxima vez é a ai, e assim por diante
    else:
        #move = a_star()
        move = 0
        #tem que verificar se o movimento da ai é valido mas ok
        row = get_row(board,move)
        board[row][move] = 2
        
    draw_board(board)
    turn = turn + 1