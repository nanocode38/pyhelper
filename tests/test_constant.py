import unittest
from pyhelper.constant import *

class ConstantTestCase(unittest.TestCase):
    def test_Constant(self):
        const_a = Constant()
        const_a.PI = 3.1415926
        self.assertEqual(const_a.PI, 3.1415926)
        with self.assertRaisesRegex(ConstantError, "Cannot change the value of the Type Constant!"):
            const_a.PI = 3.1415927
        self.assertEqual(const_a.PI, 3.1415926)
        with self.assertRaisesRegex(ConstantError, "Cannot assign a constant to a non-hashable object!"):
            const_a.x = [1, 2, 3]
            
if __name__ == "__main__":
    unittest.main()