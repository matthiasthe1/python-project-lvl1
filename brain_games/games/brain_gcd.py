#!/usr/bin/env python
import random
import prompt
from brain_games import engine


def qa_gen():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    que = str(number_1) + ' ' + str(number_2)
    while number_1 > 0 and number_2 > 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    if number_1 > number_2:
        answ = number_1
    else:
        answ = number_2
    return (que, answ)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
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
