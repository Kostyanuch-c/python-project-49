from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def problem_and_correct_answer():
    problem = randint(1, 30)
    divider_lst = list(range(1, problem + 1))

    for divider in divider_lst[:]:
        if problem % divider != 0:
            divider_lst.remove(divider)
    if len(divider_lst) == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return f'{problem}', correct_answer
