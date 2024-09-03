import unittest
from chess import Chess
from board import Board
from redis_storage import guardar_partida, cargar_partida

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.chess._Chess__turn, "WHITE")

    def test_move_piece(self):
        # Suponiendo que el tablero empieza con piezas en posiciones iniciales
        # y que tienes un método para verificar el estado del tablero.
        self.chess.move(1, 0, 3, 0)  # mueve un peón
        # Verifica que la pieza se haya movido
        self.assertEqual(self.chess._Chess__board.get_piece(3, 0).symbol, 'P')
        self.assertEqual(self.chess._Chess__board.get_piece(1, 0), None)

    def test_move_no_piece(self):
        self.chess.move(4, 4, 5, 5)  # Movimiento sin pieza en la posición de origen
        # Debería mostrar "No hay ninguna pieza en la posición de origen."
        # y no cambiar el estado del tablero.

    def test_invalid_move(self):
        # Suponiendo que `es_movimiento_valido` devuelve False para movimientos inválidos
        self.chess.move(1, 0, 2, 2)  # Movimiento no válido
        # Debería mostrar "Movimiento no válido."

    def test_undo_redo(self):
        self.chess.move(1, 0, 3, 0)
        self.chess.undo()
        # Verifica que el tablero ha vuelto a su estado anterior
        self.assertEqual(self.chess._Chess__board.get_piece(1, 0).symbol, 'P')
        self.assertEqual(self.chess._Chess__board.get_piece(3, 0), None)
        
        self.chess.redo()
        # Verifica que el tablero se ha restaurado al estado después del movimiento
        self.assertEqual(self.chess._Chess__board.get_piece(3, 0).symbol, 'P')
        self.assertEqual(self.chess._Chess__board.get_piece(1, 0), None)

    def test_guardar_cargar_partida(self):
        self.chess.move(1, 0, 3, 0)
        self.chess.guardar_partida("test_id")
        # Mockear la función `cargar_partida` para devolver un estado conocido
        estado_tablero = {'turn': 'WHITE'}
        def mock_cargar_partida(id_partida):
            return estado_tablero
        
        global cargar_partida
        cargar_partida = mock_cargar_partida
        
        self.chess.cargar_partida("test_id")
        # Verifica que el turno se haya restaurado correctamente
        self.assertEqual(self.chess._Chess__turn, "WHITE")
        # Verifica que el tablero está en el estado guardado

    def test_print_board(self):
        # Captura la salida de `print_board` y verifica su contenido
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        self.chess.print_board()
        sys.stdout = sys.__stdout__
        
        # Verifica que la salida capturada contiene la representación esperada del tablero
        output = captured_output.getvalue()
        # Añadir verificaciones específicas según cómo se imprima el tablero

if __name__ == '__main__':
    unittest.main()

