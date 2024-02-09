from random import randint


def welcome_question():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    return question


def problem_and_correct_answer():
    problem = randint(0, 200)

    if problem % 2 == 0:
        correct_answer = 'yes'
    elif problem % 2 != 0:
        correct_answer = 'no'
    else:
        correct_answer = 'no'
    return problem, correct_answer
