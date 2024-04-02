import numpy as np
from dictgeneration import gen_dict
NUM_ROW = 6
NUM_COL = 7
EMPTY = "-"
PLAYER_PIECE = "X"
AI_PIECE = "O"
index_dict,pos_dict = gen_dict()


class game:
    #turn = 0
    def __init__(self, calculate_heuristics=True):
        self.game_winner = EMPTY  # variáveis que controlam o fim do jogo
        self.board_is_full = False
        self.segment_heuristics = [0 for _ in range (69)]
        self.board = np.full([NUM_ROW, NUM_COL], EMPTY)
        self.last_move = None
        self.calculate_heuristics = calculate_heuristics

    def drawBoard(self):
        for i in range(7): print(i, end=" ") #imprime os numeros das colunas
        print() # coloca newline
        for line in np.flip(self.board, 0):
            for piece in line:
                print(piece, end=" ")
            print()# coloca newline
        return

    """Dado um input, verifica a função availableCollumns para saber se é válido.
    Se não for pede novamente o input, do contrário usa a função putGamePiece para alterar a board."""

    def playOneTurn(self):
        available = self.availableCollumns()
        try:  # error handling
            collumn = int(
                input("Choose in which collumn do you wanna play or press 9 to quit: ")
            )
        except:
            collumn = -1

        while collumn not in available:
            if collumn == 9:
                quit()  # opção para quitar
            try:  # more error handlings
                collumn = int(
                    input(
                        "The collumn you selected is either full or invalid, choose another one or press 9 to quit: "
                    )
                )
            except:
                collumn = -1
        self.putGamePiece(collumn, PLAYER_PIECE)
        return

    """Verifica qual a próxima row vazia e alterar a põe a peça nesta row. 
    Checa após cada movimento a função check_win_after_move para saber se houve ganhador."""

    def putGamePiece(self, collumn, piece):
        available = self.availableCollumns()
        if collumn not in available:
            print("The last move was invalid, below is the last state of the board and the move made, the game will quit")
            self.drawBoard()
            print("last move = {collumn}")
            quit()

        piece_placement = self.nextEmptyRowinCollumn(collumn)
        self.board[piece_placement][collumn] = piece
        if self.check_win_after_move(piece_placement, collumn, piece):
            self.game_winner = piece  # checar se houve ganhador
        elif not self.availableCollumns():
            self.board_is_full = True  # se não há colunas vazias, a board está cheia
        # not list aparentemente é um dos jeitos mais eficientes de checar se uma lista está vazia, python é estranho - M
        if self.calculate_heuristics: self.update_heuristics(piece_placement, collumn) # atualiza as heuristicas se o bool for True
        self.last_move = collumn
        return

    """Checa a última row para saber quais colunas não estão cheias. Retorna a lista de colunas."""

    def availableCollumns(self):
        available = []
        for i, value in enumerate(self.board[NUM_ROW - 1]):
            if value == EMPTY:
                available.append(i)
        return available

    """Dado uma coluna, verifica qual a próxima row vazia. Retorna o número da row."""

    def nextEmptyRowinCollumn(self, collumn):
        for i, value in enumerate(self.board[:, collumn]):
            if value == EMPTY:
                return i
        return

    """Função que checa se houve vitória após cada movimento. 
    Verifica somente os arrays que contém a peça em [move_row, move_col]."""
    def check_win_after_move(self, move_row, move_col, piece):
        win_segment = [piece, piece, piece, piece]
        for i in self.segments_that_intersect(move_row, move_col): # verifica se houve vitoria em todos os segmentos que são modificados pelo ultimo movimento
            if i == win_segment: return True
        return False

    # retorna lista com todos os segmentos de 4 em todas as direções
                
    def get_segments(self):
        segments = []
        # Verifica linhas e colunas
        for i in range(NUM_ROW):
            line = self.board[i]
            for j in range(4):
                segments.append(line[j : j + 4])
            col = self.board[:, i]
            for j in range(3):
                segments.append(col[j : j + 4])

        # Verifica a ultima coluna
        col = self.board[:, NUM_COL - 1]
        for j in range(3):
            segments.append(col[j : j + 4])

        # Verifica as diagonais principais
        for i in range(-2, 4):
            dia = np.diag(self.board, i)
            for j in range(len(dia) - 3):
                segments.append(dia[j : j + 4])

        # Dá flip no array e verifica as diagonais principais do array flipado
        # (equivalentes às diagonais perpendiculares às principais do array original)
        state_tr = np.fliplr(self.board)
        for i in range(-2, 4):
            dia = np.diag(state_tr, i)
            for j in range(len(dia) - 3):
                segments.append(dia[j : j + 4])
        return segments
    def segments_that_intersect(self, move_row, move_col):
        segments = [[self.board[pos[0],pos[1]] for pos in list] for list in pos_dict[(move_row,move_col)]]
        return segments

    # avalia um segmento e retorna a sua pontuação
    def update_heuristics(self,move_row,move_col):
        indexes = index_dict[(move_row,move_col)]
        segments = self.segments_that_intersect(move_row, move_col)             
        for i in range(len(indexes)):
            self.segment_heuristics[indexes[i]] = self.evaluate(segments[i])

    def evaluate(self, segment):
        count_x = 0
        count_o = 0

        for i in segment:
            if i == PLAYER_PIECE:
                count_x += 1
            elif i == AI_PIECE:
                count_o += 1

        if (count_x == 0 and count_o == 0) or (count_x > 0 and count_o > 0):
            return 0

        match count_x:
            case 1:
                return 1
            case 2:
                return 10
            case 3:
                return 50
            case 4:
                return 512

        match count_o:
            case 1:
                return -1
            case 2:
                return -10
            case 3:
                return -50
            case 4:
                return -512

    # avalia todos as posições para descobrir se há vencedor
    def evaluate_all(self):
        if self.game_winner == PLAYER_PIECE:
            return 512
        elif self.game_winner == AI_PIECE:
            return -512
        elif self.board_is_full:
            return 0
        else:
            sum = 0
            if self.player() == PLAYER_PIECE:
                sum = sum + 16
            elif self.player() == AI_PIECE:
                sum = sum - 16
            for segment in self.get_segments():
                sum = sum + self.evaluate(segment)
            return sum

    """Verifica se um determinado estado é um estado terminal/final 
    (estado em que um dos jogadores ganhou ou em que não há ações possíveis)"""

    def terminal(self):
        if self.game_winner == PLAYER_PIECE or self.game_winner == AI_PIECE:
            return True
        else:
            return self.board_is_full
        """
        elif len(self.availableCollumns())==0:
            return True
        else:
            return False
        """

    """Recebe um estado e retorna o vencedor (no caso deste existir)"""

    def checkwin_wholeboard(self):
        for (
            segment
        ) in self.get_segments():  # Itera sobre todos os segmentos de tamanho 4
            if np.array_equal(segment, ["X", "X", "X", "X"]):
                return "X"
            elif np.array_equal(segment, ["O", "O", "O", "O"]):
                return "O"
        return None

    """Otimização da função player. Utiliza self.turn para avaliar qual o jogador atual.
    Não está em uso em outras classes."""

    """    
    def player_(self):
        if self.board_is_full:
            return None
        elif self.turn % 2 == 0:
            return PLAYER_PIECE
        else:
            return AI_PIECE"""

    """Recebe um estado e retorna o jogador nesse turno."""

    def player(self):
        cx = 0  # contador de X
        co = 0  # contador de O
        for i in range(6):
            a = self.board[i]
            for j in range(7):
                b = a[j]
                if b == PLAYER_PIECE:
                    cx += 1
                elif b == AI_PIECE:
                    co += 1
        # caso do tabuleiro estar completamente ocupado
        if cx + co == NUM_COL * NUM_ROW:
            return None

        # Se o número de X's for menor ou igual ao numéro de O's, então é a vez de X jogar.
        if cx <= co:
            return PLAYER_PIECE
        else:
            return AI_PIECE

    def utility(self):
        if self.game_winner == PLAYER_PIECE:
            return 512
        elif self.game_winner == AI_PIECE:
            return -512
        else:
            return 0
