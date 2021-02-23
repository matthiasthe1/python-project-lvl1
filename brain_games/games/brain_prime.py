import math
import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'   # noqa


def is_prime(number):
    i = 2
    while (i <= int(math.sqrt(number))):
        if number % i == 0:
            return False
        i += 1
    return True


def generate_round():
    number = random.randint(2, 100)
    answer = is_prime(number)
    answer = "yes" if (is_prime(number)) else "no"
    return (number, answer)
