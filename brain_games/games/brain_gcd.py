import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def answer_calculate(a, b):
    return answer_calculate(b, a % b) if b else a


def generate_round():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    question = '{0} {1}'.format(str(number_1), str(number_2))
    answer = str(answer_calculate(number_1, number_2))
    return (question, answer)
