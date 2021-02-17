import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ['*', '+', '-']


def answer_calculate(number_1, number_2, operation):
    if operation == '*':
        return number_1 * number_2
    elif operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2


def qa_generate():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    operation = random.choice(OPERATIONS)
    answer = str(answer_calculate(number_1, number_2, operation))
    question = '{0} {1} {2}'.format(number_1, operation, number_2)
    return (question, answer)
