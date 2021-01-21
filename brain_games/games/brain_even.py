#!/usr/bin/env python
import random
import prompt
from brain_games import engine


def qa_gen():
    number = random.randint(0, 100)
    if number % 2:
        answer = 'no'
    elif number % 2 == 0:
        answer = 'yes'
    return (number, answer)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    NUMBER_OF_ROUNDS = 3
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
