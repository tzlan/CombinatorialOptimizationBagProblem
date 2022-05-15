import unittest

from knapsack.backpack import Item


class TestItem(unittest.TestCase):
    def test_init(self):
        item = Item(1, 2, 3)
        self.assertEqual(item.name, 1)
        self.assertEqual(item.weight, 2)
        self.assertEqual(item.value, 3)
    