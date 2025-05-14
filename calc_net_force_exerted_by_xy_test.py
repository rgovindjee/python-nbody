import unittest
from body import Body

class TestCalcNetForceExertedByXy(unittest.TestCase):
    def test_basic(self):
        # Same test as for the two-body case.
        sun = Body(1.0e12, 2.0e11, 0, 0, 2.0e30, "")
        saturn = Body(2.3e12, 9.5e11, 0, 0, 6.0e26, "")
        f1_x = 3.0778909792377348925408900883295793636769308115458502958210237e22
        f1_y = 1.7757063341756162841582058201901419405828446989687597860505906e22
        self.assertAlmostEqual(sun.calc_net_force_exerted_by_x([saturn]),
                               f1_x,
                               delta=1e7)
        self.assertAlmostEqual(sun.calc_net_force_exerted_by_y([saturn]),
                               f1_y,
                               delta=1e7)
        self.assertAlmostEqual(saturn.calc_net_force_exerted_by_x([sun]),
                               -f1_x,
                               delta=1e7)
        self.assertAlmostEqual(saturn.calc_net_force_exerted_by_y([sun]),
                               -f1_y,
                               delta=1e7)
    
    def test_three_body(self):
        samh = Body(1.0, 0.0, 3.0, 4.0, mass=10.0, img_file_name="")
        aegir = Body(3.0, 3.0, 3.0, 4.0, mass=5.0, img_file_name="")
        rocinante = Body(5.0, -3.0, 3.0, 4.0, mass=50, img_file_name="")

        # Don't include samh in the list
        bodys = [aegir, rocinante]
        self.assertAlmostEqual(samh.calc_net_force_exerted_by_x(bodys), 1.2095019349547030093793207446983917630857760245417029126554953e-9)
        self.assertAlmostEqual(samh.calc_net_force_exerted_by_y(bodys), -5.8694709756794548593101888295241235537133596318744563101675e-10)
    
    def test_three_body_including_self(self):
        samh = Body(1.0, 0.0, 3.0, 4.0, mass=10.0, img_file_name="")
        aegir = Body(3.0, 3.0, 3.0, 4.0, mass=5.0, img_file_name="")
        rocinante = Body(5.0, -3.0, 3.0, 4.0, mass=50, img_file_name="")

        # Include samh in the list
        bodys = [samh, aegir, rocinante]
        self.assertAlmostEqual(samh.calc_net_force_exerted_by_x(bodys), 1.2095019349547030093793207446983917630857760245417029126554953e-9)
        self.assertAlmostEqual(samh.calc_net_force_exerted_by_y(bodys), -5.8694709756794548593101888295241235537133596318744563101675e-10)
    

