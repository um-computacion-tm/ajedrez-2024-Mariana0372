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

    def obtener_estado(self):
        estado = {}
        for i in range(8):
            for j in range(8):
                piece = self.get_piece(i, j)
                if piece != '.':
                    estado[f"{chr(97 + j)}{8 - i}"] = piece
        return estado

    def establecer_estado(self, estado):
        self.__board = [[None for _ in range(8)] for _ in range(8)]
        for position, symbol in estado.items():
            col, row = ord(position[0]) - ord('a'), 8 - int(position[1])
            piece = self.__convert_symbol_to_piece(symbol)
            self.set_piece(row, col, piece)

    def __convert_symbol_to_piece(self, symbol):
        # Esta función debería convertir un símbolo a una instancia de pieza correspondiente
        color = 'WHITE' if symbol.isupper() else 'BLACK'
        symbol = symbol.upper()
        if symbol == 'R':
            return Torre(color)
        elif symbol == 'N':
            return Caballo(color)
        elif symbol == 'B':
            return Alfil(color)
        elif symbol == 'Q':
            return Reina(color)
        elif symbol == 'K':
            return Rey(color)
        elif symbol == 'P':
            return Peon(color)
        else:
            return None

