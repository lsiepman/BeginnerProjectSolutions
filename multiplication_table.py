# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:58:48 2020.

Multiplication Table

Create a program that prints out a multiplication table for the
numbers 1 through 9.
- It should include the numbers 1 through 9 on the top and left axises,
and it should be relatively easy to find the product of two numbers.
Do not simply write out every line manually (ie print('7 14 21 28 35 49 56 63') ).
- As your products get larger, your columns will start to get crooked from
the number of characters on each line. Clean up your table by evenly spacing
columns so it is very easy to find the product of two numbers.
- Allow the user to choose a number to change the size of the table
(so if they type in 12, the table printed out should be a 12x12
multiplication table).

@author: laura
"""

class MultiTable:
    """Print multiplication table."""

    def __init__(self, number):
        self.number = number + 1
        self.create_table()

    def create_table(self):
        for i in range(1, self.number):
            print()
            for j in range(1, self.number):
                print(i * j, end="\t")

table = MultiTable(7)

