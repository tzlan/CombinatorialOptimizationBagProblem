import unittest

from knapsack.backpack import Item
from knapsack.algorithm import Algorithm


class TestAlgorithm(unittest.TestCase):
    def setUp(self) -> None:
        self.input_bag = [
            Item(name="E", weight=10, value=1),
            Item(name="B", weight=24, value=3),
            Item(name="C", weight=150, value=12),
            Item(name="A", weight=1, value=1),
            Item(name="D", weight=1, value=5),
        ]
        return super().setUp()

    def test_heuristic(self):
        algo = Algorithm(self.input_bag, capacity1=50, capacity2=30)
        algo.heuristic()
        self.assertListEqual([e.name for e in algo.input_sorted], ['D', 'A', 'B', 'E', 'C'])
        self.assertListEqual([e.heuristic for e in algo.input_sorted], [5.0, 1.0,  0.125, 0.1, 0])
        self.assertEqual(algo.input_sorted[0].heuristic, 5.0)
        self.assertEqual(algo.input_sorted[-1].heuristic, 0)

    def test_compute(self):
        algo = Algorithm(self.input_bag, capacity1=50, capacity2=30)
        algo.compute()
        name_backpack1 = [e.name for e in algo.backpack1.items]
        name_backpack2 = [e.name for e in algo.backpack2.items]
        self.assertListEqual(name_backpack1, ['D', 'A', 'B', 'E'])
        self.assertListEqual(name_backpack2, [])
        