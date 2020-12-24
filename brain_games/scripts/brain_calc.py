#!/usr/bin/env python
import prompt
import random
from brain_games import engine


def eval(question):
    q_tupled = question[0].partition(question[1])
    if question[1] == ' * ':
        return int(q_tupled[0]) * int(q_tupled[2])
    elif question[1] == ' + ':
        return int(q_tupled[0]) + int(q_tupled[2])
    elif question[1] == ' - ':
        return int(q_tupled[0]) - int(q_tupled[2])


def question_generator():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    operations = [' * ', ' + ', ' - ']
    operation = random.choice(operations)
    return (str(number_1) + operation + str(number_2), operation)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    counter = 0
    while (counter < 3):
        question = question_generator()
        the_answer = eval(question)
        if engine.engine(question[0], the_answer, name):
            counter += 1
    print('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
