#!/usr/bin/env python
import random
from brain_games import engine


NUMBER_OF_ROUNDS = 3
GAME_MESSANGE = 'Find the greatest common divisor of given numbers.'


def answer_calculate(number_1, number_2):
    while number_1 > 0 and number_2 > 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    if number_1 > number_2:
        answer = number_1
    else:
        answer = number_2
    return answer


def qa_generate():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    question = str(number_1) + ' ' + str(number_2)
    answer = answer_calculate(number_1, number_2)
    return (question, answer)


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
