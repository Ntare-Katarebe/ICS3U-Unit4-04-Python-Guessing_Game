#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program guesses your number
#    with numbers inputted from the user

import random


def main():
    # This function guesses your number

    # input
    random_number = random.randint(0, 9)

    # process/output
    while True:
        guessed_string = input("Enter the number between 0 - 9: ")
        try:
            guessed_number = int(guessed_string)
            if guessed_number < random_number:
                print("Your guess is too low")
            elif guessed_number > random_number:
                print("Your guess is too high")
            else:
                print("You guessed correct")
                break
        except Exception:
            print("{} is not an integer".format(guessed_string))

    print("Thanks for playing")
    print("\nDone")


if __name__ == "__main__":
    main()
