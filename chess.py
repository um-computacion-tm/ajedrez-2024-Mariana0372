# chess.py

from board import Board
from movimientos import es_movimiento_valido

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.board.get_piece(from_row, from_col)
        if piece == '.':
            print("No hay ninguna pieza en la posición de origen.")
            return

        if not es_movimiento_valido(from_row, from_col, to_row, to_col, self.board):
            print("Movimiento no válido.")
            return
        
        piece_obj = self.convert_symbol_to_piece(piece)
        if piece_obj is None:
            print("Error al convertir la pieza.")
            return
        
        self.board.set_piece(to_row, to_col, piece_obj)
        self.board.set_piece(from_row, from_col, None)
        
        self.change_turn()

    def convert_symbol_to_piece(self, symbol):
        color = 'WHITE' if symbol.isupper() else 'BLACK'
        if symbol.lower() == 'p':
            return Peon(color)
        elif symbol.lower() == 'r':
            return Torre(color)
        elif symbol.lower() == 'n':
            return Caballo(color)
        elif symbol.lower() == 'b':
            return Alfil(color)
        elif symbol.lower() == 'q':
            return Reina(color)
        elif symbol.lower() == 'k':
            return Rey(color)
        return None

    def change_turn(self):
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"

    def print_board(self):
        self.board.imprimir_tablero()
