from piezas import Peon, Torre, Caballo, Alfil, Reina, Rey

def es_movimiento_valido(from_row, from_col, to_row, to_col, board):
    piece = board.get_piece(from_row, from_col)
    if piece == '.':
        return False

    piece_obj = convert_symbol_to_piece(piece)
    if piece_obj is None:
        return False

    return piece_obj.mover(from_row, from_col, to_row, to_col, board)

def convert_symbol_to_piece(symbol):
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

