from random import randint
import brain_games.enginy


def problem_and_correct_answer():
    problem = randint(1, 20)
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


def prime_game():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_games.enginy.welcome_us(question)

    counter = 0

    while counter < 3:
        counter = brain_games.enginy.comparison(problem_and_answer=problem_and_correct_answer(), counter=counter)
