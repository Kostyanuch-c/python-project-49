from random import randint
import brain_games.enginy


def problem_and_correct_answer():
    problem = randint(0, 200)

    if problem % 2 == 0:
        correct_answer = 'yes'
    elif problem % 2 != 0:
        correct_answer = 'no'
    else:
        correct_answer = 'no'
    return problem, correct_answer


def game_even():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_games.enginy.welcome_us(question)

    counter = 0
    while counter < 3:
        counter = brain_games.enginy.comparison(problem_and_answer=problem_and_correct_answer(), counter=counter)
