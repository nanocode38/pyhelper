import unittest

from pyhelper.color import HEXColor, HSLColor, RGBColor


class ColorTestCase(unittest.TestCase):
    def test_rgb_color(self):
        self.assertEqual(RGBColor.RED, (255, 0, 0))
        self.assertEqual(RGBColor.YELLOW, (255, 255, 0))
        self.assertEqual(RGBColor.to_hex(RGBColor.RED), "#FF0000")
        self.assertEqual(RGBColor.to_hsl(RGBColor.RED), (0.0, 1.0, 0.5))

    def test_hex_color(self):
        self.assertEqual(HEXColor.RED, "#FF0000")
        self.assertEqual(HEXColor.YELLOW, "#FFFF00")
        self.assertEqual(HEXColor.to_rgb(HEXColor.RED), (255, 0, 0))
        self.assertEqual(HEXColor.to_hsl(HEXColor.RED), (0.0, 1.0, 0.5))

    def test_hsl_color(self):
        self.assertEqual(HSLColor.RED, (0.0, 1.0, 0.5))
        self.assertEqual(HSLColor.YELLOW, (60.0, 1.0, 0.5))
        self.assertEqual(HSLColor.to_rgb(HSLColor.RED), (255, 0, 0))
        self.assertEqual(HSLColor.to_hex(HSLColor.RED), "#FF0000")


if __name__ == "__main__":
    unittest.main()
