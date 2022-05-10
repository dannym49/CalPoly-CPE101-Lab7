import unittest
from objects import *
from list_comp import *

class TestCases(unittest.TestCase):
   # Borrowed from Lab 5 to help compare lists
   # of floating point numbers. This function is ONLY
   # for comparing lists of floats.
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_distance_all(self):
      points = [Point(0.0, 2.0), Point(3.0, 0.0)]
      res = [2.0, 3.0]
      self.assertListAlmostEqual(distance_all(points), res)

   def test_distance_all1(self):
      points = [Point(2.4, 4.2), Point(3.1, 0.5)]
      res = [4.83735464, 3.140063693]
      self.assertListAlmostEqual(distance_all(points), res)

   def test_are_in_first_quadrant(self):
      points = [Point(0.0, 0.0), Point(1.0,2.0), Point(-1.0,2.0)]
      res = [Point(1.0,2.0)]
      self.assertListAlmostEqual(are_in_first_quadrant(points), res)

   def test_are_in_first_quadrant2(self):
      points = [Point(-1.0, 0.0), Point(0.00001, -5.0), Point(-1.0, -2.0), Point(100.0, 2.0)]
      res = [Point(100.0, 2.0)]
      self.assertListAlmostEqual(are_in_first_quadrant(points), res)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()