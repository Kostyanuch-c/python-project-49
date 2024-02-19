from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return bool(not number % 2)


def problem_and_correct_answer():
    problem = randint(0, 200)
    if is_even(problem):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return problem, correct_answer



