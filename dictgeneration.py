#
import numpy as np
NUM_ROW = 6
NUM_COL = 7
def get_segments(board):
        segments = []
        # Verifica linhas e colunas
        for i in range(NUM_ROW):
            line = board[i]
            for j in range(4):
                segments.append(line[j : j + 4])
            col = board[:, i]
            for j in range(3):
                segments.append(col[j : j + 4])

        # Verifica a ultima coluna
        col = board[:, NUM_COL - 1]
        for j in range(3):
            segments.append(col[j : j + 4])

        # Verifica as diagonais principais
        for i in range(-2, 4):
            dia = np.diag(board, i)
            for j in range(len(dia) - 3):
                segments.append(dia[j : j + 4])

        # Dá flip no array e verifica as diagonais principais do array flipado
        # (equivalentes às diagonais perpendiculares às principais do array original)
        state_tr = np.fliplr(board)
        for i in range(-2, 4):
            dia = np.diag(state_tr, i)
            for j in range(len(dia) - 3):
                segments.append(dia[j : j + 4])
        return segments
def gen_dict():
    board = [[f"{i},{j}" for j in range(7)]for i in range(6)]
    board = np.array(board)
    segments = get_segments(board)
    index_dict = {}
    position_dict = {}
    for j in range(7):
        for i in range(6):
            temp = []
            for z,segment in enumerate(segments):
                if f"{i},{j}" in segment:
                    temp.append(z)
                index_dict[(i,j)] = temp
                position_dict[(i,j)] = [[tuple(map(int, pos.split(","))) for pos in segments[index]] for index in temp]
                #position_dict[(i,j)] = [segments[index] for index in temp]
    return index_dict,position_dict
board = [[f"{i},{j}" for j in range(7)]for i in range(6)]
board = np.array(board)
segments = get_segments(board)
#index_dict, position_dict = gen_dict()