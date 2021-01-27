#!/usr/bin/env python
import prompt
import random
from brain_games import engine


NUMBER_OF_ROUNDS = 3
GAME_MESSANGE = 'What is the result of the expression?'


def calculate(number_1, number_2, operation):
    if operation == ' * ':
        return number_1 * number_2
    elif operation == ' + ':
        return number_1 + number_2
    elif operation == ' - ':
        return number_1 - number_2


def qa_gen():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    operations = [' * ', ' + ', ' - ']
    operation = random.choice(operations)
    answer = calculate(number_1, number_2, operation)
    question = str(number_1) + operation + str(number_2)
    return (question, answer)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(GAME_MESSANGE)
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
