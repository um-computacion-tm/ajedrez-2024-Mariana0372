class Board:
    def __init__(self):
        self.__tablero__ = self.__crear_tablero__()

    def __crear_tablero__(self):
        # Crear un tablero de 8x8 vacío
        tablero = [['.' for _ in range(8)] for _ in range(8)]

        # Configuración de piezas para las blancas y negras
        piezas_blancas = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        piezas_negras = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        
        # Colocar las piezas blancas en la fila 1 (índice 0) y 2 (índice 1)
        tablero[0] = piezas_blancas
        tablero[1] = ['P'] * 8

        # Colocar las piezas negras en la fila 8 (índice 7) y 7 (índice 6)
        tablero[6] = ['p'] * 8
        tablero[7] = piezas_negras

        return tablero

    def __imprimir_tablero__(self):
        # Encabezado de columnas
        columnas = '  a b c d e f g h'
        print(columnas)
        
        # Imprimir cada fila del tablero
        fila_num = 8
        for fila in self.__tablero__:
            # Mostrar número de fila y contenido de la fila
            print(f"{fila_num} {' '.join(fila)}")
            fila_num -= 1

        # Línea final con coordenadas de columnas
        print(columnas)

    def __get_piece__(self, row, col):
        # Obtener una pieza en una posición específica
        return self.__tablero__[row][col]

    def __set_piece__(self, row, col, piece):
        # Colocar una pieza en una posición específica
        self.__tablero__[row][col] = piece

