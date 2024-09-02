import unittest

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        # Verifica la colocación inicial de las piezas en el tablero
        for col in range(8):
            self.assertIsInstance(self.board.get_piece(0, col), Torre)
            self.assertIsInstance(self.board.get_piece(1, col), Peon)
            self.assertIsInstance(self.board.get_piece(6, col), Peon)
            self.assertIsInstance(self.board.get_piece(7, col), Torre)

    def test_get_piece(self):
        # Verifica que get_piece devuelve el símbolo correcto
        self.assertEqual(self.board.get_piece(0, 0), 'R')
        self.assertEqual(self.board.get_piece(1, 0), 'P')
        self.assertEqual(self.board.get_piece(7, 7), 'R')
        self.assertEqual(self.board.get_piece(6, 7), 'P')

    def test_obtener_estado(self):
        # Verifica que obtener_estado devuelve el estado correcto
        estado = self.board.obtener_estado()
        expected_estado = {
            'a8': 'R', 'b8': 'N', 'c8': 'B', 'd8': 'Q', 'e8': 'K', 'f8': 'B', 'g8': 'N', 'h8': 'R',
            'a7': 'P', 'b7': 'P', 'c7': 'P', 'd7': 'P', 'e7': 'P', 'f7': 'P', 'g7': 'P', 'h7': 'P',
            'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
            'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R'
        }
        self.assertEqual(self.board.obtener_estado(), expected_estado)

    def test_establecer_estado(self):
        # Verifica que establecer_estado configura el tablero correctamente
        estado = {
            'e1': 'K', 'd1': 'Q', 'c1': 'B', 'b1': 'N', 'a1': 'R', 'h1': 'R', 'g1': 'N', 'f1': 'B',
            'e2': 'P', 'd2': 'P', 'c2': 'P', 'b2': 'P', 'a2': 'P', 'h2': 'P', 'g2': 'P', 'f2': 'P',
            'e3': 'K', 'd3': 'Q', 'c3': 'B', 'b3': 'N', 'a3': 'R', 'h3': 'R', 'g3': 'N', 'f3': 'B',
        }
        self.board.establecer_estado(estado)
        self.assertEqual(self.board.get_piece(0, 0), 'R')
        self.assertEqual(self.board.get_piece(0, 4), 'K')
        self.assertEqual(self.board.get_piece(2, 4), 'K')

if __name__ == '__main__':
    unittest.main()

