import unittest

class UndoRedoManagerTest(unittest.TestCase):
    def setUp(self):
        self.manager = UndoRedoManager()

    def test_push_and_undo(self):
        # Suponiendo que el tablero es una lista simple para pruebas
        board1 = [1, 2, 3]
        board2 = [4, 5, 6]
        
        self.manager.push(board1)
        self.manager.push(board2)
        
        self.assertEqual(self.manager.undo(), board2)  # Debería deshacer y devolver board2
        self.assertEqual(self.manager.undo(), board1)  # Debería deshacer y devolver board1
        self.assertIsNone(self.manager.undo())         # Debería retornar None ya que no hay más movimientos

    def test_redo(self):
        board1 = [1, 2, 3]
        board2 = [4, 5, 6]
        
        self.manager.push(board1)
        self.manager.push(board2)
        self.manager.undo()  # Deshacer board2
        self.manager.undo()  # Deshacer board1
        
        # Después de deshacer ambos, el redo debería volver a traer board1 y board2
        self.manager.redo()  # Debería rehacer y devolver board1
        self.assertEqual(self.manager.redo(), board2)  # Debería rehacer y devolver board2

    def test_clear_redo_stack_on_new_push(self):
        board1 = [1, 2, 3]
        board2 = [4, 5, 6]
        
        self.manager.push(board1)
        self.manager.push(board2)
        self.manager.undo()  # Deshacer board2
        self.manager.redo()  # Rehacer board2
        
        board3 = [7, 8, 9]
        self.manager.push(board3)  # Agregar board3
        
        self.assertEqual(self.manager.undo(), board3)  # Debería deshacer board3
        self.assertEqual(self.manager.undo(), board2)  # Debería deshacer board2
        self.assertIsNone(self.manager.undo())         # No hay más movimientos
        
    def test_no_redo_when_empty(self):
        self.assertIsNone(self.manager.redo())  # No debería rehacer nada cuando la pila de rehacer está vacía

    def test_no_undo_when_empty(self):
        self.assertIsNone(self.manager.undo())  # No debería deshacer nada cuando la pila de deshacer está vacía

if __name__ == '__main__':
    unittest.main()
