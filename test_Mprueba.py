import unittest
from chess import Chess

class TestChess(unittest.TestCase):

    def setUp(self):
        self.juego = Chess()

    def test_move(self):
        # Suponiendo que el tablero est\u00e1 en su estado inicial
        self.juego.move(1, 0, 3, 0)  # Mover un pe\u00f3n de 'a2' a 'a4'
        # Verificar el nuevo estado del tablero
        self.assertEqual(self.juego.get_piece_at(3, 0), 'P')  # 'P' para pe\u00f3n, seg\u00fan la implementaci\u00f3n

    def test_invalid_move(self):
        with self.assertRaises(ValueError):
            self.juego.move(1, 0, 9, 0)  # Movimiento fuera del rango

if __name__ == '__main__':
    unittest.main()
