from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_check(number):
    return 'yes' if number % 2 == 0 else 'no'


def problem_and_correct_answer():
    problem = randint(0, 200)

    correct_answer = parity_check(problem)

    return problem, correct_answer
