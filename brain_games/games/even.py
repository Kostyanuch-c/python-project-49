from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return not number % 2


def problem_and_correct_answer():
    problem = randint(0, 200)
    correct_answer = 'yes' if is_even(problem) else 'no'

    return problem, correct_answer
