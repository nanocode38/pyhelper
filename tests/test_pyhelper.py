import unittest
import os
import sys

import pyhelper
from pyhelper import *
from test_color import ColorTestCase
from test_mathhelper import MathHelperTestCase
from test_TKhelper import RectTestCase
class TestCase(unittest.TestCase):
    def test_get_version(self):
        self.assertEqual(get_version(), pyhelper.__version__)

    def test_chdir(self):
        father_path = os.path.abspath("..")
        this_path = os.path.abspath(".")
        with chdir(".."):
            self.assertEqual(os.getcwd(), father_path)
        self.assertEqual(os.getcwd(), this_path)

    def test_freopen(self):
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        if not os.path.isfile('test.in'):
            os.chdir('.\\tests\\')
        with open("test.in", "r", encoding="utf-8") as fb:
            with freopen(fb, "stdin"):
                self.assertEqual(sys.stdin, fb)
                file_input = input()
            self.assertEqual(sys.stdin, original_stdin)
            self.assertEqual(file_input, "Hello, World!")
        with open("test.out", "w", encoding="utf-8") as fb:
            with freopen(fb, "stdout"):
                print("Hello, World!")
                self.assertEqual(sys.stdout, fb)
            self.assertEqual(sys.stdout, original_stdout)
        with open("test.out", "r", encoding="utf-8") as fb:
            self.assertEqual(fb.read(), "Hello, World!\n")
        with open("test.out", "w", encoding="utf-8"):
            pass

if __name__ == "__main__":
    unittest.main()
