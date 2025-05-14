import unittest
from body import Body
from math import sqrt

class TestCalcDistance(unittest.TestCase):
    def test_basic(self):
        # Don't bother to use floats. Should just work!
        body1 = Body(0, 0, 0, 0, 123, "")
        body2 = Body(1, 1, 0, 0, 123, "")
        dist1 = body1.calc_distance(body2)
        dist2 = body2.calc_distance(body1)
        # Use AssertAlmostEqual so this test is not sensitve to floating point error.
        self.assertAlmostEqual(dist1, sqrt(2))
        # Distances should be symmetric.
        self.assertEqual(dist1, dist2)
    
    def test_negative(self):
        body1 = Body(0, 0, 0, 0, 123, "")
        body2 = Body(-1, -1, 0, 0, 123, "")
        dist1 = body1.calc_distance(body2)
        dist2 = body2.calc_distance(body1)
        self.assertAlmostEqual(dist1, sqrt(2))
        self.assertEqual(dist1, dist2)
    
    def test_different_quadrants(self):
        body1 = Body(1235, -1203, 0, 0, 123, "")
        body2 = Body(-1123, 5, 0, 0, 123, "")
        dist1 = body1.calc_distance(body2)
        dist2 = body2.calc_distance(body1)
        self.assertAlmostEqual(dist1, 2649.420313955489)
        self.assertEqual(dist1, dist2)
    
    def test_small(self):
        body1 = Body(0.00001, 0.01, 0, 0, 123, "")
        body2 = Body(0.000001, -0.001, 0, 0, 123, "")
        dist1 = body1.calc_distance(body2)
        dist2 = body2.calc_distance(body1)
        self.assertAlmostEqual(dist1, 0.011000003681817565)
        self.assertEqual(dist1, dist2)
    
    def test_large(self):
        body1 = Body(1.2e10, 3, 0, 0, 123, "")
        body2 = Body(5.0e11, 4, 0, 0, 123, "")
        dist1 = body1.calc_distance(body2)
        dist2 = body2.calc_distance(body1)
        self.assertAlmostEqual(dist1, 488000000000.0)
        self.assertEqual(dist1, dist2)
    
