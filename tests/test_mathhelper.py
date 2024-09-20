import unittest

from pyhelper.mathhelper import *

# noinspection PyTypeChecker
class MathHelperTestCase(unittest.TestCase):
    def setUp(self):
        self.array1 = Array([1, 2, 3, 4, 5])
        self.array2 = Array([1, 2, 3, 4, 5])
        self.array3 = Array([6, 7, 8, 9, 10])

    def test_equality(self):
        self.assertEqual(self.array1, self.array2)
        self.assertNotEqual(self.array1, self.array3)

    def test_addition(self):
        result = self.array1 + self.array3
        expected = Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(result, expected)

    def test_count(self):
        count = self.array1.count(3)
        self.assertEqual(count, 1)

    def test_index(self):
        index = self.array1.index(4)
        self.assertEqual(index, 3)

    def test_type_checking(self):
        with self.assertRaises(TypeError):
            Array([1, 2, 3, 4, 5], dtype=str)

        with self.assertRaises(TypeError):
            self.array1[0] = '6'

        with self.assertRaises(TypeError):
            self.array1 + [6, 7, 8, 9, 10]

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

    def test_Stack(self):
        import array
        from pyhelper.mathhelper import Stack, StackIsCloseError, StackOverFlowError, StackUnderFlowError
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        with self.assertRaises(StackUnderFlowError):
            s.pop()
        s = Stack(size=2)
        s.push(1)
        s.push(2)
        with self.assertRaises(StackOverFlowError):
            s.push(3)
        s = Stack(infuse=array.array('i'))
        s.push(1)
        s.push(2)
        with self.assertRaises(TypeError):
            s.push(1.5)
        s.lock()
        with self.assertRaises(StackIsCloseError):
            s.push(3)
        s.unlock()
        self.assertEqual(s.pop(), 2)
        # [1]
        s += array.array('i', [1, 3, 2])
        self.assertEqual(list(s.get_list()), [1, 1, 3, 2])
        self.assertFalse(s > [1, 3])
        # [1, 1, 3, 2]
        self.assertTrue(s == Stack(array.array('i', [1, 1, 3, 2])))
        self.assertFalse(s < Stack([1]))
        self.assertEqual(len(s), 4)
        self.assertEqual(s[0], s[1])
        self.assertEqual(s[3], 2)
        s[2] = 9
        self.assertEqual(s[2], 9)
        self.assertEqual(list(s.get_list()), [1, 1, 9, 2])


if __name__ == '__main__':
   unittest.main()