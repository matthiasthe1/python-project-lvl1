#!/usr/bin/env python
from brain_games import cli


def engine(question, the_answer):
    print('Question: ', question)
    answr = input('Your answer: ')
    if the_answer == answr:
        print('Correct!')
        return True
    else:
        print("'" + str(answr) + "' is wrong answer ;(. Correct answer was " + the_answer)
        print("Let's try again, " + cli.name + "!")
        return False
