# -*- coding: utf-8 -*-
"""
Rock, Paper, Scissors.

Created on Sun Mar 8 10:48:11 2020

@author: Laura

Rock Paper Scissors Game
    - Create a rock-paper-scissors game.
    - Ask the player to pick rock, paper or scissors.
    - Have the computer chose its move.
    - Compare the choices and decide who wins.
    - Print the results.

    - Give the player the option to play again.
    - Keep a record of the score (e.g. Player: 3 / Computer: 6).
"""

import random


class RockPaperScissors:
    """Playing Rock, Paper, Scissors."""

    def __init__(self):
        """Set initial scores and values. Play game."""
        self.player_score = 0
        self.computer_score = 0
        self.player_choice = None
        self.computer_choice = None
        self.play_again = True

        self.play_game()

    def print_score(self):
        """Print scores."""
        print("Player score:", self.player_score)
        print("Computer score:", self.computer_score)

    def input_player(self):
        """Choose rock, paper, scissors."""
        player_choice = input("Choose rock, paper, or scissors: ")
        player_choice = player_choice.lower()
        print("You chose " + player_choice)

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Please try again.")
            player_choice = None
            self.input_player()

        else:
            self.player_choice = player_choice

    def input_computer(self):
        """Assign rock, paper, scissors to computer."""
        options = ["rock", "paper", "scissors"]
        self.computer_choice = random.choice(options)
        print("The computer chose " + self.computer_choice)

    def choose_winner(self):
        """Determine winner."""
        # draw
        if self.player_choice == self.computer_choice:
            print("Draw")

        # you chose rock
        elif (self.player_choice == "rock"
              and self.computer_choice == "paper"):
            print("Computer wins")
            self.computer_score += 1

        elif (self.player_choice == "rock"
              and self.computer_choice == "scissors"):
            print("Player wins")
            self.player_score += 1

        # you chose paper
        elif (self.player_choice == "paper"
              and self.computer_choice == "scissors"):
            print("Computer wins")
            self.computer_score += 1

        elif (self.player_choice == "paper"
              and self.computer_choice == "rock"):
            print("Player wins")
            self.player_score += 1

        # you chose scissors
        elif (self.player_choice == "scissors"
              and self.computer_choice == "rock"):
            print("Computer wins")
            self.computer_score += 1

        elif (self.player_choice == "scissors"
              and self.computer_choice == "paper"):
            print("Player wins")
            self.player_score += 1

        else:
            print("unknown error")

    def play_game_again(self):
        """Play again."""
        play_again = input("Play again (yes/no)? ")
        if play_again.lower() in ["y", "yes", "ye"]:
            self.play_again = True
        else:
            self.play_again = False

    def print_final_score(self):
        """Print final score."""
        if self.player_score > self.computer_score:
            print("Player wins")
        elif self.computer_score > self.player_score:
            print("Computer wins")
        else:
            print("Draw")

    def play_game(self):
        """Play the actual game."""
        while self.play_again is True:
            self.input_player()
            self.input_computer()
            self.choose_winner()
            self.print_score()
            self.play_game_again()

        self.print_final_score()


# Play the game
play = RockPaperScissors()
