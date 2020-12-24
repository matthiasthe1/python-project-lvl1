#!/usr/bin/env python
import math
import random
import prompt
from brain_games import engine


def eval(question):
    i = 2
    while (i <= int(math.sqrt(question))):
        if question % i == 0:
            return 'no'
            break
        i += 1
    return 'yes'


def question_generator():
    return random.randint(2, 100)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    counter = 0
    while (counter < 3):
        question = question_generator()
        the_answer = eval(question)
        if engine.engine(question, the_answer, name):
            counter += 1
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
