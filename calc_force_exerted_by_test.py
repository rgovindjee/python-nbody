import unittest
from body import Body

class TestCalcForceExertedBy(unittest.TestCase):
    def test_basic(self):
        sun = Body(1.0e12, 2.0e11, 0, 0, 2.0e30, "")
        saturn = Body(2.3e12, 9.5e11, 0, 0, 6.0e26, "")
        self.assertAlmostEqual(sun.calc_force_exerted_by(saturn),
                               3.55338512763596004439511653718091009988901220865704772475027746947835e22,
                               delta=1e7)
    
    def test_three_body(self):
        b1 = Body(1.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif")
        b2 = Body(2.0, 1.0, 3.0, 4.0, 4e11, "jupiter.gif")
        b3 = Body(4.0, 5.0, 3.0, 4.0, 5.0, "jupiter.gif")

        self.assertAlmostEqual(b1.calc_force_exerted_by(b2), 133.4)
        self.assertAlmostEqual(b1.calc_force_exerted_by(b3), 6.67e-11)