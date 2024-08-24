import unittest
from maze import Maze
from window import Window

class TestMaze(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800,600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        win = Window(800,600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_left_wall)
        self.assertFalse(m1._cells[num_cols-1][num_rows-1].has_right_wall)

if __name__ == "__main__":
    unittest.main()