import math
import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'   # noqa


def is_prime(number):
    i = 2
    answer = 'yes'
    while (i <= int(math.sqrt(number))):
        if number % i == 0:
            answer = 'no'
            break
        i += 1
    return answer


def qa_generate():
    number = random.randint(2, 100)
    answer = is_prime(number)
    return (number, answer)
