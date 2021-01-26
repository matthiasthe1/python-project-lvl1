#!/usr/bin/env python
import math
import random
import prompt
from brain_games import engine


NUMBER_OF_ROUNDS = 3


def qa_gen():
    number = random.randint(2, 100)
    i = 2
    answer = 'yes'
    while (i <= int(math.sqrt(number))):
        if number % i == 0:
            answer = 'no'
            break
        i += 1
    return (number, answer)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
