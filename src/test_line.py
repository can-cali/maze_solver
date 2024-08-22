import unittest
from line import Line
from point import Point

class TestLine(unittest.TestCase):
    def test_init(self):
        p1 = Point(100,100)
        p2 = Point(200,200)
        l = Line(p1,p2)
        self.assertEqual(l.start, p1)
        self.assertEqual(l.end, p2)
    
    def test_draw(self):
        pass

if __name__ == "__main__":
    unittest.main()
