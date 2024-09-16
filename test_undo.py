import unittest
from typing import Optional, List

class TestUndoRedoManager(unittest.TestCase):

    def setUp(self):
        self.manager = UndoRedoManager()

    def test_push_and_get_history(self):
        board1 = [1, 2, 3]
        board2 = [4, 5, 6]
        
        self.manager.push(board1)
        self.manager.push(board2)
        
        self.assertEqual(self.manager.get_history(), [board1, board2])
        self.assertEqual(self.manager.get_redo_stack(), [])

    def test_undo(self):
        board1 = [1, 2, 3]
        board2 = [4, 5, 6]
        
        self.manager.push(board1)
        self.manager.push(board2)
        
        self.assertEqual(self.manager.undo(), board2)
        self.assertEqual(self.manager.get_history(), [board1])
        self.assertEqual(self.manager.get_redo_stack(), [board2])

    def test_redo(self):
        board1 = [1, 2, 3]
        board2 = [4, 5, 6]
        
        self.manager.push(board1)
        self.manager.push(board2)
        self.manager.undo()
        
        self.assertEqual(self.manager.redo(), board2)
        self.assertEqual(self.manager.get_history(), [board1, board2])
        self.assertEqual(self.manager.get_redo_stack(), [])

    def test_undo_empty_history(self):
        self.assertIsNone(self.manager.undo())
        self.assertEqual(self.manager.get_history(), [])
        self.assertEqual(self.manager.get_redo_stack(), [])

    def test_redo_empty_redo_stack(self):
        self.assertIsNone(self.manager.redo())
        self.assertEqual(self.manager.get_history(), [])
        self.assertEqual(self.manager.get_redo_stack(), [])

    def test_clear(self):
        board1 = [1, 2, 3]
        board2 = [4, 5, 6]
        
        self.manager.push(board1)
        self.manager.push(board2)
        self.manager.clear()
        
        self.assertEqual(self.manager.get_history(), [])
        self.assertEqual(self.manager.get_redo_stack(), [])

if __name__ == '__main__':
    unittest.main()

