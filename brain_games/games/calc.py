from random import randint, choice
import operator


def calc_welcome():
    question = 'What is the result of the expression?'
    return question


def calc_game_logic():
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    action_key = list(action.keys())
    random_operation = choice(action_key)
    first_value = randint(10, 20)
    second_value = randint(1, 10)

    correct_answer = f'{action[random_operation](first_value, second_value)}'
    problem = f'{first_value} {random_operation} {second_value}'
    return problem, correct_answer
