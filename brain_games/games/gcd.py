from random import randint

QUESTION = 'Find the greatest common divisor of given numbers.'


def algorithm_gcd(number_1, number_2):
    return algorithm_gcd(number_2, number_1 % number_2) \
        if (number_1 % number_2) else f'{abs(number_2)}'


def problem_and_correct_answer():
    first_value = randint(1, 10)
    second_value = randint(1, 20)

    correct_answer = algorithm_gcd(first_value, second_value)
    problem = f'{first_value} {second_value}'
    return problem, correct_answer
