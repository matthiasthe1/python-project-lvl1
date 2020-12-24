#!/usr/bin/env python
import random
import prompt
from brain_games import engine


def eval(question):
    a = question[0]
    b = question[1]
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a > b:
        return a
    else:
        return b


def question_generator():
    return (random.randint(0, 100), random.randint(0, 100))


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    counter = 0
    NUMBER_OF_ROUNDS = 3
    while (counter < NUMBER_OF_ROUNDS):
        question = question_generator()
        the_answer = eval(question)
        q = str(question[0]) + ' ' + str(question[1])
        if engine.engine(q, the_answer, name):
            counter += 1
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
