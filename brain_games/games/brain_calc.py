#!/usr/bin/env python
import random
from brain_games import engine


NUMBER_OF_ROUNDS = 3
GAME_MESSANGE = 'What is the result of the expression?'


def answer_calculate(number_1, number_2, operation):
    if operation == ' * ':
        return number_1 * number_2
    elif operation == ' + ':
        return number_1 + number_2
    elif operation == ' - ':
        return number_1 - number_2


def qa_generate():
    counter = 0
    question_list = []
    answer_list = []
    while counter < NUMBER_OF_ROUNDS:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, number_1)
        operations = [' * ', ' + ', ' - ']
        operation = random.choice(operations)
        answer = answer_calculate(number_1, number_2, operation)
        question = str(number_1) + operation + str(number_2)
        question_list.append(question)
        answer_list.append(answer)
        counter += 1
    return (question_list, answer_list)


def game():
    q_a = qa_generate()
    engine.start(q_a[0], q_a[1], GAME_MESSANGE)
