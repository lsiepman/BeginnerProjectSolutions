# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:00:13 2020.

Menu Calculator


@author: laura

Goals:
    - To quickly take orders, your program should allow the user
    to type in a string of numbers and then it should calculate
    the cost of the order.
    - Also, make sure that the program loops so the user can take
    multiple orders without having to restart the program each time.
    - Once the user has entered an order, print out how many of each
    item have been ordered, as well as the total price.
        If an item was not ordered at all, then it should not show up.
"""

from collections import Counter
import pandas as pd

item_num = list(range(1, 10))
item_names = ["Chicken Strips", "French Fries", "Hamburger", "Hotdog",
              "Large Drink", "Medium Drink", "Milk Shake", "Salad",
              "Small Drink"]
item_prices = [3.50, 2.50, 4.00, 3.50, 1.75, 1.50, 2.25, 3.75, 1.25]

menu_restaurant = pd.DataFrame(zip(item_num, item_names, item_prices),
                               columns=["ID", "Items", "Prices"])


class TakeOrders:
    """Collection of functions to take orders."""

    def __init__(self, menu):
        """Initialise values.

        Parameters
        ----------
        menu : pandas dataframe
            Dataframe with items, ids and prices.

        Returns
        -------
        None.
        """
        self.order_string = None
        self.order = None
        self.total_price = 0
        self.menu = menu
        self.work_hours = True

        self.wait_tables()

    def input_order(self):
        """Take the order input."""
        self.order_string = input("Input order: ")

    def split_order(self):
        """Split string of numbers into list of ints."""
        self.order = list(self.order_string)
        self.order = list(map(int, self.order))

    def calc_price(self):
        """Calculate total price."""
        for i in self.order:
            self.total_price += self.menu.loc[
                self.menu["ID"] == i]["Prices"].iloc[0]

        print("Total Price:", self.total_price)

    def count_items(self):
        """Print an overview of all ordered items."""
        item_lst = []
        for i in self.order:
            item_lst.append(self.menu.loc[
                self.menu["ID"] == i]["Items"].iloc[0])

        print(Counter(item_lst))

    def set_values(self):
        """Set initial total price."""
        self.total_price = 0

    def wait_tables(self):
        """Execute all methods."""
        while self.work_hours is True:
            self.set_values()
            self.input_order()
            self.split_order()
            self.calc_price()
            self.count_items()
            next_order = input("Next order? (y/n) ")
            if next_order in ["n", "no"]:
                self.work_hours = False

waiter = TakeOrders(menu_restaurant)
