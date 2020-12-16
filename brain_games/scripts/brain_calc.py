#!/usr/bin/env python
import prompt
import random

##def answer_check(answr, number):
##    if number % 2 and answr == 'no':
##        return True
##    elif number % 2 == 0 and answr == 'yes':
##        return True
##    else:
#    	return False
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
    print('What is the result of the expression?')
    counter = 0
    while (counter < 3):
        number_1 = random.randint(0, 10000)
        number_2 = random.randint(0, number_1)
        operations = [' * ', ' + ', ' - ']
        operation = random.choice(operations)
        print(number_1, operation, number_2)
        answr = input('Your answer: ')
        if answr == str(checker(number_1, number_2, operation)):
    	    print('Correct!')
    	    counter +=1
        elif answr != checker(number_1, number_2, operation):
    	    print( "'" + str(answr) + "' is wrong answer ;(. Correct answer was " + str(checker(number_1, number_2, operation)) + "\nLet's try again, " + name + "!")
    print('Congradulations, ' + name + '!')
    	
    

if __name__ == '__main__':
    main()
