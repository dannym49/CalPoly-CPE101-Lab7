import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_point1(self):
      p1 = Point(0,0)
      p2 = Point(0,0)
      self.assertEqual(p1, p2)

   def test_point2(self):
      p1 = Point(1,5)
      p2 = Point(1,5)
      self.assertEqual(p1, p2)

   def test_point3(self):
      p1 = Point(-1,5)
      p2 = Point(-1,5)
      self.assertEqual(p1, p2)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()