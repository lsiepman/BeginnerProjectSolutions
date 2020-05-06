# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:37:39 2020.

Countdown Clock

    - Create a program that allows the user to choose a time and date,
    and then prints out a message at given intervals (such as every second)
    that tells the user how much longer there is until the selected time.
    - If the selected time has already passed,
    have the program tell the user to start over.

@author: laura
"""

import datetime as dt
import time


class CountDownClock:
    """Countdown clock.

    Counts down to a time later today.
    """

    def __init__(self):
        self.input = None
        self.clock()

    def get_input(self):
        """Get target time from user."""
        print("Please input the time in the following format:")
        today = dt.datetime.today().strftime('%Y-%m-%d')
        time_input = input("hh:mm:ss \n")
        target = f"{today} {time_input}"
        self.input = dt.datetime.strptime(target, "%Y-%m-%d %H:%M:%S")

    def fetch_now(self):
        """Fetch now datetime."""
        return dt.datetime.now()

    def compare_times(self):
        """Compare now with target."""
        if self.fetch_now() > self.input:
            print("Input in the past, please start over")
            self.get_input()

        while True:
            time.sleep(1)
            wait = self.input - self.fetch_now()
            wait = wait.seconds
            if wait == 0:
                break
            print(f"{wait} seconds remaining")

        print(f"Target reached, it is now {self.input}")

    def clock(self):
        """Execute countdown."""
        self.get_input()
        self.compare_times()


t = CountDownClock()
