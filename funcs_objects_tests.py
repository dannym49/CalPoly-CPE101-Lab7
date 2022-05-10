import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      # Add code here.
      pt1 = Point(1.234, -8)
      self.assertAlmostEqual(pt1.x, 1.234)
      self.assertAlmostEqual(pt1.y, -8)


   def test_circle1(self):
      # Add code here.
      circle = Circle(Point(1.2, 2.1), 3.2)
      self.assertAlmostEqual(circle.center.x, 1.2)
      self.assertAlmostEqual(circle.center.y, 2.1)
      self.assertAlmostEqual(circle.radius, 3.2)

   def test_circle2(self):
      # Add code here.
      circle = Circle(Point(5.6, 8.2), 5.5)
      self.assertAlmostEqual(circle.center.x, 5.6)
      self.assertAlmostEqual(circle.center.y, 8.2)
      self.assertAlmostEqual(circle.radius, 5.5)
   # Add other testing functions

   def test_distance1(self):
      p1 = Point(0.0, 3.0)
      p2 = Point(4.0, 0.0)
      self.assertAlmostEqual(distance(p1, p2), 5.0)

   def test_distance2(self):
      p1 = Point(0.0, 6.0)
      p2 = Point(8.0, 0.0)
      self.assertAlmostEqual(distance(p1, p2), 10.0)

   def test_distance3(self):
      p1 = Point(7.5, 3.1)
      p2 = Point(10.4, 9.8)
      self.assertAlmostEqual(distance(p1, p2), 7.30068489)

   def test_overlap(self):
      c1 = Circle(Point(1.2, 2.1), 3.2)
      c2 = Circle(Point(3.5, 5.8), 1.7)
      self.assertEqual(circles_overlap(c1, c2), True)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

