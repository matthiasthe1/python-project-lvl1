#!/usr/bin/env python
import prompt


def engine(question_list, answer_list, GAME_MESSANGE):
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(GAME_MESSANGE)
    round = 0
    is_correct = True
    while (round < 3):
        print('Question:', question_list[round])
        answer = input('Your answer: ')
        if str(answer_list[round]) == answer:
            print('Correct!')
            round += 1
        else:
            is_correct = False
            break
    if is_correct:
        print('Congratulations, {0}!'.format(name))
    else:
        out = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
        print(out.format(answer, answer_list[round]))
        print("Let's try again, " + name + "!")
    return
