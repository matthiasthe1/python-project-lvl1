import math
import random


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'   # noqa


def is_prime(question):
    i = 2
    while (i <= int(math.sqrt(question))):
        if question % i == 0:
            return False
        i += 1
    return True


def generate_round():
    question = random.randint(2, 100)
    answer = "yes" if is_prime(question) else "no"
    return (str(question), answer)
