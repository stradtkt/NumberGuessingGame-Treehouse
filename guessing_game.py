"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
For this first project we will be using Workspaces.
NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
"""

import random


high_score = 0


def start_game():
    count = 0

    def welcome_message():
        print(""" 
 _____ _        _  _            _              ___                _            ___                
|_   _| |_  ___| \| |_  _ _ __ | |__  ___ _ _ / __|_  _ ___ _____(_)_ _  __ _ / __|__ _ _ __  ___ 
  | | | ' \/ -_) .` | || | '  \| '_ \/ -_) '_| (_ | || / -_|_-<_-< | ' \/ _` | (_ / _` | '  \/ -_)
  |_| |_||_\___|_|\_|\_,_|_|_|_|_.__/\___|_|  \___|\_,_\___/__/__/_|_||_\__, |\___\__,_|_|_|_\___|
                                                                        |___/  
        """)
        print("Press [q/Q] to quit to quit the game.")

    def random_number():
        number = random.randint(1, 10)
        return number

    def play_again():
        while True:
            try:
                again = input("Do you want to play again?  [y/yes] or [n/no]").lower()
                if again not in ("y", "yes", "n", "no", "q"):
                    raise ValueError("Please enter [y or yes] or [n or no]")
            except ValueError as error:
                print("There has been an error.  Your error is: {}".format(error))
            else:
                if again == "y" or again == "yes":
                    count = 0
                    number = random_number()
                    guess(count, number)
                elif again == "n" or again == "no":
                    print("Okay have a good rest of your day.  Thank you for playing the number guessing game!")
                    exit()

    def guess(count, number):
        global high_score
        if high_score != 0:
            print("Your previous high score is {}, try to beat it!".format(high_score))
        while True:
            try:
                the_guess = input('Guess a number between 1 and 10: ')
                if the_guess == "q" or the_guess == "Q":
                    print("Thank you for playing!")
                    print("Goodbye!")
                    exit()
                if not the_guess.isdigit():
                    raise ValueError("The guess needs to be a digit, please try again.")
                the_guess = int(the_guess)
                if the_guess > 10 or the_guess < 1:
                    raise ValueError("The guess is out of the specified range for the game.  Please try again.")
            except ValueError as error:
                print("There has been an error.  Your error is: {}".format(error))
            else:
                count += 1
                if the_guess == number:
                    print("You guessed the right number!  It took you {} attempts to guess.".format(count))
                    if high_score == 0 or count < high_score:
                        high_score = count
                        print("{} is your new high score!".format(high_score))
                    play_again()
                if the_guess > number:
                    print("The number is lower than that, please try again.")
                if the_guess < number:
                    print("The number is higher than that, please try again.")

    welcome_message()
    number = random_number()
    guess(count, number)


if __name__ == '__main__':
    start_game()
