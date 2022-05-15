# coding: utf-8

import pathlib
import time
import logging

from typing import List
from knapsack.backpack import BackPack, Item

logger = logging.getLogger("knapsack")

class Algorithm:
    def __init__(self, input_bag, capacity1, capacity2):
        """Init the algorithm

        :param input_bag: the input data
        :type input_bag: list[Item]
        :param capacity1: the capacity of the first backpack
        :type capacity1: int
        :param capacity2: the capacity of the second backpack
        :type capacity2: int
        """
        self.input_bag = input_bag
        self.input_sorted = None
        self.backpack1 = BackPack(capacity=capacity1)
        self.backpack2 = BackPack(capacity=capacity2)

    def heuristic(self) -> List[Item]:
        """Sort the input bag by the heuristic value

        This method set the heuristic value of each Item in the input_bag.
        This method set a value fot input_sorted attribute.

        The heuristic value is calculated by the ratio between the value and the weight.
        If the weight of an item is bigger than the capacity of the two backpack, the heuristic value is set to 0.

        Example:
            >>> algo = Algorithm(input_bag, capacity1, capacity2)
            >>> algo.input_sorted
            None
            >>> algo.heuristic()
            >>> algo.input_sorted
            [Item(name='0', weight=1, value=1, heuristic=0.1), ...]
        
        :return: the sorted input bag
        :rtype: list[Item]
        """
        for item in self.input_bag:
            # If the weight is too heavy for all the backpacks, we skip it
            if (
                item.weight > self.backpack1.capacity
                and item.weight > self.backpack2.capacity
            ):
                item.heuristic = 0
                logger.debug("The item %s is too heavy", item.name)
                continue
            item.heuristic = float(item.value / item.weight)
            logger.debug("The item %s has a heuristic value of %s", item.name, item.heuristic)
        # Sort the input bag
        self.input_sorted = sorted(
            self.input_bag, key=lambda item: item.heuristic, reverse=True
        )
        return self.input_sorted

    def compute(self):
        """Give the item for the two backpacks

        We'll iterate over the list of our input_sorted.
        Then, we'll try to put the item in the first backpack.
        If the item is too heavy for the first backpack, we'll try to put it in the second backpack.
        If the item is too heavy for the second backpack, we'll skip it.

        Example:
            >>> algo = Algorithm(input_bag, capacity1, capacity2)
            >>> algo.backpack1.items
            []
            >>> algo.compute()
            >>> len(algo.backpack1.items)
            2
        
        :return: the two backpacks
        :rtype: BackPack, BackPack
        """
        if not self.input_sorted:
            self.heuristic()
        for item in self.input_sorted:
            # Check in the first backpack
            if self.backpack1.add_item(item):
                continue
            self.backpack2.add_item(item)
        return self.backpack1.items, self.backpack2.items

    def save_csv(self):
        """Save the result in a csv file
        
        :return: None
        """
        if not self.input_sorted:
            raise ValueError("The input bag is not sorted")
        filename = pathlib.Path.home() / f'knapsack-{time.time():.0f}.csv'
        with open(filename, "w") as f:
            f.write("name,weight,value,heuristic,bag\n")
            # Write the sorted input bag
            for item in self.backpack1.items:
                f.write(f"{item.name},{item.weight},{item.value},{item.heuristic},1\n")
            for item in self.backpack2.items:
                f.write(f"{item.name},{item.weight},{item.value},{item.heuristic},2\n")
        logger.info("The result is saved in %s", filename)
