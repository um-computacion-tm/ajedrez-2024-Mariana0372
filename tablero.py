# board.py

from piezas import Peon, Torre, Caballo, Alfil, Reina, Rey

class Board:
    def __init__(self):
        self.board = self.crear_tablero()

    def crear_tablero(self):
        tablero = [[None for _ in range(8)] for _ in range(8)]
        piezas_blancas = [Torre('WHITE'), Caballo('WHITE'), Alfil('WHITE'), Reina('WHITE'), Rey('WHITE'), Alfil('WHITE'), Caballo('WHITE'), Torre('WHITE')]
        piezas_negras = [Torre('BLACK'), Caballo('BLACK'), Alfil('BLACK'), Reina('BLACK'), Rey('BLACK'), Alfil('BLACK'), Caballo('BLACK'), Torre('BLACK')]
        tablero[0] = piezas_blancas
        tablero[1] = [Peon('WHITE')] * 8
        tablero[6] = [Peon('BLACK')] * 8
        tablero[7] = piezas_negras
        return tablero

    def get_piece(self, row, col):
        piece = self.board[row][col]
        return piece if piece is None else piece.symbol

    def set_piece(self, row, col, piece):
        self.board[row][col] = piece

    def imprimir_tablero(self):
        print('  a b c d e f g h')
        for i in range(8):
            print(f"{8 - i} {' '.join(self.get_piece(i, j) or '.' for j in range(8))}")
        print('  a b c d e f g h')
