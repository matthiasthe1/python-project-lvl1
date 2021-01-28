#!/usr/bin/env python
import random
from brain_games import engine


NUMBER_OF_ROUNDS = 3
GAME_MESSANGE = 'What number is missing in the progression?'


def answer_calculate(a_0, step, hid_pos):
    return a_0 + step * hid_pos


def qa_generate():
    step = random.randint(0, 10)
    a_0 = random.randint(0, 10)
    hid_pos = random.randint(0, 9)
    i = 0
    a = a_0
    question = ''
    while (i < 10):
        if i == hid_pos:
            question += '.. '
            a += step
        else:
            question += str(a) + ' '
            a += step
        i += 1
    answer = answer_calculate(a_0, step, hid_pos)
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
