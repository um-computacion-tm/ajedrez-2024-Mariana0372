from board import Board
from piezas import Peon, Torre, Caballo, Alfil, Reina, Rey
from movimientos import es_movimiento_valido
from undo_redo import UndoRedoManager

class Chess:
    def __init__(self):
        # Inicializa el tablero de ajedrez y el turno del jugador.
        self.__board = Board()
        self.__turn = "WHITE"
        # Inicializa el manejador de deshacer/rehacer.
        self.__undo_redo_manager = UndoRedoManager()

    def move(self, from_row, from_col, to_row, to_col):
        # Obtiene el símbolo de la pieza en la posición de origen.
        piece_symbol = self.__board.get_piece(from_row, from_col)
        if piece_symbol == '.':
            print("No hay ninguna pieza en la posición de origen.")
            return

        # Verifica si el movimiento es válido.
        if not es_movimiento_valido(from_row, from_col, to_row, to_col, self.__board, self.__turn):
            print("Movimiento no válido.")
            return
        
        # Convierte el símbolo de la pieza a un objeto de pieza.
        piece_obj = self.__convert_symbol_to_piece(piece_symbol)
        if piece_obj is None:
            print("Error al convertir la pieza.")
            return

        # Guarda el estado actual del tablero en la pila de deshacer.
        self.__undo_redo_manager.push(self.__board.crear_copia())

        # Realiza el movimiento de la pieza.
        self.__board.set_piece(to_row, to_col, piece_obj)
        self.__board.set_piece(from_row, from_col, None)
        
        # Cambia el turno del jugador.
        self.__change_turn()

    def undo(self):
        # Obtiene el estado del tablero anterior a partir de la pila de deshacer.
        previous_board = self.__undo_redo_manager.undo()
        if previous_board:
            self.__board = previous_board
            # Cambia el turno, ya que deshacer también cambia el turno.
            self.__change_turn() 

    def redo(self):
        # Obtiene el estado del tablero siguiente a partir de la pila de rehacer.
        next_board = self.__undo_redo_manager.redo()
        if next_board:
            self.__board = next_board
            # Cambia el turno, ya que rehacer también cambia el turno.
            self.__change_turn() 

    def __convert_symbol_to_piece(self, symbol):
        # Convierte un símbolo de pieza a un objeto de pieza con el color correspondiente.
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
        # Cambia el turno del jugador actual.
        self.__turn = "BLACK" if self.__turn == "WHITE" else "WHITE"

    def print_board(self):
        # Imprime el estado actual del tablero.
        self.__board.imprimir_tablero()

