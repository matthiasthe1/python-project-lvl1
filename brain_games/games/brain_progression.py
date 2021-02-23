import random


NUMBER_OF_ROUNDS = 3
GAME_DESCRIPTION = 'What number is missing in the progression?'
LENGTH = 10


def find_answer(start, step, hidden):
    return start + step * hidden


def generate_round():
    step = random.randint(0, 10)
    start = random.randint(0, 10)
    hidden = random.randint(0, 9)
    i = 0
    question = ''
    for i in range(LENGTH):
        if i == hidden:
            question += '.. '
            continue
        question += str(start + i * step) + ' '
    answer = str(find_answer(start, step, hidden))
    return (question, answer)
