import unittest
from body import Body

class TestUpdate(unittest.TestCase):
    def test_squirrel(self):
        squirrel = Body(0, 0, 3, 5, 1, "")
        dt = 1
        f_net_x = -5
        f_net_y = -2
        squirrel.update(dt, f_net_x, f_net_y)
        self.assertAlmostEqual(squirrel.xx_vel, -2)
        self.assertAlmostEqual(squirrel.yy_vel, 3)
        self.assertAlmostEqual(squirrel.xx_pos, -2)
        self.assertAlmostEqual(squirrel.yy_pos, 3)