#!/usr/bin/env python
import random
import prompt
from brain_games import engine


def qa_gen():
    number = random.randint(0, 100)
    if number % 2:
        answ = 'no'
    elif number % 2 == 0:
        answ = 'yes'
    return (number, answ)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    NUMBER_OF_ROUNDS = 3
    counter = 0
    q = []
    a = []
    while counter < NUMBER_OF_ROUNDS:
        q_a = qa_gen()
        q.append(q_a[0])
        a.append(q_a[1])
        counter += 1
    engine.engine(q, a, name)


if __name__ == '__main__':
    main()
