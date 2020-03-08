# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:48:03 2020.

99 Bottles

@author: laura


Goals:
    - Create a program that prints out every line to the song
    "99 bottles of beer on the wall."
    - Do not use a list for all of the numbers,
    and do not manually type them all in. Use a built in function instead.
    - Besides the phrase "take one down,"
    you may not type in any numbers/names of numbers
    directly into your song lyrics.
    - Remember, when you reach 1 bottle left,
    the word "bottles" becomes singular.
"""


class BeerBottles:
    """99 Beer Bottles song."""

    def __init__(self):
        """Initialize values and print songs."""
        self.num_bottles = 99
        self.lyric_bottles = "bottles"
        self.continue_song = True

        self.sing_song()

    def count_down(self):
        """Count down the number of bottles."""
        self.num_bottles -= 1

    def check_count(self):
        """Check if the word 'bottle' has to be singular."""
        if self.num_bottles == 1:
            self.lyric_bottles = "bottle"

        elif self.num_bottles == 0:
            self.num_bottles = "No more"
            self.lyric_bottles = "bottles"
            self.continue_song = False

    def finish_song(self):
        """Print correct song conclusion."""
        self.lyric_bottles = "bottles"
        self.print_first_line()
        print("Go to the store and buy some more,",
              "99 bottles of beer on the wall.")

    def print_first_line(self):
        """Print the first line of each verse."""
        if isinstance(self.num_bottles, str):
            text = self.num_bottles.capitalize()
        else:
            text = self.num_bottles

        print("{0} {1} of beer on the wall, {2} {1} of beer.".format(
            text, self.lyric_bottles, self.num_bottles))

    def print_second_line(self):
        """Print the second line in each verse."""
        if isinstance(self.num_bottles, str):
            self.num_bottles = self.num_bottles.lower()

        print("Take one down and pass it around,",
              "{0} {1} of beer on the wall.".format(self.num_bottles,
                                                    self.lyric_bottles))
        print("\n")

    def sing_song(self):
        """Sing the song."""
        while self.continue_song is True:
            self.print_first_line()
            self.count_down()
            self.check_count()
            self.print_second_line()
        self.finish_song()


beer = BeerBottles()
