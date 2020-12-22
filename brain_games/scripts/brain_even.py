#!/usr/bin/env python
import random
from brain_games import cli
from brain_games import engine


def eval(number):
    if number % 2:
        return 'yes'
    elif number % 2 == 0:
        return 'no'


def question_generator():
    return random.randint(0, 100)


def main():
    cli.welcome_user()
    counter = 0
    while (counter < 3):
        question = question_generator()
        the_answer = eval(question)
        if engine.engine(question, the_answer):
            counter += 1
    print('Congradulations, ' + cli.name + '!')


if __name__ == '__main__':
    main()
