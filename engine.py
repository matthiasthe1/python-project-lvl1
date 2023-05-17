import prompt


NUMBER_OF_ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.generate_round()
        print('Question:', question)
        answer = input('Your answer: ')
        if answer != correct_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'\nLet's try again, {2}!".format(answer, correct_answer, name)) # noqa
            return
        print('Correct!')
    print("Congratulations, {}!".format(name)) 
