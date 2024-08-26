
def es_movimiento_valido(from_row, from_col, to_row, to_col, piece, board):
    def esta_en_rango(row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def liberar_camino(from_row, from_col, to_row, to_col):
        if from_row == to_row:
            step = 1 if from_col < to_col else -1
            for col in range(from_col + step, to_col, step):
                if board.get_piece(from_row, col) != '.':
                    return False
        elif from_col == to_col:
            step = 1 if from_row < to_row else -1
            for row in range(from_row + step, to_row, step):
                if board.get_piece(row, from_col) != '.':
                    return False
        else:
            row_step = 1 if from_row < to_row else -1
            col_step = 1 if from_col < to_col else -1
            row, col = from_row + row_step, from_col + col_step
            while row != to_row:
                if board.get_piece(row, col) != '.':
                    return False
                row += row_step
                col += col_step
        return True

    if not esta_en_rango(to_row, to_col):
        return False

    if piece.lower() == 'p':
        direction = 1 if piece.isupper() else -1
        start_row = 1 if piece.isupper() else 6
        if from_col == to_col:  # Movimiento hacia adelante
            if from_row == start_row and to_row == from_row + 2 * direction and from_col == to_col:
                return board.get_piece(from_row + direction, from_col) == '.'
            return to_row == from_row + direction and board.get_piece(to_row, to_col) == '.'
        elif abs(from_col - to_col) == 1 and to_row == from_row + direction:  # Captura
            return board.get_piece(to_row, to_col) != '.' and board.get_piece(to_row, to_col).isupper() != piece.isupper()
        return False
    elif piece.lower() == 'r':
        if from_row != to_row and from_col != to_col:
            return False
        return liberar_camino(from_row, from_col, to_row, to_col)
    elif piece.lower() == 'n':
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)
    elif piece.lower() == 'b':
        if abs(from_row - to_row) != abs(from_col - to_col):
            return False
        return liberar_camino(from_row, from_col, to_row, to_col)
    elif piece.lower() == 'q':
        return es_movimiento_valido(from_row, from_col, to_row, to_col, 'r', board) or es_movimiento_valido(from_row, from_col, to_row, to_col, 'b', board)
    elif piece.lower() == 'k':
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1
    return False
