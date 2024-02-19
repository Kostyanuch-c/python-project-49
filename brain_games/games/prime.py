from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True


def problem_and_correct_answer():
    problem = randint(1, 30)
    if is_prime(problem):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return f'{problem}', correct_answer


