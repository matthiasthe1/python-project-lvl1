#!/usr/bin/env python


def engine(question, the_answer, name):
    print('Question:', question)
    answr = input('Your answer: ')
    if str(the_answer) == answr:
        print('Correct!')
        return True
    else:
        print("'" + str(answr) + "' is wrong answer ;(. Correct answer was '" + str(the_answer) + "'")
        print("Let's try again, " + name + "!")
        return False
