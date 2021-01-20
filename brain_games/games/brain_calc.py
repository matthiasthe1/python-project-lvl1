#!/usr/bin/env python
import prompt
import random
from brain_games import engine


def qa_gen():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    operations = [' * ', ' + ', ' - ']
    operation = random.choice(operations)
    if operation == ' * ':
        answ = number_1 * number_2
    elif operation == ' + ':
        answ = number_1 + number_2
    elif operation == ' - ':
        answ = number_1 - number_2
    return (str(number_1) + operation + str(number_2), answ)


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    NUMBER_OF_ROUNDS = 3
    counter = 0
    q = []
    a = []
    while counter < NUMBER_OF_ROUNDS:
        q_a = qa_gen()
        q.append(q_a[0])
        a.append(q_a[1])
        counter += 1
    engine.engine(q, a, name)


if __name__ == '__main__':
    main()
