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
    number = random.randint(0, 100)
    answer = answer_calculate(number)
    return (number, answer)


def game():
    counter = 0
    question_list = []
    answer_list = []
    while counter < NUMBER_OF_ROUNDS:
        q_a = qa_generate()
        question_list.append(q_a[0])
        answer_list.append(q_a[1])
        counter += 1
    engine.engine(question_list, answer_list, GAME_MESSANGE)
