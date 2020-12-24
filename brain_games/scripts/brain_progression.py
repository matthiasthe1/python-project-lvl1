#!/usr/bin/env python
import random
import prompt
from brain_games import engine


def question_generator():
    step = random.randint(0, 10)
    a_0 = random.randint(0, 10)
    hid_pos = random.randint(0, 9)
    i = 0
    a = a_0
    s = ''
    while (i < 10):
        if i == hid_pos:
            s += '.. '
            hidden = a
            a += step
        else:
            s += str(a) + ' '
            a += step
        i += 1
    return (s, hidden)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    counter = 0
    while (counter < 3):
        question = question_generator()
        the_answer = question[1]
        if engine.engine(question[0], the_answer, name):
            counter += 1
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
