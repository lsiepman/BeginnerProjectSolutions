# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 23:58:14 2020.

What's My Number?

Between 1 and 1000, there is only 1 number that meets the following criteria:

    - The number has two or more digits.
    - The number is prime.
    - The number does NOT contain a 1 or 7 in it.
    - The sum of all of the digits is less than or equal to 10.
    - The first two digits add up to be odd.
    - The second to last digit is even and greater than 1.
    - The last digit is equal to how many digits are in the number.

@author: laura
"""

import re

ALL_NUMS = list(range(1, 1001))


class WhatsMyNumber:
    """Find the number in the 'What's my number' challenge."""

    def __init__(self, input_numbers):
        """Calculate answer.

        Parameters
        ----------
        input_numbers : list of int
            List of input numbers.

        Returns
        -------
        None.
        """
        self.number = input_numbers
        self.find_more_than_2_digits()
        self.find_all_primes()
        self.remove_one_seven()
        self.sum_of_digits()
        self.sum_of_first_two_digits()
        self.check_second_to_last()
        self.check_last_digit()
        print("The answer is", self.number)

    def find_more_than_2_digits(self):
        """Exclude numbers with less than two digits."""
        more_than_two_digits = []
        for i in self.number:
            if re.search(r"\d{2,}", str(i)):
                more_than_two_digits.append(i)

        self.number = more_than_two_digits

    @staticmethod
    def find_prime(num):
        """Discover if the number is prime."""
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                return num

    def find_all_primes(self):
        """Find all primes in list."""
        primes = []
        for number in self.number:
            value = self.find_prime(number)
            if value:
                primes.append(value)

        self.number = primes

    def remove_one_seven(self):
        """Remove numbers containing ones and sevens."""
        clean = []
        for i in self.number:
            if re.search("1", str(i)) or re.search("7", str(i)):
                continue
            clean.append(i)

        self.number = clean

    def sum_of_digits(self):
        """Exclude numbers that do not have a digit sum of 10 or less."""
        digit_sum = []
        for i in self.number:
            vals = list(str(i))
            vals = [int(j) for j in vals]

            if sum(vals) <= 10:
                digit_sum.append(i)

        self.number = digit_sum

    def sum_of_first_two_digits(self):
        """Exclude numbers without odd first two digit sum."""
        odd_sum = []
        for i in self.number:
            vals = list(str(i))[:2]
            vals = [int(j) for j in vals]
            sum_vals = sum(vals)
            if (sum_vals % 2) != 0:
                odd_sum.append(i)

        self.number = odd_sum

    def check_second_to_last(self):
        """Exclude values without an even, > 1, second to last digit."""
        clean = []
        for i in self.number:
            vals = list(str(i))
            val = int(vals[-2])
            if (val % 2) == 0 and val > 1:
                clean.append(i)

        self.number = clean

    def check_last_digit(self):
        """Find numbers with last digit equal to length of number."""
        clean = []
        for i in self.number:
            vals = list(str(i))
            vals = [int(j) for j in vals]
            if vals[-1] == len(vals):
                clean.append(i)
        if len(clean) == 1:
            self.number = clean[0]
        else:
            self.number = clean


ANSWER = WhatsMyNumber(ALL_NUMS)
