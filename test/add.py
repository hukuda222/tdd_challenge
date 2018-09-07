import unittest

from add import Add


class TestAdd(unittest.TestCase):

    def test_add(self):
        add = Add()
        self.assertEqual(add.add(1, 2), 3)
        self.assertEqual(add.add(-1, 2), 1)
        self.assertEqual(add.add(0, 0), 0)
