class UndoRedoManager:
    def __init__(self):
        self.__history = []  # Pila para deshacer
        self.__redo_stack = []  # Pila para rehacer

    def push(self, board_copy):
        """Guardar una copia del tablero para deshacer"""
        self.__history.append(board_copy)
        self.__redo_stack.clear()  # Limpiar la pila de rehacer cuando se hace un nuevo movimiento

    def undo(self):
        """Deshacer el último movimiento"""
        if not self.__history:
            print("No hay movimientos para deshacer.")
            return None
        
        # Guardar el estado actual del tablero en la pila de rehacer
        current_board = self.__history[-1]
        self.__redo_stack.append(current_board)
        
        # Recuperar el último estado de la pila de deshacer
        return self.__history.pop()

    def redo(self):
        """Rehacer el último movimiento deshecho"""
        if not self.__redo_stack:
            print("No hay movimientos para rehacer.")
            return None

        # Guardar el estado actual del tablero en la pila de deshacer
        current_board = self.__redo_stack[-1]
        self.__history.append(current_board)
        
        # Recuperar el último estado de la pila de rehacer
        return self.__redo_stack.pop()

