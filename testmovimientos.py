class Board:
    def __init__(self):
        # Inicializa un tablero vacío de 8x8
        self.board = [['.' for _ in range(8)] for _ in range(8)]

    def get_piece(self, row, col):
        return self.board[row][col]

    def set_piece(self, row, col, piece):
        self.board[row][col] = piece

def test_es_movimiento_valido():
    board = Board()
    
    # Prueba movimiento válido del peón
    board.set_piece(6, 4, 'P')  # Peón blanco en (6,4)
    assert es_movimiento_valido(6, 4, 4, 4, 'P', board) == True  # Avanzar dos pasos
    assert es_movimiento_valido(6, 4, 5, 4, 'P', board) == True  # Avanzar un paso
    assert es_movimiento_valido(6, 4, 5, 5, 'P', board) == False  # Movimiento inválido (peón no puede capturar)
    
    # Configura para captura de peón
    board.set_piece(5, 5, 'b')  # Pieza negra en (5,5)
    assert es_movimiento_valido(6, 4, 5, 5, 'P', board) == True  # Captura válida
    
    # Configura tablero para probar la torre
    board.set_piece(0, 0, 'R')  # Torre blanca en (0,0)
    assert es_movimiento_valido(0, 0, 0, 5, 'R', board) == True  # Movimiento horizontal válido
    assert es_movimiento_valido(0, 0, 5, 0, 'R', board) == True  # Movimiento vertical válido
    
    # Torre bloqueada
    board.set_piece(3, 0, 'p')  # Peón en (3,0)
    assert es_movimiento_valido(0, 0, 3, 0, 'R', board) == False  # Movimiento bloqueado por pieza

    # Configura tablero para probar el caballo
    board.set_piece(7, 1, 'N')  # Caballo blanco en (7,1)
    assert es_movimiento_valido(7, 1, 5, 2, 'N', board) == True  # Movimiento en L válido
    assert es_movimiento_valido(7, 1, 5, 3, 'N', board) == False  # Movimiento inválido (no en L)
    
    # Configura tablero para probar el alfil
    board.set_piece(2, 2, 'B')  # Alfil blanco en (2,2)
    assert es_movimiento_valido(2, 2, 5, 5, 'B', board) == True  # Movimiento diagonal válido
    assert es_movimiento_valido(2, 2, 4, 4, 'B', board) == True  # Movimiento diagonal válido
    
    # Configura tablero para probar la reina
    board.set_piece(3, 3, 'Q')  # Reina blanca en (3,3)
    assert es_movimiento_valido(3, 3, 6, 3, 'Q', board) == True  # Movimiento vertical válido
    assert es_movimiento_valido(3, 3, 3, 6, 'Q', board) == True  # Movimiento horizontal válido
    assert es_movimiento_valido(3, 3, 6, 6, 'Q', board) == True  # Movimiento diagonal válido
    
    # Configura tablero para probar el rey
    board.set_piece(4, 4, 'K')  # Rey blanco en (4,4)
    assert es_movimiento_valido(4, 4, 5, 4, 'K', board) == True  # Movimiento válido (1 paso en cualquier dirección)
    assert es_movimiento_valido(4, 4, 3, 5, 'K', board) == True  # Movimiento válido (1 paso en cualquier dirección)
    assert es_movimiento_valido(4, 4, 6, 6, 'K', board) == False  # Movimiento inválido (más de 1 paso)

    print("Todos los tests pasaron!")

# Ejecuta los tests
test_es_movimiento_valido()
