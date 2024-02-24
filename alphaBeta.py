"""Função que checa se houve vitória após cada movimento."""
    # def check_win_after_move_2(self, move_row, move_col, piece):
        
    #     #verificar se houve vitória na row
    #     row_count = 0 #conta quantas vezes seguidas a peça aparece na row
    #     for i in range(NUM_COL):
    #         if self.board[move_row][i] == piece: 
    #             row_count += 1
    #             if row_count >= 4: 
    #                 return True
    #         else: 
    #             row_count = 0
        
        
    #     #verificar se houve vitória na coluna
    #     col_count = 0 #conta quantas vezes seguidas a peça aparece na coluna
    #     for i in range(NUM_ROW):
    #         if self.board[i][move_col] == piece: 
    #             col_count += 1
    #             if col_count >= 4: 
    #                 return True
    #         else: 
    #             col_count = 0
        
    #     #verificar se houve vitória na diagonal principal e adjacentes
    #     r_diag_count = 0
    #     r_diag_array = []
    #     for k in range(-2,4): #gerar os r_array a partir da diagonal principal
    #         r_diag_array = np.diag(self.board, k) #transforma uma diagonal num array uni-dimensional
    #         for i in range(r_diag_array.size): #verifica cada array pra ver se houve vitória
    #             if r_diag_array[i] == piece:
    #                 r_diag_count += 1
    #                 if r_diag_count >= 4: 
    #                     return True
    #             else: 
    #                 r_diag_count = 0
                    
    #     #verificar se houve vitória na diagonal secundária e adjacentes
    #     l_diag_count = 0
    #     l_diag_array = []
    #     for k in range(-2,4): #gerar os r_array a partir da diagonal principal
    #         l_diag_array = np.diag(np.fliplr(self.board), k) #dá flip no array e verifica as diagonais principais do array flipado
    #         for i in range(l_diag_array.size): #verifica cada array pra ver se houve vitória
    #             if l_diag_array[i] == piece:
    #                 l_diag_count += 1
    #                 if l_diag_count >= 4: 
    #                     return True
    #             else: 
    #                 l_diag_count = 0
                    
    #     return False"""

from game import *

class alphaBeta:
    def __init__(self):
        pass
    
    #def printtest(self, board_state):
    #    print (board_state)
    #    return
    
    def a_star (self):
        return 0