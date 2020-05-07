# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:59:44 2020.

Hangman Game

    Create a program that selects a random word and then allows the user to guess it in a game of hangman.
    Like the real game, there should be blank spots for each letter in the word, and a part of the body should be added each time the user guesses a letter than is not in the answer.
    You may choose how many wrong turns the user can make until the game ends.
    Subgoals:
        If the user loses, print out the word at the end of the game.
        Create a "give up" option.

@author: laura
"""

import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pyinputplus as pyip


class Hangman:
    """Play hangman"""

    def __init__(self):
        self.choose_word()
        self.guessed = []
        self.mistakes = 0
        self.current_guess()

    def choose_word(self):
        """Computer chooses word."""
        words = []
        with(open("hangman/hangman_words.txt")) as file:
            for line in file:
                words.append(line.strip())

        word = random.choice(words)
        self.word = list(word)
        length = len(self.word)
        self.empty = list("_" * length)
        print("word:", self.empty)

    def current_guess(self):
        """Guess a letter."""
        letter = input("Guess a letter: ").lower()

        # check whether letter was already guessed
        if letter in self.guessed:
            print("Letter already guessed.")
            self.current_guess()


        # add letter to already guessed
        self.guessed.append(letter)


        # check if letter in word
        if letter in self.word:
            idxs = []
            for num, let in enumerate(self.word):
                if let == letter:
                    idxs.append(num)

            for i in idxs:
                self.empty[i] = letter

        else:
            self.mistakes += 1

        # check if game is finished
        if "_" in self.empty and self.mistakes < 10:
            self.show_status()
            self.current_guess()
        elif self.mistakes == 10:
            print("Game over")
            self.show_status(t=5)
            print("The word was:", self.word)

            again = pyip.inputYesNo("Play again? ")

            if again == "yes":
                print("ok")
                self.reset()
            else:
                print("Try again later")

        elif "_" not in self.empty:
            print("You win")

            again = pyip.inputYesNo("Play again? ")

            if again == "yes":
                print("ok")
                self.reset()
            else:
                print("Try again later")
        else:
            print("The computer is confused.")

    def show_status(self, t=1.5):
        """Show current status."""
        print(self.empty)
        im = f"hangman/hangman_{self.mistakes}.png"
        im_open = Image.open(im)
        im_np = np.asarray(im_open)
        plt.imshow(im_np)
        plt.pause(t)
        plt.close()
        print(f"Already guessed: {sorted(self.guessed)}")

    def reset(self):
        """Play a new game."""
        self.choose_word()
        self.guessed = []
        self.mistakes = 0
        self.current_guess()

play = Hangman()



