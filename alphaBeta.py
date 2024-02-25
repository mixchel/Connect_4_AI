from game import *
import numpy as np
import copy

class alphaBeta:
    def __init__(self):
      pass
  
    def get_move(self, state, depth=5, alpha=-np.infty, beta=np.infty):
        pl = state.player()
        if depth == 0:
            segments = state.get_segments()
            s = 0
            for segment in segments:
                s += state.evaluate(segment)
            
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




"""
class alphaBeta:
    def __init__(self):
        pass
    
    def get_segments(self, board_state):
        segments = [] 

        #Verifica as linhas e colunas
        for i in range(6):
            linha = board_state[i]
            for j in range(4):
                segments.append(linha[j:j+4])
            coluna = board_state[:,i]
            for j in range(3):
                segments.append(coluna[j:j+4])

        #Verifica a ultima coluna       
        coluna = board_state[:,6]
        for j in range(3):
            segments.append(coluna[j:j+4])
    
        #Verifica as diagonais principais
        for i in range(-2,4):
            diagonal = np.diag(board_state,i)
            for j in range(len(diagonal)-3):
                segments.append(diagonal[j:j+4])
                
        #Dá flip no array e verifica as diagonais principais do array flipado (equivalentes às diagonais perpendiculares às principais do array original)
        board_state_flip = np.fliplr(board_state)
        for i in range(-2,4):
            diagonal = np.diag(board_state_flip,i)
            for j in range(len(diagonal)-3):
                segments.append(diagonal[j:j+4])
        
        print(segments)
        return segments

    #recebe um estado e itera sobre todas as sequencias de 4 valores, e retorna o vencedor (no caso deste existir)
    def ganho(self, board_state):
        for segment in self.get_segments(board_state):
            if np.array_equal(segment, ['X', 'X', 'X', 'X']):
                return "X"
            elif np.array_equal(segment, ['O', 'O', 'O', 'O']):
                return "O"
        return None
    
    #Verifica se um determinado estado é um estado terminal/final (estado em que um dos jogadores ganhou ou em que não há ações possíveis)
    def terminal(self, board_state, turn):
        #Se houver vencedor o jogo acaba
        if self.ganho(board_state):
            return True
        #Se não houverem ações disponiveis o jogo acaba
        elif turn == NUM_MOVES: #num total de movimentos
            return True
        else:
            return False
        
    #Recebe um estado e retorna a utilidade desse estado.
    def utility(self, board_state):
        win = self.ganho(board_state)
        if win =="X":
            return 512
        elif win =="O":
            return -512
        else:
            return 0
        
    #Função para ver de quem é o turno
    def get_turn(self, start, turn):
        if start == 0: #jogador começou
                if turn % 2 == 0: #vez do jogador
                    return "O"
                else:
                    return "X"
            
        else: #ai começou
            if turn % 2 == 0: #vez da ai
                return "X"
            else:
                return "O"
          
    # Recebe um estado e retorna uma lista com todas as ações possíveis.  
    def all_actions(self, state):
        actions = []

        for i in range(7):
            if state[0][i] == "-":
                actions.append(i)
        if len(actions)== 0:
            return None
        return actions
        
    #avalia o valor de cada estado
    def evaluate(self, board_state):
        segment = self.get_segments(board_state)
        
        cx = 0
        co = 0
        for i in segment:
            if i=="X":
                cx+=1
            elif i=="O":
                co+=1

        # print(cx, co)
        if (cx==0 and co==0) or (cx>0 and co>0):
            return 0
        elif cx == 1:
            return 1
        elif cx == 2:
            return 10
        elif cx==3:
            return 50
        
        #   VERIFICAR ISTO
        elif cx == 4:
            return 512
        elif co ==4:
            return -512
        # ---

        elif co == 1:
            return -1
        elif co == 2:
            return -10
        elif co==3:
            return -50

        
    def alphabeta(self, board_state, start, turn, depth, alpha, beta):

        """
        #Aplica o algoritmo min/max aproximado (como descrito no enunciado).
        #Aplica também alpha-betta pruning.
        #Recebe um estado de jogo, um limite máximo de profundiade e alpha beta.
        #Utiliza alpha-beta até à profundidade limite retornando uma aproximação do valor real.
        #Retorna o valor min/max e a ação correspondente.
        #Avalia automaticamente se é o max player ("X") ou min player ("O").
        #
