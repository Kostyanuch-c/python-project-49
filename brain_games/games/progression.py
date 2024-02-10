from random import randint


def welcome_question_progression():
    question = 'What number is missing in the progression?'
    return question


def problem_and_correct_answer_progression():
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
