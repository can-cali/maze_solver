import unittest
from window import Window
from point import Point
from line import Line

class TestWindow(unittest.TestCase):
    def test_init(self):
        win = Window(800,600)
        self.assertEqual(win.running, False)
        win.close()
        # I cannot test the windows size because functions return 1 for width and height
    
    def test_redraw(self):
        win = Window(800,600)
        p1 = Point(100,100)
        p2 = Point(200,200)
        l = Line(p1,p2)
        win.draw_line(l)
        win.redraw()
        win.close()

if __name__ == "__main__":
    unittest.main()
    