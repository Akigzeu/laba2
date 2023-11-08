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
    def test_valid_inpit_for_rectangle(self):
        self.assertEqual(area_rectangle(3,4),3*4)
        self.assertEqual(area_rectangle(3.8, 4.9), 3.8 * 4.9)
        self.assertEqual(area_rectangle(0, 4), 0 )
        self.assertEqual(area_rectangle(3, 0), 0)
        self.assertEqual(area_rectangle(0.1,0.7),0.1*0.7)

    def test_negative_length_or_width(self):
        with self.assertRaises(ValueError):
            area_rectangle(1,-3)
        with self.assertRaises(ValueError):
            area_rectangle(-7,30)

    def test_invalid_inputs_for_rectangle(self):
        with self.assertRaises(TypeError):
            area_rectangle('five',7)
        with self.assertRaises(TypeError):
            area_rectangle(7,'two')
        with self.assertRaises(TypeError):
            area_rectangle(5 + 2j,7)
        with self.assertRaises(TypeError):
            area_rectangle(13,5 + 2j)
        with self.assertRaises(TypeError):
            area_rectangle([16, 42],7)
        with self.assertRaises(TypeError):
            area_rectangle(11,[16, 42])
        with self.assertRaises(TypeError):
            area_rectangle(True,'two')
        with self.assertRaises(TypeError):
            area_rectangle(False,'two')
if __name__ == '__main__':
    unittest.main()
