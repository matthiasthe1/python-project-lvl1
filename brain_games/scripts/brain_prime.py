#!/usr/bin/env python
import prompt
import random
import math


def checker(num):
    i = 2
    while (i <= int(math.sqrt(num))):
        if num % i == 0:
            return 'no'
            break
        i += 1
    return 'yes'


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while (counter < 3):
        num = random.randint(2, 100)
        print('Question: ', num)
        answr = input('Your answer: ')
        if answr == checker(num):
            print('Correct!')
            counter += 1
        elif answr != checker(num):
            print("'" + answr + "' is wrong answer ;(. Correct answer was " + checker(num) + "\nLet's try again, " + name + "!")
    print('Congradulations, ' + name + '!')


if __name__ == '__main__':
    main()
