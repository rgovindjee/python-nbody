from nbody import NBody
import unittest

class TestReadRadius(unittest.TestCase):
    def test_read_radius(self):
        # Test the read_radius function with a sample file.
        nb = NBody()
        radius = nb.read_radius("data/planets.txt")
        self.assertAlmostEqual(radius, 2.50e11, delta=1e4)