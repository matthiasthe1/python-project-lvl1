#!/usr/bin/env python


def engine(question, the_answer, name):
    print('Question: ', question)
    answr = input('Your answer: ')
    if the_answer == answr:
        print('Correct!')
        return True
    else:
        print("'" + str(answr) + "' is wrong answer ;(. Correct answer was " + the_answer)
        print("Let's try again, " + name + "!")
        return False
