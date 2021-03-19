import random
import operator


GAME_DESCRIPTION = 'What is the result of the expression?'
map_symbols_to_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_answer(number_1, number_2, random_operator):
    return str(map_symbols_to_operators[random_operator](number_1, number_2))


def generate_round():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    random_operator = random.choice(list(map_symbols_to_operators.keys()))
    answer = get_answer(number_1, number_2, random_operator)
    question = '{0} {1} {2}'.format(number_1, random_operator, number_2)
    return (question, answer)
