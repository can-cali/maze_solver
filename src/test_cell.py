import unittest
from cell import Cell
from window import Window

class TestCell(unittest.TestCase):
    def test_draw(self):
        win = Window(800,600)
        cell = Cell(win, False, True, False, True)
        cell.draw(0,0,1,1)
    
    def test_draw_move(self):
        win = Window(800,600)
        cell = Cell(win, False, True, False, True)
        cell.draw(0,0,1,1)
        cell1 = Cell(win, False, True, False, True)
        cell1.draw(1,0,2,1)
        cell.draw_move(cell1)
        cell.draw_move(cell1, True)

if __name__ == "__main__":
    unittest.main()