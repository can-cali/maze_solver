import unittest
from cell import Cell
from window import Window

class TestCell(unittest.TestCase):
    def test_draw(self):
        win = Window(800,600)
        cell = Cell(win, False, True, False, True)
        cell.draw(0,0,1,1)

if __name__ == "__main__":
    unittest.main()