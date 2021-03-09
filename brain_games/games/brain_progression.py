import random


GAME_DESCRIPTION = 'What number is missing in the progression?'
MARKER = '..'


def create_progression(start, step, length):
    return [start + step*x for x in range(0, length)]


def get_question(progression, hidden_element):
    return ' '.join([MARKER if x == progression[hidden_element] else str(x) for x in progression])  # noqa


def generate_round():
    step = random.randint(0, 10)
    start = random.randint(0, 10)
    hidden_element = random.randint(0, 9)
    length = 10
    progression = create_progression(start, step, length)
    answer = str(progression[hidden_element])
    question = get_question(progression, hidden_element)
    return (question, answer)
