import unittest

from pyhelper.TKhelper import Rect 

class RectTestCase(unittest.TestCase):
    def setUp(self):
        self.rect = Rect(10, 20, 30, 40)

    def test_initialization(self):
        self.assertEqual(self.rect.x, 10)
        self.assertEqual(self.rect.y, 20)
        self.assertEqual(self.rect.w, 20)
        self.assertEqual(self.rect.h, 20)

    def test_properties(self):
        self.assertEqual(self.rect.width, 20)
        self.assertEqual(self.rect.height, 20)
        self.assertEqual(self.rect.size, (20, 20))
        self.assertEqual(self.rect.left, 10)
        self.assertEqual(self.rect.top, 20)
        self.assertEqual(self.rect.right, 30)
        self.assertEqual(self.rect.bottom, 40)
        self.assertEqual(self.rect.centerx, 20)
        self.assertEqual(self.rect.centery, 30)
        self.assertEqual(self.rect.center, (20, 30))
        self.assertEqual(self.rect.topleft, (10, 20))
        self.assertEqual(self.rect.topright, (30, 20))
        self.assertEqual(self.rect.bottomleft, (10, 40))
        self.assertEqual(self.rect.bottomright, (30, 40))
        self.assertEqual(self.rect.midleft, (10, 30))
        self.assertEqual(self.rect.midright, (30, 30))
        self.assertEqual(self.rect.midtop, (20, 20))
        self.assertEqual(self.rect.midbottom, (20, 40))

    def test_setters(self):
        self.rect.width = 25
        self.assertEqual(self.rect.width, 25)
        self.rect.height = 25
        self.assertEqual(self.rect.height, 25)
        self.rect.size = (30, 30)
        self.assertEqual(self.rect.size, (30, 30))
        self.rect.left = 15
        self.assertEqual(self.rect.left, 15)
        self.rect.top = 25
        self.assertEqual(self.rect.top, 25)
        self.rect.right = 35
        self.assertEqual(self.rect.right, 35)
        self.rect.bottom = 45
        self.assertEqual(self.rect.bottom, 45)
        self.rect.centerx = 25
        self.assertEqual(self.rect.centerx, 25)
        self.rect.centery = 35
        self.assertEqual(self.rect.centery, 35)
        self.rect.center = (25, 35)
        self.assertEqual(self.rect.center, (25, 35))
        self.rect.topleft = (15, 25)
        self.assertEqual(self.rect.topleft, (15, 25))
        self.rect.topright = (35, 25)
        self.assertEqual(self.rect.topright, (35, 25))
        self.rect.bottomleft = (15, 45)
        self.assertEqual(self.rect.bottomleft, (15, 45))
        self.rect.bottomright = (35, 45)
        self.assertEqual(self.rect.bottomright, (35, 45))
        self.rect.midleft = (15, 35)
        self.assertEqual(self.rect.midleft, (15, 35))
        self.rect.midright = (35, 35)
        self.assertEqual(self.rect.midright, (35, 35))
        self.rect.midtop = (25, 25)
        self.assertEqual(self.rect.midtop, (25, 25))
        self.rect.midbottom = (25, 45)
        self.assertEqual(self.rect.midbottom, (25, 45))

    def test_move(self):
        new_rect = self.rect.move(5, 5)
        self.assertEqual(new_rect.x, 5)
        self.assertEqual(new_rect.y, 5)
        self.assertEqual(new_rect.w, 20)
        self.assertEqual(new_rect.h, 20)

    def test_move_ip(self):
        self.rect.move_ip(5, 5)
        self.assertEqual(self.rect.x, 5)
        self.assertEqual(self.rect.y, 5)

    def test_copy(self):
        copy_rect = self.rect.copy()
        self.assertEqual(copy_rect.x, self.rect.x)
        self.assertEqual(copy_rect.y, self.rect.y)
        self.assertEqual(copy_rect.w, self.rect.w)
        self.assertEqual(copy_rect.h, self.rect.h)

    def test_repr(self):
        self.assertEqual(repr(self.rect), f"<Rect(10, 20, 30, 40) at {id(self.rect)}>")

if __name__ == "__main__":
    unittest.main()