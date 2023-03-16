#!/usr/bin/env python3
from brain_games import cli
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_OF_ROUNDS = 3


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(0, 100)
    answer = 'yes' if is_even(number) else 'no'
    return (str(number), answer)


def main():
    name = cli.welcome_user()
    print(DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        number = random.randint(0, 100)
        print(number)
        answer = input('Your answer: ')
        state = "yes" if is_even(number) is True else "no"
        if answer != state:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'\nLet's try again, {2}!".format(answer, state, name))
            return
        else:
            print('Correct!')
    print("Congratulations, {}!".format(name))
            
if __name__ == "__main__":
    main()
