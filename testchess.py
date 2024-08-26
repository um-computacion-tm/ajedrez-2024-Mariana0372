import unittest
from chess import Chess
from board import Board

class TestChess(unittest.TestCase):

    def setUp(self):
        """Configura el entorno para las pruebas."""
        self.chess = Chess()
        self.board = self.chess._board  # Accede al tablero privado para pruebas

    def test_initial_turn(self):
        """Verifica que el turno inicial sea WHITE."""
        self.assertEqual(self.chess.turn, "WHITE")

    def test_move_piece(self):
        """Prueba que se pueda mover una pieza y que el turno cambie."""
        # Coloca una pieza en la posición (1, 0) y mueve a (2, 0)
        self.board.set_piece(1, 0, 'P')  # Coloca un peón blanco en (1, 0)
        self.chess.move(1, 0, 2, 0)      # Mueve el peón a (2, 0)
        
        # Verifica que la pieza se haya movido
        self.assertEqual(self.board.get_piece(2, 0), 'P')
        self.assertEqual(self.board.get_piece(1, 0), '.')

        # Verifica que el turno haya cambiado a BLACK
        self.assertEqual(self.chess.turn, "BLACK")

    def test_move_piece_no_piece(self):
        """Prueba que se maneje el intento de mover una pieza cuando no hay ninguna en la posición de origen."""
        self.chess.move(0, 0, 1, 0)  # Intenta mover una pieza de una posición vacía
        
        # Verifica que la posición de origen y destino siguen vacías
        self.assertEqual(self.board.get_piece(0, 0), '.')
        self.assertEqual(self.board.get_piece(1, 0), '.')
        
        # Verifica que el turno no cambió
        self.assertEqual(self.chess.turn, "WHITE")

    def test_change_turn(self):
        """Verifica que el turno cambie correctamente."""
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()
