from piezas import Peon, Torre, Caballo, Alfil, Reina, Rey
from Board import Board
from tu_modulo import es_movimiento_valido
def test_peon():
    board = Board()
    white_pawn = Peon('WHITE')
    black_pawn = Peon('BLACK')
    
    board.set_piece(6, 0, white_pawn)
    assert white_pawn.mover(6, 0, 4, 0, board) == True, "Error en el movimiento del peón blanco dos casillas"
    assert white_pawn.mover(6, 0, 5, 0, board) == True, "Error en el movimiento del peón blanco una casilla"
    assert white_pawn.mover(6, 0, 5, 1, board) == False, "Error en el movimiento inválido del peón blanco"
    
    board.set_piece(1, 0, black_pawn)
    assert black_pawn.mover(1, 0, 3, 0, board) == True, "Error en el movimiento del peón negro dos casillas"
    assert black_pawn.mover(1, 0, 2, 0, board) == True, "Error en el movimiento del peón negro una casilla"
    assert black_pawn.mover(1, 0, 2, 1, board) == False, "Error en el movimiento inválido del peón negro"

def test_torre():
    board = Board()
    white_rook = Torre('WHITE')
    black_rook = Torre('BLACK')
    
    board.set_piece(0, 0, white_rook)
    assert white_rook.mover(0, 0, 0, 5, board) == True, "Error en el movimiento horizontal de la torre blanca"
    assert white_rook.mover(0, 0, 5, 0, board) == True, "Error en el movimiento vertical de la torre blanca"
    assert white_rook.mover(0, 0, 2, 2, board) == False, "Error en el movimiento diagonal inválido de la torre blanca"
    
    board.set_piece(7, 7, black_rook)
    assert black_rook.mover(7, 7, 7, 2, board) == True, "Error en el movimiento horizontal de la torre negra"
    assert black_rook.mover(7, 7, 2, 7, board) == True, "Error en el movimiento vertical de la torre negra"
    assert black_rook.mover(7, 7, 5, 5, board) == False, "Error en el movimiento diagonal inválido de la torre negra"

def test_caballo():
    board = Board()
    white_knight = Caballo('WHITE')
    
    board.set_piece(4, 4, white_knight)
    assert white_knight.mover(4, 4, 2, 3, board) == True, "Error en el movimiento del caballo blanco"
    assert white_knight.mover(4, 4, 3, 2, board) == True, "Error en el movimiento del caballo blanco"
    assert white_knight.mover(4, 4, 5, 5, board) == False, "Error en el movimiento inválido del caballo blanco"

def test_alfil():
    board = Board()
    white_bishop = Alfil('WHITE')
    
    board.set_piece(4, 4, white_bishop)
    assert white_bishop.mover(4, 4, 1, 1, board) == True, "Error en el movimiento diagonal del alfil blanco"
    assert white_bishop.mover(4, 4, 6, 6, board) == True, "Error en el movimiento diagonal del alfil blanco"
    assert white_bishop.mover(4, 4, 4, 6, board) == False, "Error en el movimiento inválido del alfil blanco"

def test_reina():
    board = Board()
    white_queen = Reina('WHITE')
    
    board.set_piece(4, 4, white_queen)
    assert white_queen.mover(4, 4, 1, 1, board) == True, "Error en el movimiento diagonal de la reina blanca"
    assert white_queen.mover(4, 4, 4, 7, board) == True, "Error en el movimiento horizontal de la reina blanca"
    assert white_queen.mover(4, 4, 7, 4, board) == True, "Error en el movimiento vertical de la reina blanca"
    assert white_queen.mover(4, 4, 5, 6, board) == False, "Error en el movimiento inválido de la reina blanca"

def test_rey():
    board = Board()
    white_king = Rey('WHITE')
    
    board.set_piece(4, 4, white_king)
    assert white_king.mover(4, 4, 5, 4, board) == True, "Error en el movimiento del rey blanco"
    assert white_king.mover(4, 4, 4, 5, board) == True, "Error en el movimiento del rey blanco"
    assert white_king.mover(4, 4, 6, 6, board) == False, "Error en el movimiento inválido del rey blanco"

# Ejecutar las pruebas
test_peon()
test_torre()
test_caballo()
test_alfil()
test_reina()
test_rey()

print("Todos los tests pasaron correctamente.")

