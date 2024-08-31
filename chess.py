from board import Board
from piezas import Peon, Torre, Caballo, Alfil, Reina, Rey
from movimientos import es_movimiento_valido
from undo_redo import UndoRedoManager
from redis_storage import guardar_partida, cargar_partida

class Chess:
    def __init__(self):
        self.__board = Board()
        self.__turn = "WHITE"
        self.__undo_redo_manager = UndoRedoManager()

    def move(self, from_row, from_col, to_row, to_col):
        piece_symbol = self.__board.get_piece(from_row, from_col)
        if piece_symbol == '.':
            print("No hay ninguna pieza en la posición de origen.")
            return

        if not es_movimiento_valido(from_row, from_col, to_row, to_col, self.__board):
            print("Movimiento no válido.")
            return

        piece_obj = self.__convert_symbol_to_piece(piece_symbol)
        if piece_obj is None:
            print("Error al convertir la pieza.")
            return

        self.__undo_redo_manager.push(self.__board.crear_copia())
        self.__board.set_piece(to_row, to_col, piece_obj)
        self.__board.set_piece(from_row, from_col, None)
        self.__change_turn()

    def guardar_partida(self, id_partida):
        estado_tablero = self.__board.obtener_estado_tablero() 
        guardar_partida(id_partida, estado_tablero)

    def cargar_partida(self, id_partida):
        estado_tablero = cargar_partida(id_partida)
        if estado_tablero:
            self.__board.establecer_estado_tablero(estado_tablero)  
            self.__turn = "WHITE" if estado_tablero.get('turn') == 'WHITE' else "BLACK"

    def undo(self):
        previous_board = self.__undo_redo_manager.undo()
        if previous_board:
            self.__board = previous_board
            self.__change_turn()

    def redo(self):
        next_board = self.__undo_redo_manager.redo()
        if next_board:
            self.__board = next_board
            self.__change_turn()

    def __convert_symbol_to_piece(self, symbol):
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

    def __change_turn(self):
        self.__turn = "BLACK" if self.__turn == "WHITE" else "WHITE"

    def print_board(self):
        self.__board.imprimir_tablero()

