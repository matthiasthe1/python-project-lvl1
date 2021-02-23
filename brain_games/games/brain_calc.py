import random
import operator


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def calculate(number_1, number_2, operation):
    return str(OPERATORS[operation](number_1, number_2))


def generate_round():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    operation = random.choice(list(OPERATORS.keys()))
    answer = calculate(number_1, number_2, operation)
    question = '{0} {1} {2}'.format(number_1, operation, number_2)
    return (question, answer)
