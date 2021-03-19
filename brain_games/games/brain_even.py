import random


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    return not(question % 2 == 0)


def generate_round():
    question = random.randint(0, 100)
    answer = 'yes' if is_even(question) else 'no'
    return (str(question), answer)
