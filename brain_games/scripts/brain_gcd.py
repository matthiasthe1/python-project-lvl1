#!/usr/bin/env python
import prompt
import random


def checker(number_1, number_2):
    while number_1 > 0 and number_2 > 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    if number_1 > number_2:
        return number_1
    else:
        return number_2


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers. ')
    counter = 0
    while (counter < 3):
        number_1 = random.randint(0, 10000)
        number_2 = random.randint(0, 10000)
        print("Question: ", number_1, number_2)
        answr = input('Your answer: ')
        if answr == str(checker(number_1, number_2)):
            print('Correct!')
            counter += 1
        elif answr != checker(number_1, number_2):
            print("'" + str(answr) + "' is wrong answer ;(. Correct answer was " + str(checker(number_1, number_2)) + "\nLet's try again, " + name + "!")
    print('Congradulations, ' + name + '!')


if __name__ == '__main__':
    main()
