import random

LENGTH = 10
GAME_DESCRIPTION = 'What number is missing in the progression?'
MARKER = '..'


def create_progression(start, step, LENGTH):
    return [start + step*x for x in range(0, LENGTH)]


def get_question(progression, hidden_index):
    str_progression = ' '.join(map(str,progression))
    str_progression[hidden_index] = MARKER
    return str_progression


def generate_round():
    step = random.randint(0, 10)
    start = random.randint(0, 10)
    hidden_index = random.randint(0, 9)
    progression = create_progression(start, step, LENGTH)
    answer = str(progression[hidden_index])
    question = get_question(progression, hidden_index)
    return (question, answer)
