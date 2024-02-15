from prompt import string


def welcome_us(question):
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}"
          f"\n{question}")
    return user_name


def user_answer():
    return string('Your answer: ')


def game_engine(game_module):
    user_name = welcome_us(game_module.QUESTION)
    counter = 0
    while counter < 3:

        problem, correct_answer = game_module.problem_and_correct_answer()

        print(f'Question: {problem}')
        answer = user_answer()
        if answer == correct_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
