import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    return "yes" if (question % 2 == 0) else "no"


def generate_round():
    question = random.randint(0, 100)
    answer = is_even(question)
    return (str(question), answer)