"""
        player = self.get_turn(start,turn)
        
        novo_game = game()
        novo_game.board = board_state
        
        if depth == 0:
            #avalia os segmentos?
            segments = self.get_segments(board_state)
            s = 0
            for segment in segments:
                s = s + self.evaluate(segment)

            #olha de quem é a vez e adiciona 16 na vez da ai e subtrai 16 na vez do jogador
            if start == 0: #jogador começou
                if turn % 2 == 0: #vez do jogador
                    s = s - 16
                else:
                    s = s + 16
            
            else: #ai começou
                if turn % 2 == 0: #vez da ai
                    s = s + 16
                else:
                    s = s - 16
                    
            return s
        
        
        #FAZER COM QUE RETORNE O MOVIMENTO QUE FAZ GANHAR
        if self.terminal(board_state,turn):
            return self.utility(board_state), None
        
        if player == "X": #vez da ai
            v = -np.infty
            move = None
            for action in self.all_actions(board_state):
                res = novo_game.nextEmptyRowinCollumn(action)
                test = self.alphabeta(res, start, turn, depth-1, alpha, beta )[0]
                if test >v:
                    v = test 
                    move = action
                if v > beta:
                    break
                alpha = max(alpha, v)
            return move
        
        else: #vez do jogador
            v = np.infty
            for action in self.all_actions(board_state):
                res = novo_game.nextEmptyRowinCollumn(action)
                test = self.alphabeta(res, start, turn, depth-1, alpha, beta )[0]
                if test < v:
                    v = test 
                    move = action
                if v < alpha:
                    break
                beta = min (beta, v)        
            return move

  Função que checa se houve vitória após cada movimento. 
    def get_segments(self, board_board_state):
        
        #verificar se houve vitória na row
        row_count = 0 #conta quantas vezes seguidas a peça aparece na row
        for i in range(NUM_COL):
            if self.board[move_row][i] == piece: 
                row_count += 1
                if row_count >= 4: 
                    return True
            else: 
                row_count = 0
        
        
        #verificar se houve vitória na coluna
        col_count = 0 #conta quantas vezes seguidas a peça aparece na coluna
        for i in range(NUM_ROW):
            if self.board[i][move_col] == piece: 
                col_count += 1
                if col_count >= 4: 
                    return True
            else: 
                col_count = 0
        
        #verificar se houve vitória na diagonal principal e adjacentes
        r_diag_count = 0
        r_diag_array = []
        for k in range(-2,4): #gerar os r_array a partir da diagonal principal
            r_diag_array = np.diag(self.board, k) #transforma uma diagonal num array uni-dimensional
            for i in range(r_diag_array.size): #verifica cada array pra ver se houve vitória
                if r_diag_array[i] == piece:
                    r_diag_count += 1
                    if r_diag_count >= 4: 
                        return True
                else: 
                    r_diag_count = 0
                    
        #verificar se houve vitória na diagonal secundária e adjacentes
        l_diag_count = 0
        l_diag_array = []
        for k in range(-2,4): #gerar os r_array a partir da diagonal principal
            l_diag_array = np.diag(np.fliplr(self.board), k) #dá flip no array e verifica as diagonais principais do array flipado
            for i in range(l_diag_array.size): #verifica cada array pra ver se houve vitória
                if l_diag_array[i] == piece:
                    l_diag_count += 1
                    if l_diag_count >= 4: 
                        return True
                else: 
                    l_diag_count = 0
                    
        return False"""