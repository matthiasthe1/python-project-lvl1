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
        out = 'Congratulations, {0}!'
        print(out.format(name))
    else:
        out = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
        print(out.format(answr, a[i]))
        print("Let's try again, " + name + "!")
    return
