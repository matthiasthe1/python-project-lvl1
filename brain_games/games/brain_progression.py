#!/usr/bin/env python
import random
import prompt
from brain_games import engine


NUMBER_OF_ROUNDS = 3


def qa_gen():
    step = random.randint(0, 10)
    a_0 = random.randint(0, 10)
    hid_pos = random.randint(0, 9)
    i = 0
    a = a_0
    question = ''
    while (i < 10):
        if i == hid_pos:
            question += '.. '
            answer = a
            a += step
        else:
            question += str(a) + ' '
            a += step
        i += 1
    return (question, answer)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    counter = 0
    question_list = []
    answer_list = []
    while counter < NUMBER_OF_ROUNDS:
        q_a = qa_gen()
        question_list.append(q_a[0])
        answer_list.append(q_a[1])
        counter += 1
    engine.engine(question_list, answer_list, name)


if __name__ == '__main__':
    main()
