"""
Inventory will be used to store the data for the Coins as well as Products.
"""
from collections import defaultdict


class Inventory:
    """
    Inventory Class with all the functionality.
    """
    def __init__(self):
        self.inventory = defaultdict(lambda: 0)

    def get_item_quantity(self, item):
        return self.inventory[item]

    def set_item_quantity(self, item, quantity):
        self.inventory[item] = quantity

    def add_item(self, item):
        self.inventory[item] += 1

    def remove_item(self, item):
        self.inventory[item] -= 1

    def is_item_available(self, item):
        return self.inventory[item] > 0

    def show_inventory(self):
        print('+' * 50)
        for key in self.inventory.keys():
            if self.inventory[key] >= 0:
                print("{} \t\t {}".format(key, self.inventory[key]))
        print('-' * 50)

    def clear_inventory(self):
        self.inventory = defaultdict(lambda: 0)
