"""
Testing Module For the Code Base
"""

from Code_Base.vendingMachine import *


def test1(product, coin, id):
    print("Test Case {}".format(id))
    print(':-:' * 50)
    vm1 = VendingMachineFactory.create_vending_machine()
    tmp = vm1.select_product_and_get_price(product)
    print(tmp[0])
    if not tmp[1]:
        print("\n")
        print("\n")
        return
    print("Please Insert Coins ->")
    for c in coin:
        vm1.insert_coin(c)
    tmp = vm1.collect_product_and_change()
    if tmp.get_first() == -1:
        print("\n")
        print("\n")
        return
    cn = tmp.get_second()
    if cn:
        print("Here is your {} and change of {} distributed as {}.".format(tmp.get_first(), sum(cn), cn))
    else:
        print("Here is your {}".format(tmp.get_first()))
    print('---------End Of Day--------')
    vm1.print_status()
    print("\n")
    print("\n")
    return


if __name__ == '__main__':
    test1(Pepsi(), [Nickel(), Quarter()], 1)  # When Under Paying for product
    test1(Pepsi(), [Dime(), Quarter()], 2)  # When Paying Perfectly
    test1(Pepsi(), [Quarter(), Quarter()], 3)  # When Over Paying for product
