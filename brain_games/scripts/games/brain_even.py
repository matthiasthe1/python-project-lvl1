#!/usr/bin/env python
import random
import prompt
from brain_games import engine


def eval(number):
    if number % 2:
        return 'no'
    elif number % 2 == 0:
        return 'yes'


def question_generator():
    return random.randint(0, 100)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    counter = 0
    NUMBER_OF_ROUNDS = 3
    while (counter < NUMBER_OF_ROUNDS):
        question = question_generator()
        the_answer = eval(question)
        if engine.engine(question, the_answer, name):
            counter += 1
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
