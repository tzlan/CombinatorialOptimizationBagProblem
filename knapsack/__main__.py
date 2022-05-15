# coding: utf-8

from knapsack.algorithm import Algorithm
from knapsack.backpack import Item
import random
import logging

logger = logging.getLogger("knapsack")


def random_input():
    items = []
    for i in range(20):
        items.append(
            Item(
                name=str(i), weight=random.randint(1, 100), value=random.randint(1, 100)
            )
        )
    return items


def main(input_bag, capacity1, capacity2):
    logger.info("Capacity1: %s, Capacity2: %s", capacity1, capacity2)
    logger.info("Generated %s items", len(input_bag))
    algo = Algorithm(input_bag, capacity1, capacity2)
    algo.heuristic()
    algo.compute()
    algo.save_csv()
    return algo.backpack1.items, algo.backpack2.items


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(name)s %(levelname)s %(message)s"
    )
    main(
        input_bag=random_input(),
        capacity1=random.randint(50, 100),
        capacity2=random.randint(50, 100),
    )
