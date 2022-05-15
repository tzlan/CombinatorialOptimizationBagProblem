# coding: utf-8

import logging

logger = logging.getLogger("knapsack")

class BackPack:
    """A backpack is a list of items with a capacity"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.remaining = capacity
        self.items = []

    def add_item(self, item):
        """Add an item to the backpack

        We check if the item can be added to the backpack.
        If the capacity is not enough, we return False.
        If the capacity is enough, we add the item to the backpack and return True.

        :param item: the item to add
        :type item: Item
        :return: True if the item has been added, False otherwise
        :rtype: bool
        """
        if self.remaining >= item.weight:
            self.items.append(item)
            self.remaining -= item.weight
            logger.debug("The item %s has been added to the backpack", item.name)
            return True
        logger.debug("The item %s has not been added to the backpack", item.name)
        return False


class Item:
    """Content of the backpack"""

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        # Permet d'attribuer l'indice dans une liste
        self.heuristic = 0

    def __str__(self) -> str:
        return "Item(name={}, weight={}, value={}, heuristic={})".format(
            self.name, self.weight, self.value, self.heuristic
        )

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self):
        return hash(self.name) ^ hash(self.weight) ^ hash(self.value)

    def __eq__(self, other):
        return (
            isinstance(other, Item)
            and self.name == other.name
            and self.weight == other.weight
            and self.value == other.value
        )
