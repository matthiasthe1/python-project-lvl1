 #!/usr/bin/env python3
from brain_games import cli
import random
import operator


DESCRIPTION = 'What is the result of the expression?'
NUMBER_OF_ROUNDS = 3


map_operator_to_operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def calculate(number_1, number_2, chosen_operator):
    return map_operator_to_operation[chosen_operator](number_1, number_2)

def main():
    name = cli.welcome_user()
    print(DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, number_1)
        chosen_operator = random.choice(list(map_operator_to_operation.keys()))
        state = str(calculate(number_1, number_2, chosen_operator))
        question = '{0} {1} {2}'.format(number_1, chosen_operator, number_2)
        print(question)
        answer = input('Your answer: ')
        if answer != state:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'\nLet's try again, {2}!".format(answer, state, name))
            return
        else:
            print('Correct!')
    print("Congratulations, {}!".format(name))
            
if __name__ == "__main__":
    main()

