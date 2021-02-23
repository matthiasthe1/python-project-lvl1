import prompt


def start(game):
    print('Welcome to Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.GAME_DESCRIPTION)
    round = 0
    for round in range(game.NUMBER_OF_ROUNDS):
        question, correct_answer = game.generate_round()
        print('Question:', question)
        answer = input('Your answer: ')
        if check(answer, correct_answer) is False:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'\nLet's try again, {2}!".format(answer, correct_answer, name)) # noqa
            break
        else:
            print('Correct!')
    else:
        print("Congratulations, {}!".format(name))
    return


def check(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False
