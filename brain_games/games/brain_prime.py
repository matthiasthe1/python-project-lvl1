#!/usr/bin/env python
import math
import random
import prompt
from brain_games import engine


def qa_gen():
    number = random.randint(2, 100)
    i = 2
    answ = 'yes'
    while (i <= int(math.sqrt(number))):
        if number % i == 0:
            answ = 'no'
            break
        i += 1
    return (number, answ)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
