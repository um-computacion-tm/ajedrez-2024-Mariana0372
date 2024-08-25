# chess.py

from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        # Validar coordenadas
        piece = self.__board__.get_piece(from_row, from_col)
        
        # Verificar si hay una pieza en la posición de origen
        if piece == '.':
            print("No hay ninguna pieza en la posición de origen.")
            return
        
        # Mover la pieza
        self.__board__.set_piece(to_row, to_col, piece)
        self.__board__.set_piece(from_row, from_col, '.')
        
        # Cambiar turno
        self.change_turn()

    @property

    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def print_board(self):
        self.__board__.imprimir_tablero()
