#!/usr/bin/env python
import random
from brain_games import engine


NUMBER_OF_ROUNDS = 3
GAME_MESSANGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def answer_calculate(number):
    if number % 2:
        return 'no'
    elif number % 2 == 0:
        return 'yes'


def qa_generate():
    counter = 0
    question_list = []
    answer_list = []
    while counter < NUMBER_OF_ROUNDS:
        number = random.randint(0, 100)
        answer = answer_calculate(number)
        question_list.append(number)
        answer_list.append(answer)
        counter += 1
    return (question_list, answer_list)


def game():
    q_a = qa_generate()
    engine.start(q_a[0], q_a[1], GAME_MESSANGE)
