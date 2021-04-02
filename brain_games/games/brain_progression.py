import random

LENGTH = 10
DESCRIPTION = 'What number is missing in the progression?'


def create_progression(start, step, LENGTH):
    return [start + step * i for i in range(0, LENGTH)]


def get_question(progression, hidden_element_index, marker='..'):
    copied_progression = progression[:]
    copied_progression[hidden_element_index] = marker
    return (' '.join(map(str, copied_progression)))


def generate_round():
    step = random.randint(0, 10)
    start = random.randint(0, 10)
    hidden_element_index = random.randint(0, 9)
    progression = create_progression(start, step, LENGTH)
    answer = str(progression[hidden_element_index])
    question = get_question(progression, hidden_element_index)
    return (question, answer)
