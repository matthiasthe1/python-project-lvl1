import random

LENGTH = 10
GAME_DESCRIPTION = 'What number is missing in the progression?'
MARKER = '..'


def create_progression(start, step, length):
    return [start + step * x for x in range(0, length)]


def get_question(progression, hidden_index):
    progression = progression[:hidden_index - 1] + [MARKER] + progression[hidden_index:] # noqa
    return (' '.join(map(str, progression)))


def generate_round():
    step = random.randint(0, 10)
    start = random.randint(0, 10)
    hidden_index = random.randint(0, 9)
    length = LENGTH
    progression = create_progression(start, step, length)
    answer = str(progression[hidden_index])
    question = get_question(progression, hidden_index)
    return (question, answer)
