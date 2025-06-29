import unittest

from pyhelper.mathhelper import *


# noinspection PyTypeChecker
class MathHelperTestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(TypeError):
            fibonacci(1.5)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(37))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(43))
        self.assertTrue(is_prime(47))
        self.assertTrue(is_prime(53))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(105))
        self.assertFalse(is_prime(292))
        self.assertFalse(is_prime(63))
        self.assertFalse(is_prime(39))


if __name__ == "__main__":
    unittest.main()
