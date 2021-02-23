import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'What number is missing in the progression?'
LENGTH = 10
MARKER = '..'


def create_progression(start, step):
    return [str(start+step*x) for x in range(0, LENGTH)]


def generate_round():
    step = random.randint(0, 10)
    start = random.randint(0, 10)
    hidden_element = random.randint(0, 9)
    progression = create_progression(start, step)
    answer = progression[hidden_element]
    progression[hidden_element] = MARKER
    question = ' '.join(progression)
    return (question, answer)
