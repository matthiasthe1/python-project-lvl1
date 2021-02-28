import random


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd_calculate(a, b):
    return gcd_calculate(b, a % b) if b else a


def generate_round():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    question = '{0} {1}'.format(str(number_1), str(number_2))
    answer = str(gcd_calculate(number_1, number_2))
    return (question, answer)
