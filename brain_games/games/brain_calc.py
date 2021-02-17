import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['*', '+', '-']


def calculate(number_1, number_2, operator):
    if operator == '*':
        return number_1 * number_2
    elif operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2


def qa_generate():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    operator = random.choice(OPERATORS)
    answer = str(calculate(number_1, number_2, operator))
    question = '{0} {1} {2}'.format(number_1, operator, number_2)
    return (question, answer)
