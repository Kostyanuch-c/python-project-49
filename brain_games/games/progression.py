from random import randint
import brain_games.enginy


def problem_and_correct_answer():
    length_lst = randint(5, 12)
    step = randint(2, 8)

    first_element = randint(1, 20)
    progression = [f'{first_element}']

    for _ in range(length_lst - 1):
        first_element += step
        progression.append(str(first_element))

    delete_index = randint(0, length_lst - 1)

    correct_answer = progression[delete_index]

    progression[delete_index] = '..'

    problem = ' '.join(progression)
    return problem, correct_answer


def progression_game():
    question = 'What number is missing in the progression?'
    brain_games.enginy.welcome_us(question)

    counter = 0

    while counter < 3:
        counter = brain_games.enginy.comparison(problem_and_answer=problem_and_correct_answer(), counter=counter)

