#!/usr/bin/env python
import random
from brain_games import engine


NUMBER_OF_ROUNDS = 3
GAME_MESSANGE = 'What number is missing in the progression?'


def answer_calculate(a_0, step, hid_pos):
    return a_0 + step * hid_pos


def qa_generate():
    counter = 0
    question_list = []
    answer_list = []
    while counter < NUMBER_OF_ROUNDS:
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
        question_list.append(question)
        answer_list.append(answer)
        counter += 1
    return (question_list, answer_list)


def game():
    q_a = qa_generate()
    engine.start(q_a[0], q_a[1], GAME_MESSANGE)
