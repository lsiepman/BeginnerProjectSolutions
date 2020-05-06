# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:59:05 2020.

Fibonacci Sequence

Define a function that allows the user to find the value of the nth term
in the sequence.
- To make sure you've written your function correctly, test the first
10 numbers of the sequence.
- You can assume either that the first two terms are 0 and 1
 or that they are both 1.
- There are two methods you can employ to solve the problem.
One way is to solve it using a loop and the other way is to use recursion.


@author: laura
"""


class Fibonacci:
    """Find nth Fibonacci numbers."""

    def __init__(self, nth):
        self.nth = nth
        self.start = [0, 1]
        self.recur_num = self.start.copy()

    def solve_loop(self):
        """Find the nth Fibonacci number using a for loop."""
        nums = self.start
        for i in range(2, self.nth):
            nums.append(nums[-1] + nums[-2])

        print(f"{nums[-1]} is Fibonacci number {self.nth}")

    def solve_recursion(self):
        """Find the nth Fibonacci number using recursion"""
        new_num = self.recur_num[-1] + self.recur_num[-2]
        self.recur_num.append(new_num)

        if len(self.recur_num) < self.nth:
            self.solve_recursion()
        else:
            print(f"{self.recur_num[-1]} is Fibonacci number {self.nth}")

n = Fibonacci(10)
n.solve_loop()
n.solve_recursion()
