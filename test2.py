import unittest
from math import pi
from main import circle_area, area_rectangle

class TestAreas(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(circle_area(3), pi * (3 ** 2))
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi * (2.5 ** 2))

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_area(-2)
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            circle_area('five')
        with self.assertRaises(TypeError):
            circle_area(5 + 2j)
        with self.assertRaises(TypeError):
            circle_area([16, 42])
        with self.assertRaises(TypeError):
            circle_area([22])
        with self.assertRaises(TypeError):
            circle_area(True)

    
if __name__ == '__main__':
    unittest.main()
