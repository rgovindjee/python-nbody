import unittest
from body import Body

class TestBody(unittest.TestCase):
    def test_initialization(self):
        # Test initialization with dummy values.
        body = Body(1.5, 2.6, 3.7, 4.1, 123981203.10283, "data/test_file.gif")
        self.assertEqual(body.xx_pos, 1.5)
        self.assertEqual(body.yy_pos, 2.6)
        self.assertEqual(body.xx_vel, 3.7)
        self.assertEqual(body.yy_vel, 4.1)
        self.assertEqual(body.mass, 123981203.10283)
        self.assertEqual(body.img_file_name, "data/test_file.gif")
    
    def test_multiple_initialization(self):
        # Make sure multiple instances can be created with their own values.
        body1 = Body(1.5, 2.6, 3.7, 4.1, 123981203.10283, "data/test_file.gif")
        body2 = Body(10.5, 20.6, 30.7, 40.1, 1239812030.10283, "data/test_file2.gif")

        self.assertEqual(body1.xx_pos, 1.5)
        self.assertEqual(body1.yy_pos, 2.6)
        self.assertEqual(body1.xx_vel, 3.7)
        self.assertEqual(body1.yy_vel, 4.1)
        self.assertEqual(body1.mass, 123981203.10283)
        self.assertEqual(body1.img_file_name, "data/test_file.gif")

        self.assertEqual(body2.xx_pos, 10.5)
        self.assertEqual(body2.yy_pos, 20.6)
        self.assertEqual(body2.xx_vel, 30.7)
        self.assertEqual(body2.yy_vel, 40.1)
        self.assertEqual(body2.mass, 1239812030.10283)
        self.assertEqual(body2.img_file_name, "data/test_file2.gif")

    def test_copy_body_basic(self):
        # Test copying a body.
        body1 = Body(1.5, 2.6, 3.7, 4.1, 123981203.10283, "data/test_file.gif")
        body2 = Body.copy(body1)

        self.assertEqual(body1.xx_pos, body2.xx_pos)
        self.assertEqual(body1.yy_pos, body2.yy_pos)
        self.assertEqual(body1.xx_vel, body2.xx_vel)
        self.assertEqual(body1.yy_vel, body2.yy_vel)
        self.assertEqual(body1.mass, body2.mass)
        self.assertEqual(body1.img_file_name, body2.img_file_name)

    def test_copy_body_modification(self):
        body1 = Body(1.5, 2.6, 3.7, 4.1, 123981203.10283, "data/test_file.gif")
        body2 = Body.copy(body1)

        self.assertEqual(body1.xx_pos, body2.xx_pos)
        self.assertEqual(body1.yy_pos, body2.yy_pos)
        self.assertEqual(body1.xx_vel, body2.xx_vel)
        self.assertEqual(body1.yy_vel, body2.yy_vel)
        self.assertEqual(body1.mass, body2.mass)
        self.assertEqual(body1.img_file_name, body2.img_file_name)

        # Modify body2 and check that body1 remains unchanged.
        body2.xx_pos = 100.0
        body2.img_file_name = "data/modified_test_file.gif"
        self.assertEqual(body2.xx_pos, 100.0)
        self.assertEqual(body2.img_file_name, "data/modified_test_file.gif")
        self.assertNotEqual(body1.xx_pos, body2.xx_pos)
        self.assertNotEqual(body1.img_file_name, body2.img_file_name)

        # Modify body1 and check that body2 remains unchanged.
        body1.xx_pos = 200.0
        body1.img_file_name = "data/another_test_file.gif"
        self.assertEqual(body1.xx_pos, 200.0)
        self.assertEqual(body1.img_file_name, "data/another_test_file.gif")
        self.assertNotEqual(body2.xx_pos, body1.xx_pos)
        self.assertNotEqual(body2.img_file_name, body1.img_file_name)
