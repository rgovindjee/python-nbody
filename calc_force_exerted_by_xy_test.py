import unittest
from body import Body

class TestCalcForceExertedByXy(unittest.TestCase):
    def test_basic(self):
        sun = Body(1.0e12, 2.0e11, 0, 0, 2.0e30, "")
        saturn = Body(2.3e12, 9.5e11, 0, 0, 6.0e26, "")
        f1_x = 3.0778909792377348925408900883295793636769308115458502958210237e22
        f1_y = 1.7757063341756162841582058201901419405828446989687597860505906e22
        # Test force exerted by Saturn on the Sun.
        self.assertAlmostEqual(sun.calc_force_exerted_by_x(saturn), f1_x, delta=1e7)
        self.assertAlmostEqual(sun.calc_force_exerted_by_y(saturn), f1_y, delta=1e7)

        # Test force exerted by Sun on Saturn. This should be symmetric.
        self.assertAlmostEqual(saturn.calc_force_exerted_by_x(sun), -f1_x, delta=1e7)
        self.assertAlmostEqual(saturn.calc_force_exerted_by_y(sun), -f1_y, delta=1e7)


            