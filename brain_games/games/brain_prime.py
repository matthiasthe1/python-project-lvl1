import math
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'   # noqa


def is_prime(number):
    i = 2
    while (i <= int(math.sqrt(number))):
        if number % i == 0:
            return False
        i += 1
    return True


def generate_round():
    number = random.randint(2, 100)
    answer = "yes" if is_prime(number) else "no"
    return (str(number), answer)
