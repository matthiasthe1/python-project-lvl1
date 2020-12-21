#!/usr/bin/env python
import prompt
import random


def answer_check(answr, number):
    if number % 2 and answr == 'no':
        return True
    elif number % 2 == 0 and answr == 'yes':
        return True
    else:
        return False


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while (counter < 3):
        number = random.randint(0, 10000)
        print('Question: ', number)
        answr = input('Your answer: ')
        if answer_check(answr, number):
            print('Correct!')
            counter += 1
        elif number % 2:
            print("'" + answr + "' is wrong answer ;(. Correct answer was 'no'\nLet's try again, " + name + "!")
        elif number % 2 == 0:
            print("'" + answr + "' is wrong answer ;(. Correct answer was 'yes'\nLet's try again, " + name + "!")
    print('Congradulations, ' + name + '!')


if __name__ == '__main__':
    main()
