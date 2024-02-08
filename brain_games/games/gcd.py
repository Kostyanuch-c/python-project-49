from random import randint
import brain_games.enginy


def algorithm_math(number_1, number_2):
    high_number = max([number_1, number_2])
    lst = []
    for i in range(1, high_number + 1):
        if number_1 % i == 0 and number_2 % i == 0:
            lst.append(i)
    return f'{max(lst)}'


def problem_and_correct_answer():
    first_value = randint(1, 10)
    second_value = randint(1, 20)

    correct_answer = algorithm_math(first_value, second_value)
    problem = f'{first_value} {second_value}'
    return problem, correct_answer


def gcd_game():
    question = 'Find the greatest common divisor of given numbers.'
    brain_games.enginy.welcome_us(question)

    counter = 0

    while counter < 3:
        counter = brain_games.enginy.comparison(problem_and_answer=problem_and_correct_answer(), counter=counter)
