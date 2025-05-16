from nbody import NBody
import unittest

class TestReadBodies(unittest.TestCase):
    def test_read_bodies(self):
        # Test the read_bodies function with a sample file.
        bodies = NBody.read_bodies("data/planets.txt")
        
        # Check the number of bodies read
        self.assertEqual(len(bodies), 5)
        
        # Check the properties of the first body
        # Don't use a large tolerance, as we're reading the values directly
        # and not processing them.
        body = bodies[0]
        # Let's see if you did a good job with str()
        print("\nRead " + str(body))
        self.assertAlmostEqual(body.xx_pos, 1.4960e11)
        self.assertAlmostEqual(body.yy_pos, 0.0)
        self.assertAlmostEqual(body.xx_vel, 0.0)
        self.assertAlmostEqual(body.yy_vel, 2.98e04)
        self.assertAlmostEqual(body.mass, 5.9740e24)
        self.assertEqual(body.img_file_name, "earth.gif")

        # Check the properties of the second body
        body = bodies[1]
        print("Read " + str(body))
        self.assertAlmostEqual(body.xx_pos, 2.2790e11)
        self.assertAlmostEqual(body.yy_pos, 0.0)
        self.assertAlmostEqual(body.xx_vel, 0.0)
        self.assertAlmostEqual(body.yy_vel, 2.41e04)
        self.assertAlmostEqual(body.mass, 6.419e23)
        self.assertEqual(body.img_file_name, "mars.gif")