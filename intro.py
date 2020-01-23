"""
This was created as practice for myself. Within the introduction of this book, is the first
program the writer wrote. I wanted to build as close to a mockup to that as a reminder of what I
should already know.
"""

from random import randint


def random_guess():

    random_number = randint(1, 5)

    attempt = 1

    while True:

        guess = int(input("I'm thinking of a number! Try to guess the number I'm thinking of: "))

        if guess < random_number:
            attempt += 1
            print("Too low! Guess again: ")

        elif guess > random_number:
            attempt += 1
            print("Too high! Guess again: ")

        elif guess == random_number:
            print("That's it! You took " + str(attempt) + " tries!")
            break


random_guess()

while True:

    fancy_a_game = input("Do you want to play? (yes/no) ")

    if fancy_a_game == 'yes':
        random_guess()
    elif fancy_a_game == 'no':
        break
