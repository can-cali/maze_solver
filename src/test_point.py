import unittest
from point import Point

class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point(100,100)
        self.assertEqual(p.x, 100)
        self.assertEqual(p.y, 100)

if __name__ == "__main__":
    unittest.main()
    