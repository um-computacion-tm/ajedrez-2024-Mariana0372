class Board:
    def __init__(self):
        self.__board = [[None for _ in range(8)] for _ in range(8)]
        self.__initialize_board()

    def __initialize_board(self):
        # Coloca las piezas en la posición inicial
        self.__place_pieces('WHITE', 0, 1)
        self.__place_pieces('BLACK', 7, 6)

    def __place_pieces(self, color, back_row, pawn_row):
        self.__board[back_row] = [Torre(color), Caballo(color), Alfil(color), Reina(color), Rey(color), Alfil(color), Caballo(color), Torre(color)]
        self.__board[pawn_row] = [Peon(color) for _ in range(8)]

    def get_piece(self, row, col):
        piece = self.__board[row][col]
        return piece.symbol if piece else '.'

    def set_piece(self, row, col, piece):
        self.__board[row][col] = piece

    def imprimir_tablero(self):
        for row in self.__board:
            print(' '.join(piece.symbol if piece else '.' for piece in row))
 
