class Pieza:
    def __init__(self, color):
        self.color = color
        self.symbol = ''

    def mover(self, from_row, from_col, to_row, to_col, board):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

class Peon(Pieza):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'WHITE' else 'p'

    def mover(self, from_row, from_col, to_row, to_col, board):
        direction = 1 if self.color == 'WHITE' else -1
        start_row = 1 if self.color == 'WHITE' else 6
        if from_col == to_col:
            if from_row == start_row and to_row == from_row + 2 * direction:
                return board.get_piece(from_row + direction, from_col) == '.'
            return to_row == from_row + direction and board.get_piece(to_row, to_col) == '.'
        elif abs(from_col - to_col) == 1 and to_row == from_row + direction:
            return board.get_piece(to_row, to_col) != '.' and board.get_piece(to_row, to_col).color != self.color
        return False

class Torre(Pieza):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if color == 'WHITE' else 'r'

    def mover(self, from_row, from_col, to_row, to_col, board):
        if from_row == to_row or from_col == to_col:
            return self.liberar_camino(from_row, from_col, to_row, to_col, board)
        return False

    def liberar_camino(self, from_row, from_col, to_row, to_col, board):
        row_step = (to_row - from_row) // max(1, abs(to_row - from_row))
        col_step = (to_col - from_col) // max(1, abs(to_col - from_col))
        row, col = from_row + row_step, from_col + col_step
        while (row, col) != (to_row, to_col):
            if board.get_piece(row, col) != '.':
                return False
            row += row_step
            col += col_step
        return True

class Caballo(Pieza):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' if color == 'WHITE' else 'n'

    def mover(self, from_row, from_col, to_row, to_col, board):
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)

class Alfil(Pieza):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'WHITE' else 'b'

    def mover(self, from_row, from_col, to_row, to_col, board):
        if abs(from_row - to_row) == abs(from_col - to_col):
            return self.liberar_camino(from_row, from_col, to_row, to_col, board)
        return False

    def liberar_camino(self, from_row, from_col, to_row, to_col, board):
        row_step = (to_row - from_row) // max(1, abs(to_row - from_row))
        col_step = (to_col - from_col) // max(1, abs(to_col - from_col))
        row, col = from_row + row_step, from_col + col_step
        while (row, col) != (to_row, to_col):
            if board.get_piece(row, col) != '.':
                return False
            row += row_step
            col += col_step
        return True

class Reina(Pieza):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'WHITE' else 'q'

    def mover(self, from_row, from_col, to_row, to_col, board):
        return Torre(self.color).mover(from_row, from_col, to_row, to_col, board) or Alfil(self.color).mover(from_row, from_col, to_row, to_col, board)

class Rey(Pieza):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'WHITE' else 'k'

    def mover(self, from_row, from_col, to_row, to_col, board):
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1

