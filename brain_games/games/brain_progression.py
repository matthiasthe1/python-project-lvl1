import random

LENGTH = 10
DESCRIPTION = 'What number is missing in the progression?'
MARKER = '..'


def create_progression(start, step, LENGTH):
    return [start + step * i for i in range(0, LENGTH)]


def get_question(progression, hidden_element_index):
    progression = progression[:hidden_element_index] + [MARKER] + progression[hidden_element_index + 1:] # noqa
    return (' '.join(map(str, progression)))


def generate_round():
    step = random.randint(0, 10)
    start = random.randint(0, 10)
    hidden_element_index = random.randint(0, 9)
    progression = create_progression(start, step, LENGTH)
    answer = str(progression[hidden_element_index])
    question = get_question(progression, hidden_element_index)
    return (question, answer)
