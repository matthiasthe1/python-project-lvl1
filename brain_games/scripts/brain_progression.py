#!/usr/bin/env python
import prompt
import random


def checker(number_1, number_2, operation):
    if operation == ' * ':
        result = number_1 * number_2
    elif operation == ' + ':
        result = number_1 + number_2
    elif operation == ' - ':
        result = number_1 - number_2
    return result


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    counter = 0
    while (counter < 3):
        step = random.randint(0, 10)
        a_0 = random.randint(0, 10)
        hid_pos = random.randint(0, 9)
        i = 0
        a = a_0
        print('Question: ')
        while (i < 10):
            if i == hid_pos:
                print('..', end=' ')
                hidden = a
                a += step
            else:
                print(a, end=' ')
                a += step
            i += 1
        answr = input('\nYour answer: ')
        if answr == str(hidden):
            print('Correct!')
            counter += 1
        elif answr != str(hidden):
            print("'" + str(answr) + "' is wrong answer ;(. Correct answer was " + str(hidden) + "\nLet's try again, " + name + "!")
    print('Congradulations, ' + name + '!')


if __name__ == '__main__':
    main()
