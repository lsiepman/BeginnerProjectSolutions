# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:56:42 2020.

Armstrong Number

Define a function that allows the user to check whether a given number
is armstrong number or not.
Hint: To do this, first determine the number of digits of the given number.
Call that n. Then take every digit in the number and raise it to the nth power.
Add them, and if your answer is the original number then it is an
Armstrong number.
    Example: Take 1634. Four digits.
    So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634.
    So 1634 is an Armstrong number.
    Tip: All single digit numbers are Armstrong numbers.

@author: laura
"""

class Armstrong:
    """Find whether an input is an Armstrong Number."""

    def __init__(self):
        self.get_input()
        self.get_length()
        self.power_numbers()
        self.get_sum()
        self.test_number()

    def get_input(self):
        self.input = input("Input a number: \n")
        if int(self.input):
            self.input_list = list(self.input)
            self.input_list = [int(i) for i in self.input_list]

    def get_length(self):
        self.length = len(self.input_list)

    def power_numbers(self):
        self.power_digits = []
        for i in self.input_list:
            self.power_digits.append(i**self.length)

    def get_sum(self):
        self.sum = sum(self.power_digits)

    def test_number(self):
        number = str(self.sum)
        if self.input == number:
            print(f"{self.input} is an Armstrong Number.")
        else:
            print(f"{self.input} is NOT an Armstrong Number.")

n = Armstrong()

