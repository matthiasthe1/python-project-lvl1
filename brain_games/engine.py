#!/usr/bin/env python


def engine(question_list, answer_list, name):
    i = 0
    f = True
    while (i < 3):
        print('Question:', question_list[i])
        answer = input('Your answer: ')
        if str(answer_list[i]) == answer:
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
        print(out.format(answer, answer_list[i]))
        print("Let's try again, " + name + "!")
    return
