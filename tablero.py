from piezas import Peon, Torre, Caballo, Alfil, Reina, Rey

class Board:
    def __init__(self):
#inicializa el tablero creando el estado iniacial del juego
        self.board = self.crear_tablero()
#crea un tablero de ajedres vacio con 8 filas y 8 columnas
    def crear_tablero(self):
        tablero = [[None for _ in range(8)] for _ in range(8)]
#inicializa piezas blancas y negras en sus posiciones iniciales 
        piezas_blancas = [Torre('WHITE'), Caballo('WHITE'), Alfil('WHITE'), Reina('WHITE'), Rey('WHITE'), Alfil('WHITE'), Caballo('WHITE'), Torre('WHITE')]
        piezas_negras = [Torre('BLACK'), Caballo('BLACK'), Alfil('BLACK'), Reina('BLACK'), Rey('BLACK'), Alfil('BLACK'), Caballo('BLACK'), Torre('BLACK')]
#coloca las piezas blancas en la primera y segunda fila 
        tablero[0] = piezas_blancas
        tablero[1] = [Peon('WHITE')] * 8
#colaca las piezas negras en la secta y septima fila
        tablero[6] = [Peon('BLACK')] * 8
        tablero[7] = piezas_negras
        return tablero

    def get_piece(self, row, col):
#Obtiene la pieza en la posición dada y devuelve su símbolo
        piece = self.board[row][col]
        return piece if piece is None else piece.symbol

    def set_piece(self, row, col, piece):
        self.board[row][col] = piece

    def imprimir_tablero(self):
        print('  a b c d e f g h')
        for i in range(8):
            print(f"{8 - i} {' '.join(self.get_piece(i, j) or '.' for j in range(8))}")
        print('  a b c d e f g h')

    def crear_copia(self):
#Crea una copia del tablero actual para permitir deshacer y rehacer movimientos
        copia = Board()
#Copia el estado del tablero actual a la copia, asegurando que se clonen las referencias a las filas
        copia.board = [fila[:] for fila in self.board]
        return copia
