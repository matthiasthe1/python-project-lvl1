#!/usr/bin/env python


def engine(q, a, name):
    i = 0
    f = True
    while (i < 3):
        print('Question:', q[i])
        answr = input('Your answer: ')
        if str(a[i]) == answr:
            print('Correct!')
            i += 1
        else:
            f = False
            break
    if f:
        print('Congratulations, ' + name + '!')
    else:
        print("'" + str(answr) + "' is wrong answer ;(. Correct answer was '" + str(a[i]) + "'")
        print("Let's try again, " + name + "!")
    return
