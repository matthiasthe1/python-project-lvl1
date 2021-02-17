import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return "yes" if (number % 2 == 0) else "no"


def qa_generate():
    number = random.randint(0, 100)
    answer = is_even(number)
    return (str(number), answer)
