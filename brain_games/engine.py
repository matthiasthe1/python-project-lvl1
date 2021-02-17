import prompt


def start(game):
    greet()
    name = get_name(game)
    round = 0
    for round in range(game.NUMBER_OF_ROUNDS):
        question, correct_answer = game.qa_generate()
        show_question(question)
        answer = input('Your answer: ')
        if check(answer, correct_answer) is False:
            show_fail(answer, correct_answer, name)
            break
        else:
            show_correct()
    else:
        show_win(name)
    return


def greet():
    print('Welcome to Brain Games!')


def get_name(game):
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    print(game.GAME_DESCRIPTION)
    return player_name


def show_question(question):
    print('Question:', question)


def show_correct():
    print('Correct!')


def show_fail(answer, correct_answer, name):
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer)) # noqa
    print("Let's try again, {0}!".format(name))


def show_win(name):
    print("Congratulations, {}!".format(name))


def check(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False
