import unittest
from BioContactMap.helpers import find_center, find_distance
import numpy as np

class TestHelpers(unittest.TestCase):

    def test_find_center(self):
        # Test for a simple 3-point residue
        x_coords = [1.0, 2.0, 3.0]
        y_coords = [1.0, 2.0, 3.0]
        z_coords = [1.0, 2.0, 3.0]

        # We expect the center to be the average of the coordinates
        expected_x = np.mean(x_coords)
        expected_y = np.mean(y_coords)
        expected_z = np.mean(z_coords)

        # Call find_center with the mock coordinates
        x, y, z = find_center(x_coords, y_coords, z_coords)

        # Check that the center matches the expected values
        self.assertAlmostEqual(x, expected_x)
        self.assertAlmostEqual(y, expected_y)
        self.assertAlmostEqual(z, expected_z)

    def test_find_distance(self):
        # Test for simple distance calculation between two points
        x1, y1, z1 = 1.0, 1.0, 1.0
        x2, y2, z2 = 4.0, 5.0, 6.0

        # Using Euclidean distance formula:
        # distance = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)
        expected_distance = np.sqrt((4.0 - 1.0)**2 + (5.0 - 1.0)**2 + (6.0 - 1.0)**2)

        # Call find_distance with the mock coordinates
        distance = find_distance(x1, y1, z1, x2, y2, z2)

        # Check that the calculated distance matches the expected value
        self.assertAlmostEqual(distance, expected_distance)

    def test_find_distance_zero_distance(self):
        # Test where the two points are the same (should return 0)
        x1, y1, z1 = 1.0, 1.0, 1.0
        x2, y2, z2 = 1.0, 1.0, 1.0

        # The distance between the same point is 0
        expected_distance = 0.0

        # Call find_distance with the same coordinates
        distance = find_distance(x1, y1, z1, x2, y2, z2)

        # Check that the distance is 0
        self.assertEqual(distance, expected_distance)


if __name__ == '__main__':
    unittest.main()