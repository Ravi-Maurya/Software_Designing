"""
Vending Machine, All the functionality are explained.
"""

from Code_Base.resources.inventory import *
from Code_Base.resources.helper import *
from abc import ABC, abstractmethod


class VendingMachineInterface(ABC):
    """
    Abstract Interface for Vending Machine.
    """

    @abstractmethod
    def select_product_and_get_price(self, item):
        """
        It will check in Inventory if the product item is available
        and give the pricing for that product.
        """
        pass

    @abstractmethod
    def insert_coin(self, coin):
        """
        Insert the Coins to the Coin Inventory and also track the current balance of the user.
        """
        pass

    @abstractmethod
    def refund(self):
        """
        Refund the current coins taken in case of cancellation.
        """
        pass

    @abstractmethod
    def collect_product_and_change(self):
        """
        Will calculate the total amount and update the inventories.
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Reset Everything in Vending Machine.
        """
        pass


class VendingMachine(VendingMachineInterface, ABC):
    """
    Vending Machine that is going to be installed in some place.
    """

    def __init__(self):
        self.__product_inventory = Inventory()
        self.__cash_inventory = Inventory()
        self.__total_sales = 0
        self.__current_balance = 0
        self.__current_product = None
        self.__initialize_inventories()
        self.print_status()

    def __initialize_inventories(self):
        """
        Initialize the Inventories.
        """
        all_products = [Coke(), Pepsi(), Soda()]
        for product in all_products:
            self.__product_inventory.set_item_quantity(product, 5)

        all_coins = [Penny(), Dime(), Nickel(), Quarter()]
        for coin in all_coins:
            self.__cash_inventory.set_item_quantity(coin, 5)

    """
    Test methods for addition and removal
    """

    def test_add_products(self, item):
        self.__product_inventory.add_item(item)

    def test_remove_products(self, item):
        self.__product_inventory.remove_item(item)

    def test_add_coins(self, item):
        self.__cash_inventory.add_item(item)

    def test_remove_coins(self, item):
        self.__cash_inventory.remove_item(item)

    """
    Abstract Methods.
    """

    def select_product_and_get_price(self, item):
        if self.__product_inventory.is_item_available(item):
            self.__current_product = item
            return "You have Selected {} to buy at price of {}.".format(item,
                                                                        self.__current_product.get_item_price()), True
        return "{} is Sold Please Select another Item".format(item), False

    def insert_coin(self, coin):
        self.__current_balance += coin.get_coin_value()
        self.__cash_inventory.add_item(coin)
        print("You have inserted {}".format(coin))

    def update_cash_inventory(self, change):
        """
        Updating the Cash Inventory.
        """
        for ch in change:
            self.__cash_inventory.remove_item(ch)

    def collect_change(self):
        """
        Collect the Change from inventory and update it.
        """
        change_amount = self.__current_balance - self.__current_product.get_item_price()
        change = self.get_change(change_amount)
        if not change:
            return change
        self.update_cash_inventory(change)
        self.__current_balance = 0
        self.__current_product = None
        return change

    def get_change(self, change_amount):
        """
        get the remaining change of the coins from inventory.
        """
        change = []
        if change_amount > 0:
            balance = change_amount
            while balance > 0:
                if balance >= Quarter().get_coin_value() and self.__cash_inventory.is_item_available(Quarter()):
                    change.append(Quarter())
                    balance -= Quarter().get_coin_value()
                    continue
                elif balance >= Dime().get_coin_value() and self.__cash_inventory.is_item_available(Dime()):
                    change.append(Dime())
                    balance -= Dime().get_coin_value()
                    continue
                elif balance >= Nickel().get_coin_value() and self.__cash_inventory.is_item_available(Nickel()):
                    change.append(Nickel())
                    balance -= Nickel().get_coin_value()
                    continue
                elif balance >= Penny().get_coin_value() and self.__cash_inventory.is_item_available(Penny()):
                    change.append(Penny())
                    balance -= Penny().get_coin_value()
                    continue
                else:
                    return []
        return change

    def has_sufficient_change(self):
        """
        Checks if has sufficient change in the inventory to sell the product with available set of coins.
        """
        change_amount = self.__current_balance - self.__current_product.get_item_price()
        if change_amount == 0:
            return True
        if self.get_change(change_amount):
            return True
        return False

    def is_full_paid(self):
        return self.__current_balance >= self.__current_product.get_item_price()

    def not_sufficient_change(self):
        self.__current_product = None
        self.__current_balance = 0

    def collect_product(self):
        """
        Check if product can be sold before transactions in inventory.
        """
        if self.is_full_paid():
            if self.has_sufficient_change():
                self.__product_inventory.remove_item(self.__current_product)
                return self.__current_product
            tmp = "Not Sufficient Change in Cash Inventory.\n" \
                  "Sorry for Inconvenience! Here is your change of {}".format(self.__current_balance)
            self.not_sufficient_change()
            return tmp
        return "Price Not Fully Paid"

    def collect_product_and_change(self):
        product = self.collect_product()
        if type(product) == str:
            print(product)
            return Bucket(-1, [])
        self.__total_sales += self.__current_product.get_item_price()
        change = self.collect_change()
        return Bucket(product, change)

    def refund(self):
        refunds = self.get_change(self.__current_balance)
        if not refunds:
            return refunds
        self.update_cash_inventory(refunds)
        self.__current_balance = 0
        self.__current_product = None
        return refunds

    def reset(self):
        self.__product_inventory = Inventory()
        self.__cash_inventory = Inventory()
        self.__total_sales = 0
        self.__current_balance = 0
        self.__current_product = None

    def print_status(self):
        """
        Prints out the status of Inventories and Total_Sale made by Vending Machine.
        """
        print("Total Sales : {}".format(self.__total_sales))
        print("Current Product Inventory : ")
        self.__product_inventory.show_inventory()
        print("Current Cash Inventory : ")
        self.__cash_inventory.show_inventory()


class VendingMachineFactory:
    """
    Factory Class For Vending Machine
    """

    @staticmethod
    def create_vending_machine():
        return VendingMachine()
