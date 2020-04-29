"""
Enums and Constants that are going to be used frequently.
"""

from enum import Enum
from abc import ABC


class Singleton:
    """
    Singleton Class For making single instances of the items i.e. coins and products
    """

    def __new__(cls) -> "Singleton":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


"""
---- Products ----
"""


class Products(Enum):
    """
    Enum Class For Products
    """
    COKE = 1
    PEPSI = 2
    SODA = 3


class ProductItem(ABC):
    """
    Abstract Class for Products
    """

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def get_item_price(self):
        return self.item_price

    def get_item_name(self):
        return self.item_name


class Coke(ProductItem, Singleton):
    def __init__(self):
        super(Coke, self).__init__(Products.COKE, 25)

    def __str__(self):
        return "Coke"


class Pepsi(ProductItem, Singleton):
    def __init__(self):
        super(Pepsi, self).__init__(Products.PEPSI, 35)

    def __str__(self):
        return "Pepsi"


class Soda(ProductItem, Singleton):
    def __init__(self):
        super(Soda, self).__init__(Products.SODA, 45)

    def __str__(self):
        return "Soda"


"""
---- Coins ----
"""


class Coins(Enum):
    """
    Enum Class For Coins
    """
    PENNY = 1
    NICKEL = 2
    DIME = 3
    QUARTER = 4


class CoinValue(ABC):
    """
    Abstract Class for Coins
    """

    def __init__(self, coin_id, coin_value):
        self.coin_id = coin_id
        self.coin_value = coin_value

    def get_coin_value(self):
        return self.coin_value


class Penny(CoinValue, Singleton):
    def __init__(self):
        super(Penny, self).__init__(Coins.PENNY, 1)

    def __str__(self):
        return "Penny"


class Nickel(CoinValue, Singleton):
    def __init__(self):
        super(Nickel, self).__init__(Coins.NICKEL, 5)

    def __str__(self):
        return "Nickel"


class Dime(CoinValue, Singleton):
    def __init__(self):
        super(Dime, self).__init__(Coins.DIME, 10)

    def __str__(self):
        return "Dime"


class Quarter(CoinValue, Singleton):
    def __init__(self):
        super(Quarter, self).__init__(Coins.QUARTER, 25)

    def __str__(self):
        return "Quarter"


if __name__ == '__main__':
    print(Coke().get_item_name(), Coke().get_item_price())
    print(Products.COKE == Coke().get_item_name())

"""
Bucket is Used for getting the Product and Exchange of Coins from Vending Machine.
"""


class Bucket:
    def __init__(self, product_name, coin_change):
        self.product_name = product_name
        self.coin_change = coin_change

    def get_first(self):
        return self.product_name

    def get_second(self):
        res = []
        for coin in self.coin_change:
            res.append(coin.get_coin_value())
        return res
