import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(a, b):
    return calculate_gcd(b, a % b) if b else a


def generate_round():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    question = '{0} {1}'.format(number_1, number_2)
    answer = str(calculate_gcd(number_1, number_2))
    return (question, answer)
