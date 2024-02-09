from random import randint


def welcome_question():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return question


def problem_and_correct_answer():
    problem = randint(1, 35)
    divider_lst = []
    for number in range(1, problem + 1):
        divider_lst.append(number)

    for divider in divider_lst[:]:
        if problem % divider != 0:
            divider_lst.remove(divider)
    if len(divider_lst) == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return f'{problem}', correct_answer
