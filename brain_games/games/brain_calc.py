import random
import operator


DESCRIPTION = 'What is the result of the expression?'
map_operator_to_operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def calculate_answer(number_1, number_2, chosen_operator):
    return map_operator_to_operation[chosen_operator](number_1, number_2)


def generate_round():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, number_1)
    chosen_operator = random.choice(list(map_operator_to_operation.keys()))
    answer = str(calculate_answer(number_1, number_2, chosen_operator))
    question = '{0} {1} {2}'.format(number_1, chosen_operator, number_2)
    return (question, answer)
